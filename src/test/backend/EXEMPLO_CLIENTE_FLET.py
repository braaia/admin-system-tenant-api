# ===================================
# EXEMPLO: Cliente Flet com Autenticação
# ===================================
# Este é um arquivo de EXEMPLO para mostrar como:
# 1. Fazer login
# 2. Guardar token seguramente
# 3. Usar cargo para condicionar a interface

import flet as ft
import requests
import json
import os
from pathlib import Path
from typing import Optional, Dict

# ===== CONFIGURAÇÃO =====
API_BASE_URL = "http://localhost:8000"
TOKEN_FILE = "auth_token.json"  # Arquivo local para guardar token

class AdminFletApp:
    """Aplicação Flet com controle de acesso por cargo"""
    
    def __init__(self):
        self.page = None
    
    def main(self, page: ft.Page):
        self.page = page
        page.title = "Sistema de Admin - Com Roles"
        page.window.width = 800
        page.window.height = 600
        
    # ===== TELA PRINCIPAL =====
    def show_main_interface(self):
        """Mostra interface principal com controle de acesso por cargo"""
        self.page.clean()
        
        # Componentes que TODOS veem
        header = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Text(f"Bem-vindo, {self.auth.user_name}!", size=20, weight="bold"),
                    ft.Text(f"Cargo: {self.auth.cargo}", size=14, color="blue"),
                    ft.IconButton(
                        ft.icons.LOGOUT,
                        on_click=lambda _: self.logout()
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            padding=20,
            bgcolor="lightgray"
        )
        
        # ===== SEÇÕES CONDICIONADAS POR CARGO =====
        
        # SEÇÃO 1: Visível apenas para ADMIN
        admin_section = self.create_admin_section()
        
        # SEÇÃO 2: Visível para ADMIN e MANAGER
        manager_section = self.create_manager_section()
        
        # SEÇÃO 3: Visível para todos
        user_section = self.create_user_section()
        
        # Montar a página
        content = ft.Column(
            controls=[
                header,
                ft.Divider(),
                user_section,  # Sempre visível
            ],
            scroll="auto",
            expand=True
        )
        
        # Adicionar seções conforme o cargo
        if self.auth.cargo and self.auth.cargo.lower() in ["admin", "manager"]:
            content.controls.append(manager_section)
        
        if self.auth.cargo and self.auth.cargo.lower() == "admin":
            content.controls.append(admin_section)
        
        self.page.add(content)
    
    def create_admin_section(self) -> ft.Container:
        """Seção visível APENAS para admin"""
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("🔐 PAINEL ADMINISTRATIVO", size=18, weight="bold", color="red"),
                    ft.Text("Apenas usuários com cargo 'admin' veem isso"),
                    ft.ElevatedButton(
                        "Gerenciar Usuários",
                        on_click=lambda _: self.alert("Abrindo gerenciador de usuários...")
                    ),
                    ft.ElevatedButton(
                        "Atualizar Cargos",
                        on_click=lambda _: self.alert("Abrindo atualizar cargos...")
                    ),
                    ft.ElevatedButton(
                        "Ver Logs do Sistema",
                        on_click=lambda _: self.alert("Abrindo logs...")
                    ),
                ]
            ),
            padding=15,
            bgcolor="lightyellow",
            border_radius=10,
        )
    
    def create_manager_section(self) -> ft.Container:
        """Seção visível para admin e manager"""
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("📊 RELATÓRIOS", size=18, weight="bold", color="blue"),
                    ft.Text("Disponível para admin e manager"),
                    ft.ElevatedButton(
                        "Gerar Relatório",
                        on_click=lambda _: self.call_protected_api(
                            "/admin/relatorios",
                            "Relatório gerado com sucesso!"
                        )
                    ),
                    ft.ElevatedButton(
                        "Exportar Dados",
                        on_click=lambda _: self.alert("Exportando dados...")
                    ),
                ]
            ),
            padding=15,
            bgcolor="lightblue",
            border_radius=10,
        )
    
    def create_user_section(self) -> ft.Container:
        """Seção visível para todos os usuários"""
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("👤 MEU PERFIL", size=18, weight="bold", color="green"),
                    ft.Text("Disponível para todos os usuários"),
                    ft.ElevatedButton(
                        "Ver Meu Perfil",
                        on_click=lambda _: self.call_protected_api(
                            "/admin/meu-perfil",
                            "Perfil carregado!"
                        )
                    ),
                    ft.ElevatedButton(
                        "Alterar Senha",
                        on_click=lambda _: self.alert("Abrindo alterar senha...")
                    ),
                ]
            ),
            padding=15,
            bgcolor="lightgreen",
            border_radius=10,
        )
    
    def call_protected_api(self, endpoint: str, success_msg: str):
        """Chama API protegida usando o token"""
        try:
            headers = self.auth.get_headers()
            response = requests.get(
                f"{API_BASE_URL}{endpoint}",
                headers=headers,
                timeout=5
            )
            
            if response.status_code == 200:
                self.alert(f"{success_msg}\nResposta: {response.json()}")
            elif response.status_code == 403:
                self.alert("❌ Acesso negado! Você não tem permissão para isso.")
            else:
                self.alert(f"❌ Erro: {response.json().get('detail', 'Erro desconhecido')}")
        
        except Exception as e:
            self.alert(f"❌ Erro de conexão: {str(e)}")
    
    def logout(self):
        """Desconectar e limpar token"""
        self.auth.clear_token()
        self.show_login_interface()
    
    def alert(self, message: str):
        """Mostra alerta na tela"""
        self.page.snack_bar = ft.SnackBar(ft.Text(message))
        self.page.snack_bar.open = True
        self.page.update()


# ===== EXECUTAR APLICAÇÃO =====
if __name__ == "__main__":
    app = AdminFletApp()
    ft.app(target=app.main)


# ===== INSTRUÇÕES DE USO =====
"""
1. PREPARAÇÃO:
   - Instale Flet: pip install flet
   - Instale requests: pip install requests
   - Certifique-se de que a API FastAPI está rodando em http://localhost:8000

2. COMO FUNCIONA:
   a) Na primeira execução: mostra tela de login
   b) Após login: salva token em 'auth_token.json' (arquivo local)
   c) Interface adapta baseado em self.auth.cargo:
      - "admin"   → vê seções admin + manager + user
      - "manager" → vê seções manager + user
      - "user"    → vê apenas seção user

3. ARMAZENAMENTO DO TOKEN:
   - Arquivo: auth_token.json (na mesma pasta do script)
   - Formato: JSON com token, cargo, user_id, user_name
   - Segurança: chmod 0o600 (apenas leitura do dono)
   - Para remover token: clique em logout ou delete auth_token.json

4. FECHAR SESSÃO:
   - Clique no ícone de logout (canto superior direito)
   - Isso deleta o arquivo auth_token.json
   - Próxima execução pedirá login novamente

5. EXEMPLOS DE CARGO:
   - "admin"   → acesso total
   - "manager" → acesso a relatórios
   - "user"    → acesso apenas perfil básico

6. TESTANDO:
   - Crie dois usuários com cargos diferentes no banco
   - Faça login com cada um
   - Veja como a interface muda!
"""
