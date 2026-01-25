from fastapi import HTTPException
from sqlalchemy.orm import Session

from backend.repository.userRepo import UserRepository
from backend.schemas import UsuariosIn, UsuariosInLogin, UsuariosOut, UsuariosWithToken
from backend.security.authHandler import AuthHandler
from backend.security.hashHelper import HashHelper


class UserService:
    def __init__(self, session: Session):
        self.__userRepo = UserRepository(session)

    def signup(self, user_datails: UsuariosIn) -> UsuariosOut:
        if self.__userRepo.user_exists_by_email(user_datails.email):
            raise HTTPException(status_code=400, detail="Por favor faça login")

        hashed_password = HashHelper.get_password_hash(user_datails.senha)
        user_datails.senha = hashed_password
        return self.__userRepo.create_user(user_datails)

    def login(self, login_details: UsuariosInLogin) -> UsuariosWithToken:
        if not self.__userRepo.user_exists_by_email(login_details.email):
            raise HTTPException(status_code=400, detail="Por favor crie um conta")

        user = self.__userRepo.get_user_by_email(login_details.email)
        if HashHelper.verify_password(login_details.senha, user.senha):
            token = AuthHandler.sign_jwt(user.id, user.cargo)
            if token:
                return UsuariosWithToken(token=token, cargo=user.cargo, tenant_schema=user.tenant_schema)
            raise HTTPException(status_code=500, detail="Incapaz de processar a solicitação")
        raise HTTPException(status_code=400, detail="Por favor verifique suas credenciais")

    def get_user_by_id(self, user_id: int):
        user = self.__userRepo.get_user_by_id(user_id)

        if user:
            return user
        raise HTTPException(status_code=400, detail="Este usuário não está disponivel")
