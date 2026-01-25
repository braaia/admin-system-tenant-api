# ===================================
# EXEMPLO: Rotas Protegidas no FastAPI
# ===================================
# Localização: src/backend/routers/exemplo_admin_routes.py
# Este é um arquivo de EXEMPLO para mostrar como usar require_roles

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.dependencies import get_db
from backend.schemas import UsuariosOut
from backend.security.util.protectedRoute import get_current_user, require_roles

router = APIRouter(prefix="/admin", tags=["Admin"])

# ===== EXEMPLO 1: Proteger com require_roles =====
# Apenas usuários com cargo "admin" podem acessar
@router.get("/dashboard", response_model=dict)
def admin_dashboard(
    current_user: UsuariosOut = Depends(require_roles("admin"))
):
    """
    Painel administrativo - ACESSO RESTRITO AO CARGO 'admin'
    
    Se tentar acessar com outro cargo, retorna:
    HTTPException(403, detail="Permissão negada")
    """
    return {
        "mensagem": f"Bem-vindo, {current_user.nome}!",
        "cargo": current_user.cargo,
        "email": current_user.email
    }


# ===== EXEMPLO 2: Permitir múltiplos cargos =====
# Tanto "admin" quanto "manager" podem acessar
@router.get("/relatorios")
def relatorios(
    current_user: UsuariosOut = Depends(require_roles("admin", "manager"))
):
    """
    Relatórios - ACESSO PARA ADMIN E MANAGER
    """
    return {
        "mensagem": f"{current_user.nome}, aqui estão seus relatórios",
        "cargo": current_user.cargo
    }


# ===== EXEMPLO 3: Apenas usuário autenticado (sem cargo específico) =====
# Qualquer usuário autenticado pode acessar
@router.get("/meu-perfil")
def meu_perfil(
    current_user: UsuariosOut = Depends(get_current_user)
):
    """
    Perfil do usuário - ACESSO APENAS AUTENTICADO
    Qualquer cargo pode ver seu próprio perfil
    """
    return {
        "id": current_user.id,
        "nome": current_user.nome,
        "email": current_user.email,
        "cargo": current_user.cargo
    }


# ===== EXEMPLO 4: Usando dependencies no decorator =====
@router.post(
    "/usuario/atualizar-cargo",
    dependencies=[Depends(require_roles("admin"))]
)
def atualizar_cargo_usuario(user_id: int, novo_cargo: str):
    """
    Atualizar cargo de usuário - ACESSO APENAS ADMIN
    
    Usando 'dependencies' no decorator ao invés de parâmetro da função.
    É útil quando você não precisa usar 'current_user' na função.
    """
    # Lógica para atualizar cargo do usuário
    return {
        "sucesso": True,
        "mensagem": f"Cargo do usuário {user_id} atualizado para {novo_cargo}"
    }


# ===== RESUMO: Como funciona =====
"""
1. require_roles("admin") retorna uma FUNÇÃO que:
   - Usa get_current_user para autenticar via token
   - Verifica se current_user.cargo está na lista de permissões
   - Lança HTTPException(403) se não tiver permissão

2. Ordem de verificação no require_roles:
   a) Token válido? Se não → HTTPException(401)
   b) Usuário existe? Se não → HTTPException(401)
   c) cargo do usuário está em allowed_roles? Se não → HTTPException(403)
   d) Se sim → passa current_user para a função

3. Exemplos de chamadas:
   - require_roles("admin")              → apenas admin
   - require_roles("admin", "manager")   → admin ou manager
   - require_roles("user")               → apenas user
   - get_current_user                    → qualquer autenticado

4. Onde colocar no seu projeto:
   - Copie os decoradores @router.get ou @router.post
   - Importe: from backend.security.util.protectedRoute import require_roles, get_current_user
   - Adapte a lógica para sua aplicação
"""
