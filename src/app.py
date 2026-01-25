from fastapi import FastAPI, Depends, Request
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

app.include_router(users.router)
app.include_router(materials.router)


@app.get("/")
def root(request: Request):
    return {"Host": request.headers["host"]}


@app.get("/admin/me", response_model=UsuariosOut, tags=["Admin"])
def get_me(user: UsuariosOut = Depends(get_current_user)):
    return user


@app.get("/admin/tests/role-test", tags=["Testes"], dependencies=[Depends(require_roles("admin"))])
def testing():
    return "Funcionando"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=5001, reload=True)
