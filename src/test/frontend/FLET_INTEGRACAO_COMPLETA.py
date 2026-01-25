# ====================================================================
# EXEMPLO PRÁTICO: Integração Flet + FastAPI com get_current_user
# ====================================================================
# Este exemplo mostra como usar seu projeto real com o padrão correto

import flet as ft
import requests
import json
import os
from typing import Optional, Dict, Any

# ============================================
# CONFIGURAÇÃO
# ============================================
API_BASE_URL = "http://localhost:8000"
TOKEN_FILE = ".auth_token"  # Arquivo oculto para guardar token


# ============================================
# CLASSE DE GERENCIAMENTO DE AUTENTICAÇÃO
# ============================================
class AuthManager:
    """Gerencia token localmente e coordena com backend"""
    
    def __init__(self, token_file: str = TOKEN_FILE):
        self.token: Optional[str] = None
        self.cargo: Optional[str] = None
        self.user_id: Optional[int] = None
        self.user_data: Optional[Dict[str, Any]] = None
        self.token_file = token_file
    
    def fazer_login(self, email: str, senha: str) -> tuple[bool, str]:
        """
        Faz login no backend
        
        Retorna:
            (sucesso: bool, mensagem: str)
        """
        try:
            # 1. ENVIA credenciais para backend
            response = requests.post(
                f"{API_BASE_URL}/auth-usuarios-admtelesil/login",
                json={"email": email, "senha": senha},
                timeout=5
            )
            
            if response.status_code != 200:
                return False, f"Erro: {response.json().get('detail', 'Login falhou')}"
            
            # 2. RECEBE resposta com token e cargo
            data = response.json()
            self.token = data.get("token")
            self.cargo = data.get("cargo", "user")
            
            # 3. SALVA em arquivo local
            self._salvar_token()
            
            return True, "Login bem-sucedido!"
        
        except requests.exceptions.Timeout:
            return False, "Erro: Timeout na conexão com servidor"
        except Exception as e:
            return False, f"Erro: {str(e)}"
    
    def carregar_token_salvo(self) -> bool:
        """Carrega token do arquivo se existir"""
        if not os.path.exists(self.token_file):
            return False
        
        try:
            with open(self.token_file, "r") as f:
                data = json.load(f)
            self.token = data.get("token")
            self.cargo = data.get("cargo")
            self.user_id = data.get("user_id")
            self.user_data = data.get("user_data")
            return True
        except:
            return False
    
    def _salvar_token(self):
        """Salva token em arquivo local"""
        data = {
            "token": self.token,
            "cargo": self.cargo,
            "user_id": self.user_id,
            "user_data": self.user_data
        }
        with open(self.token_file, "w") as f:
            json.dump(data, f)
        # Proteger arquivo (apenas owner pode ler/escrever)
        os.chmod(self.token_file, 0o600)
    
    def _get_headers(self) -> Dict[str, str]:
        """Retorna headers para requisição autenticada"""
        if not self.token:
            return {}
        return {"Authorization": f"Bearer {self.token}"}
    
    def requisicao_protegida(
        self, 
        metodo: str, 
        endpoint: str, 
        json_data: Optional[Dict] = None
    ) -> tuple[bool, Dict[str, Any]]:
        """
        Faz requisição protegida para o backend
        
        O backend executará get_current_user automaticamente!
        
        Args:
            metodo: "GET", "POST", "PUT", "DELETE"
            endpoint: "/admin/dashboard", "/meu-perfil", etc
            json_data: dados para POST/PUT
        
        Returns:
            (sucesso: bool, resposta: dict)
        """
        try:
            headers = self._get_headers()
            url = f"{API_BASE_URL}{endpoint}"
            
            if metodo == "GET":
                response = requests.get(url, headers=headers, timeout=5)
            elif metodo == "POST":
                response = requests.post(url, headers=headers, json=json_data, timeout=5)
            elif metodo == "PUT":
                response = requests.put(url, headers=headers, json=json_data, timeout=5)
            elif metodo == "DELETE":
                response = requests.delete(url, headers=headers, timeout=5)
            else:
                return False, {"erro": "Método HTTP inválido"}
            
            # Tratar respostas
            if response.status_code == 200 or response.status_code == 201:
                return True, response.json()
            elif response.status_code == 403:
                return False, {"erro": "Permissão negada (403)"}
            elif response.status_code == 401:
                self.logout()  # Token expirado
                return False, {"erro": "Sessão expirada, faça login novamente"}
            else:
                return False, response.json()
        
        except requests.exceptions.Timeout:
            return False, {"erro": "Timeout na conexão"}
        except Exception as e:
            return False, {"erro": str(e)}
    
    def pode_acessar(self, cargo_requerido: str) -> bool:
        """Verifica LOCALMENTE se tem permissão (checagem rápida)"""
        if not self.cargo:
            return False
        return self.cargo.lower() == cargo_requerido.lower()
    
    def pode_acessar_multiplos(self, cargos_permitidos: list[str]) -> bool:
        """Verifica se cargo está em uma lista de cargos permitidos"""
        if not self.cargo:
            return False
        return self.cargo.lower() in [c.lower() for c in cargos_permitidos]
    
    def logout(self):
        """Remove token e dados locais"""
        self.token = None
        self.cargo = None
        self.user_id = None
        self.user_data = None
        if os.path.exists(self.token_file):
            os.remove(self.token_file)


# ============================================
# APLICAÇÃO FLET COM AUTENTICAÇÃO
# ============================================
class AdminApp:
    """Aplicação Flet integrada com sistema de cargos"""
    
    def __init__(self):
        self.page = None
        self.auth = AuthManager()
    
    def main(self, page: ft.Page):
        """Função principal da app"""
        self.page = page
        self.page.title = "Sistema Admin com Roles"
        self.page.window.width = 900
        self.page.window.height = 700
        
        # Tentar carregar token salvo
        if self.auth.carregar_token_salvo():
            self._mostrar_tela_principal()
        else:
            self._mostrar_tela_login()
    
    # ===== TELA DE LOGIN =====
    def _mostrar_tela_login(self):
        """Mostra interface de login"""
        self.page.clean()
        
        email_input = ft.TextField(
            label="Email",
            width=300,
            border_color="blue"
        )
        senha_input = ft.TextField(
            label="Senha",
            password=True,
            width=300,
            border_color="blue"
        )
        status_text = ft.Text(size=12, color="red")
        
        def ao_clicar_entrar(_):
            status_text.value = "Carregando..."
            status_text.color = "blue"
            self.page.update()
            
            # Chamar login
            sucesso, mensagem = self.auth.fazer_login(
                email_input.value,
                senha_input.value
            )
            
            if sucesso:
                # Login bem-sucedido
                self._mostrar_tela_principal()
            else:
                # Mostrar erro
                status_text.value = mensagem
                status_text.color = "red"
                self.page.update()
        
        login_form = ft.Column(
            controls=[
                ft.Text("ACESSO AO SISTEMA", size=28, weight="bold", color="blue"),
                ft.Divider(),
                email_input,
                senha_input,
                ft.ElevatedButton(
                    "Entrar",
                    on_click=ao_clicar_entrar,
                    width=300,
                    height=50
                ),
                status_text,
                ft.Text("Teste com cargo diferente!", size=11, italic=True, color="gray"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
        )
        
        self.page.add(
            ft.Container(
                content=login_form,
                alignment=ft.alignment.center,
                expand=True,
                bgcolor="white"
            )
        )
    
    # ===== TELA PRINCIPAL =====
    def _mostrar_tela_principal(self):
        """Mostra interface principal (adapta por cargo)"""
        self.page.clean()
        
        # Header com informações do usuário
        header = self._criar_header()
        
        # Seções conforme cargo
        secoes = []
        secoes.append(self._criar_secao_perfil())
        
        # Se for admin ou manager: mostrar seção de relatórios
        if self.auth.pode_acessar_multiplos(["admin", "manager"]):
            secoes.append(self._criar_secao_relatorios())
        
        # Se for admin: mostrar painel administrativo
        if self.auth.pode_acessar("admin"):
            secoes.append(self._criar_secao_admin())
        
        # Montar página
        conteudo = ft.Column(
            controls=[header, ft.Divider()] + secoes,
            scroll="auto",
            expand=True,
            spacing=20,
            padding=20,
        )
        
        self.page.add(conteudo)
    
    def _criar_header(self) -> ft.Container:
        """Header com informações do usuário"""
        return ft.Container(
            content=ft.Row(
                controls=[
                    ft.Column(
                        controls=[
                            ft.Text("Sistema Admin", size=24, weight="bold"),
                            ft.Text(
                                f"Cargo: {self.auth.cargo.upper()}",
                                size=14,
                                color="blue" if self.auth.cargo == "admin" else "green"
                            ),
                        ]
                    ),
                    ft.Container(expand=True),
                    ft.IconButton(
                        ft.icons.LOGOUT,
                        icon_size=30,
                        tooltip="Sair",
                        on_click=lambda _: self._fazer_logout()
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=15,
            bgcolor="lightgray",
            border_radius=10,
        )
    
    def _criar_secao_perfil(self) -> ft.Container:
        """Seção: MEU PERFIL (visível para todos)"""
        
        def ao_clicar_meu_perfil(_):
            # Aqui, requisição com get_current_user no backend!
            sucesso, dados = self.auth.requisicao_protegida("GET", "/admin/meu-perfil")
            
            if sucesso:
                # get_current_user foi executado no backend automaticamente
                self._mostrar_snackbar(f"✓ Perfil carregado: {dados.get('nome')}")
            else:
                self._mostrar_snackbar(f"✗ Erro: {dados.get('erro')}")
        
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("👤 MEU PERFIL", size=18, weight="bold", color="green"),
                    ft.Text(
                        "Requisição que usa get_current_user no backend",
                        size=12,
                        italic=True,
                        color="gray"
                    ),
                    ft.ElevatedButton(
                        "Ver Meu Perfil",
                        on_click=ao_clicar_meu_perfil,
                        width=300,
                    ),
                    ft.Text(
                        "Fluxo: Flet envia token → Backend executa get_current_user → Retorna dados",
                        size=11,
                        color="gray",
                        italic=True
                    ),
                ]
            ),
            padding=15,
            bgcolor="lightgreen",
            border_radius=10,
        )
    
    def _criar_secao_relatorios(self) -> ft.Container:
        """Seção: RELATÓRIOS (admin e manager)"""
        
        def ao_clicar_relatorios(_):
            # Requisição com require_roles("admin", "manager") no backend
            sucesso, dados = self.auth.requisicao_protegida("GET", "/admin/relatorios")
            
            if sucesso:
                self._mostrar_snackbar(f"✓ Relatório gerado!")
            else:
                self._mostrar_snackbar(f"✗ {dados.get('erro')}")
        
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("📊 RELATÓRIOS", size=18, weight="bold", color="blue"),
                    ft.Text(
                        "Requisição com require_roles('admin', 'manager')",
                        size=12,
                        italic=True,
                        color="gray"
                    ),
                    ft.ElevatedButton(
                        "Gerar Relatório",
                        on_click=ao_clicar_relatorios,
                        width=300,
                    ),
                    ft.Text(
                        f"Seu cargo ({self.auth.cargo}) tem permissão! ✓",
                        size=11,
                        color="green",
                        italic=True
                    ),
                ]
            ),
            padding=15,
            bgcolor="lightblue",
            border_radius=10,
        )
    
    def _criar_secao_admin(self) -> ft.Container:
        """Seção: PAINEL ADMIN (apenas admin)"""
        
        def ao_clicar_dashboard(_):
            # Requisição com require_roles("admin") no backend
            sucesso, dados = self.auth.requisicao_protegida("GET", "/admin/dashboard")
            
            if sucesso:
                mensagem = f"✓ {dados.get('mensagem')}"
                self._mostrar_snackbar(mensagem)
            else:
                self._mostrar_snackbar(f"✗ {dados.get('erro')}")
        
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("🔐 PAINEL ADMINISTRATIVO", size=18, weight="bold", color="red"),
                    ft.Text(
                        "Requisição com require_roles('admin')",
                        size=12,
                        italic=True,
                        color="gray"
                    ),
                    ft.Text(
                        "APENAS ADMIN VÊ ISSO!",
                        size=13,
                        weight="bold",
                        color="red"
                    ),
                    ft.ElevatedButton(
                        "Acessar Dashboard",
                        on_click=ao_clicar_dashboard,
                        width=300,
                    ),
                    ft.Text(
                        "Se fizer login com outro cargo, esta seção desaparece!",
                        size=11,
                        color="orange",
                        italic=True
                    ),
                ]
            ),
            padding=15,
            bgcolor="lightyellow",
            border_radius=10,
        )
    
    def _mostrar_snackbar(self, mensagem: str):
        """Mostra mensagem na tela"""
        self.page.snack_bar = ft.SnackBar(ft.Text(mensagem))
        self.page.snack_bar.open = True
        self.page.update()
    
    def _fazer_logout(self):
        """Remove token e volta para login"""
        self.auth.logout()
        self._mostrar_tela_login()


# ============================================
# EXECUTAR APLICAÇÃO
# ============================================
if __name__ == "__main__":
    app = AdminApp()
    ft.app(target=app.main)


# ============================================
# INSTRUÇÕES DE USO
# ============================================
"""
1. PREPARAR BACKEND:
   $ cd src
   $ uvicorn main:app --reload
   
   Certifique-se de que as rotas existem em backend/routers/users.py:
   - POST /auth-usuarios-admtelesil/login
   - GET /admin/meu-perfil (com Depends(get_current_user))
   - GET /admin/dashboard (com Depends(require_roles("admin")))
   - GET /admin/relatorios (com Depends(require_roles("admin", "manager")))

2. CRIAR USUÁRIOS DE TESTE:
   $ curl -X POST "http://localhost:8000/auth-usuarios-admtelesil/sign-up" \\
     -H "Content-Type: application/json" \\
     -d '{"nome":"Admin","sobrenome":"User","email":"admin@teste.com","senha":"123456"}'
   
   Depois alterar no banco: UPDATE Usuarios SET cargo='admin' WHERE email='admin@teste.com'

3. EXECUTAR FLET:
   $ python FLET_INTEGRACAO_COMPLETA.py

4. TESTAR:
   - Login com admin@teste.com / 123456
   - Ver todas as seções
   - Clicar em cada botão (mostra como get_current_user funciona)
   - Fazer logout
   - Login com outro cargo
   - Ver que seção admin desaparece

5. ENTENDER FLUXO:
   Flet envia token
   ↓
   Backend recebe em Depends(get_current_user)
   ↓
   get_current_user decodifica + busca user
   ↓
   require_roles valida cargo
   ↓
   Função executa ou retorna 403
   ↓
   Flet recebe resposta
"""
