# ====================================================================
# TESTE RÁPIDO: Verificar se seu sistema de cargos está funcionando
# ====================================================================

"""
Execute este script para testar:
1. Se o backend está rodando
2. Se login funciona
3. Se get_current_user funciona
4. Se require_roles funciona

Uso:
    python TESTAR_SISTEMA.py
"""

import requests
import json
from datetime import datetime

# ============================================
# CONFIGURAÇÃO
# ============================================
API_URL = "http://localhost:8000"
EMAIL_TESTE = "admin@teste.com"
SENHA_TESTE = "123456"

class cor:
    """ANSI colors para output no terminal"""
    VERDE = '\033[92m'
    VERMELHO = '\033[91m'
    AMARELO = '\033[93m'
    AZUL = '\033[94m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def print_teste(nome: str):
    print(f"\n{cor.BOLD}{cor.AZUL}{'='*60}{cor.RESET}")
    print(f"{cor.AZUL}📝 TESTE: {nome}{cor.RESET}")
    print(f"{cor.BOLD}{cor.AZUL}{'='*60}{cor.RESET}\n")

def print_sucesso(msg: str):
    print(f"{cor.VERDE}✓ {msg}{cor.RESET}")

def print_erro(msg: str):
    print(f"{cor.VERMELHO}✗ {msg}{cor.RESET}")

def print_info(msg: str):
    print(f"{cor.AMARELO}ℹ {msg}{cor.RESET}")

def print_resultado(titulo: str, resultado: dict, status_esperado: int = 200):
    print(f"\n{cor.BOLD}Resposta:{cor.RESET}")
    print(json.dumps(resultado, indent=2, ensure_ascii=False))
    
    if "status" in resultado and resultado["status"] != status_esperado:
        print_erro(f"Status: {resultado['status']} (esperado: {status_esperado})")
        return False
    else:
        print_sucesso(f"Status: OK")
        return True

# ============================================
# TESTES
# ============================================

def teste_1_api_online():
    """Teste 1: Verificar se API está online"""
    print_teste("1. API está online?")
    
    try:
        response = requests.get(f"{API_URL}/docs", timeout=5)
        if response.status_code == 200:
            print_sucesso(f"API está rodando em {API_URL}")
            return True
        else:
            print_erro(f"API retornou status {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print_erro(f"Não consegui conectar em {API_URL}")
        print_info("Execute: cd src && uvicorn main:app --reload")
        return False
    except Exception as e:
        print_erro(f"Erro: {str(e)}")
        return False

def teste_2_signup():
    """Teste 2: Criar usuário de teste"""
    print_teste("2. Criar usuário de teste")
    
    try:
        dados = {
            "nome": "Teste",
            "sobrenome": "Admin",
            "email": EMAIL_TESTE,
            "senha": SENHA_TESTE
        }
        
        response = requests.post(
            f"{API_URL}/auth-usuarios-admtelesil/sign-up",
            json=dados,
            timeout=5
        )
        
        if response.status_code == 201:
            print_sucesso(f"Usuário criado: {EMAIL_TESTE}")
            print_resultado("Sign-up", response.json(), 201)
            return True
        elif response.status_code == 400:
            print_info(f"Usuário já existe (ok para teste)")
            return True
        else:
            print_erro(f"Status: {response.status_code}")
            print_resultado("Sign-up", response.json())
            return False
    
    except Exception as e:
        print_erro(f"Erro: {str(e)}")
        return False

def teste_3_login():
    """Teste 3: Login e receber token"""
    print_teste("3. Login com credenciais")
    
    try:
        dados = {
            "email": EMAIL_TESTE,
            "senha": SENHA_TESTE
        }
        
        response = requests.post(
            f"{API_URL}/auth-usuarios-admtelesil/login",
            json=dados,
            timeout=5
        )
        
        if response.status_code == 200:
            resposta = response.json()
            
            if "token" not in resposta:
                print_erro("Resposta não contém 'token'")
                return False, None
            
            if "cargo" not in resposta:
                print_erro("Resposta não contém 'cargo'")
                print_info("Verifique se seu authHandler.py foi atualizado")
                return False, None
            
            token = resposta["token"]
            cargo = resposta.get("cargo", "desconhecido")
            
            print_sucesso(f"Login bem-sucedido!")
            print_sucesso(f"Token recebido (primeiros 50 chars): {token[:50]}...")
            print_sucesso(f"Cargo do usuário: {cargo}")
            print_resultado("Login", resposta)
            
            return True, token
        else:
            print_erro(f"Login falhou com status {response.status_code}")
            print_resultado("Login", response.json())
            return False, None
    
    except Exception as e:
        print_erro(f"Erro: {str(e)}")
        return False, None

def teste_4_get_current_user(token: str):
    """Teste 4: Usar get_current_user em rota"""
    print_teste("4. Usar get_current_user em rota protegida")
    
    if not token:
        print_erro("Token não disponível (teste anterior falhou)")
        return False
    
    try:
        headers = {"Authorization": f"Bearer {token}"}
        
        # Tentar acessar /admin/meu-perfil (que usa get_current_user)
        response = requests.get(
            f"{API_URL}/admin/me",
            headers=headers,
            timeout=5
        )
        
        if response.status_code == 200:
            print_sucesso("get_current_user funcionou!")
            print_info("Backend decodificou o token e retornou dados do usuário")
            print_resultado("get_current_user", response.json())
            return True
        elif response.status_code == 404:
            print_erro("Rota /admin/meu-perfil não encontrada")
            print_info("Você precisa criar essa rota com Depends(get_current_user)")
            print_info("Veja EXEMPLO_ROTAS_PROTEGIDAS.py para exemplo")
            return False
        else:
            print_erro(f"Status: {response.status_code}")
            print_resultado("get_current_user", response.json())
            return False
    
    except Exception as e:
        print_erro(f"Erro: {str(e)}")
        return False

def teste_5_require_roles(token: str):
    """Teste 5: Testar require_roles com admin"""
    print_teste("5. Testar require_roles com cargo 'admin'")
    
    if not token:
        print_erro("Token não disponível")
        return False
    
    try:
        headers = {"Authorization": f"Bearer {token}"}
        
        # Tentar acessar /admin/dashboard (que usa require_roles("admin"))
        response = requests.get(
            f"{API_URL}/admin/tests/role-test",
            headers=headers,
            timeout=5
        )
        
        if response.status_code == 200:
            print_sucesso("require_roles funcionou!")
            print_info("Seu cargo é 'admin' e você tem acesso")
            print_resultado("require_roles", response.json())
            return True
        elif response.status_code == 403:
            print_erro("Acesso negado (403)")
            print_info("Seu cargo não é 'admin'")
            print_info("No banco, atualize: UPDATE Usuarios SET cargo='admin' WHERE email='...'")
            return False
        elif response.status_code == 404:
            print_erro("Rota /admin/dashboard não encontrada")
            print_info("Você precisa criar essa rota com Depends(require_roles('admin'))")
            print_info("Veja EXEMPLO_ROTAS_PROTEGIDAS.py para exemplo")
            return False
        else:
            print_erro(f"Status: {response.status_code}")
            print_resultado("require_roles", response.json())
            return False
    
    except Exception as e:
        print_erro(f"Erro: {str(e)}")
        return False

def teste_6_token_invalido():
    """Teste 6: Testar com token inválido"""
    print_teste("6. Testar proteção com token inválido")
    
    try:
        headers = {"Authorization": "Bearer token_invalido_xyz"}
        
        response = requests.get(
            f"{API_URL}/admin/me",
            headers=headers,
            timeout=5
        )
        
        if response.status_code == 401:
            print_sucesso("Proteção funcionou!")
            print_info("Token inválido foi rejeitado com 401")
            print_resultado("Token inválido", response.json(), 401)
            return True
        else:
            print_erro(f"Esperava 401, mas recebi {response.status_code}")
            return False
    
    except Exception as e:
        print_erro(f"Erro: {str(e)}")
        return False

def teste_7_sem_header():
    """Teste 7: Testar sem enviar token"""
    print_teste("7. Testar proteção sem token no header")
    
    try:
        # Sem header Authorization
        response = requests.get(
            f"{API_URL}/admin/me",
            timeout=5
        )
        
        if response.status_code == 401:
            print_sucesso("Proteção funcionou!")
            print_info("Requisição sem token foi rejeitada com 401")
            print_resultado("Sem token", response.json(), 401)
            return True
        else:
            print_erro(f"Esperava 401, mas recebi {response.status_code}")
            return False
    
    except Exception as e:
        print_erro(f"Erro: {str(e)}")
        return False

# ============================================
# EXECUTAR TESTES
# ============================================

def main():
    print(f"\n{cor.BOLD}{cor.AZUL}")
    print("╔════════════════════════════════════════════════════╗")
    print("║   TESTE DO SISTEMA DE CARGOS FastAPI + Flet       ║")
    print("║   " + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "                          ║")
    print("╚════════════════════════════════════════════════════╝")
    print(cor.RESET)
    
    # Teste 1
    if not teste_1_api_online():
        print_erro("\n❌ API não está online. Abortando testes.")
        return
    
    # Teste 2
    teste_2_signup()
    
    # Teste 3
    ok_login, token = teste_3_login()
    if not ok_login:
        print_erro("\n❌ Login falhou. Abortando testes restantes.")
        return
    
    # Teste 4
    teste_4_get_current_user(token)
    
    # Teste 5
    teste_5_require_roles(token)
    
    # Teste 6
    teste_6_token_invalido()
    
    # Teste 7
    teste_7_sem_header()
    
    # Resumo
    print(f"\n{cor.BOLD}{cor.AZUL}")
    print("╔════════════════════════════════════════════════════╗")
    print("║            ✓ TESTES CONCLUÍDOS                     ║")
    print("╚════════════════════════════════════════════════════╝")
    print(cor.RESET)
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{cor.VERMELHO}Testes interrompidos pelo usuário{cor.RESET}")
    except Exception as e:
        print(f"\n{cor.VERMELHO}Erro inesperado: {str(e)}{cor.RESET}")
