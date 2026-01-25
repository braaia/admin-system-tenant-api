from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.dependencies import get_db, get_tenant
from backend.models.tenant import Tenant
from backend.schemas import UsuariosInLogin, UsuariosIn, UsuariosWithToken, UsuariosOut
from backend.services.userService import UserService

router = APIRouter(prefix="/auth-usuarios-adm")


@router.post("/login", response_model=UsuariosWithToken, tags=["Usuarios"], name="Se autenticar em uma Conta",
             status_code=200)
def login(
    loginDetails: UsuariosInLogin,
    db: Session = Depends(get_db),
    tenant: Tenant = Depends(get_tenant),
):
    try:
        token_data = UserService(db).login(loginDetails)
        if not token_data.tenant_schema:
            token_data.tenant_schema = tenant.schema
        return token_data
    except Exception as error:
        print(error)
        raise error


@router.post("/sign-up", response_model=UsuariosOut, tags=["Usuarios"], name="Cadastrar uma Conta", status_code=201)
def registrar(
    registrarDetails: UsuariosIn,
    db: Session = Depends(get_db),
    tenant: Tenant = Depends(get_tenant),
):
    try:
        if not registrarDetails.tenant_schema:
            registrarDetails.tenant_schema = tenant.schema
        return UserService(db).signup(registrarDetails)
    except Exception as error:
        print(error)
        raise error
