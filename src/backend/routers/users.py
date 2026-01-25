from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.dependencies import get_db
from backend.schemas import UsuariosInLogin, UsuariosIn, UsuariosWithToken, UsuariosOut
from backend.services.userService import UserService

router = APIRouter(prefix="/auth-usuarios-adm")


@router.post("/login", response_model=UsuariosWithToken, tags=["Usuarios"], name="Se autenticar em uma Conta",
             status_code=200)
def login(loginDetails: UsuariosInLogin, db: Session = Depends(get_db)):
    try:
        return UserService(db).login(loginDetails)
    except Exception as error:
        print(error)
        raise error


@router.post("/sign-up", response_model=UsuariosOut, tags=["Usuarios"], name="Cadastrar uma Conta", status_code=201)
def registrar(registrarDetails: UsuariosIn, db: Session = Depends(get_db)):
    try:
        return UserService(db).signup(registrarDetails)
    except Exception as error:
        print(error)
        raise error
