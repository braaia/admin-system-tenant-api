import threading
import uvicorn
from decouple import config
from fastapi import FastAPI, Depends, Request, APIRouter

from backend.db_init import init_database
from backend.routers import materials, users
from backend.schemas import UsuariosOut
from backend.security.util.protectedRoute import require_roles, get_current_user

# region APP
app = FastAPI(
    title="API Admin System",
    description="Desenvolvido por Wesley.",
    version="1.0.0",
    openapi_tags=[
        {"name": "Admin", "description": "Administrador de API"},
        {"name": "Usuarios", "description": "Gerenciamento de Usuarios"},
        {"name": "MateriaisAlmoxarifado", "description": "Gerenciamento de Materiais"},
        {"name": "Testes", "description": "Testando Rotas"},
    ]
)
# endregion

api_router = APIRouter()
api_router.include_router(users.router)
api_router.include_router(materials.router)

tenant_router = APIRouter(prefix="/t/{tenant}")
tenant_router.include_router(users.router)
tenant_router.include_router(materials.router)

admin_router = APIRouter()


@app.get("/")
def root(request: Request):
    return {"Host": request.headers["host"]}


@admin_router.get("/admin/me", response_model=UsuariosOut, tags=["Admin"])
def get_me(user: UsuariosOut = Depends(get_current_user)):
    return user


@admin_router.get("/admin/tests/role-test", tags=["Testes"], dependencies=[Depends(require_roles("admin"))])
def testing():
    return "Funcionando"


api_router.include_router(admin_router)
tenant_router.include_router(admin_router)
app.include_router(api_router)
app.include_router(tenant_router)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=5001, reload=True)
