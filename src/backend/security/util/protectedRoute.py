from typing import Annotated, Union

from fastapi import Depends, Header, HTTPException, status
from sqlalchemy.orm import Session

from backend.dependencies import get_db
from backend.schemas import UsuariosOut
from backend.security.authHandler import AuthHandler
from backend.services.userService import UserService

AUTH_PREFIX = "Bearer "


def get_current_user(
        session: Session = Depends(get_db),
        authorization: Annotated[Union[str, None], Header()] = None
) -> UsuariosOut:
    auth_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciais de autenticação inválidas"
    )

    if not authorization:
        raise auth_exception

    if not authorization.startswith(AUTH_PREFIX):
        raise auth_exception

    payload = AuthHandler.decode_jwt(authorization[len(AUTH_PREFIX):])

    if payload and payload["user_id"]:
        try:
            user = UserService(session).get_user_by_id(payload["user_id"])
            return UsuariosOut(
                id=user.id,
                nome=user.nome,
                sobrenome=user.sobrenome,
                cargo=user.cargo,
                email=user.email
            )
        except Exception as error:
            raise error
    raise auth_exception


def require_roles(*allowed_roles: list):
    allowed = [r.lower() for r in allowed_roles]

    def dependency(current_user: UsuariosOut = Depends(get_current_user)) -> UsuariosOut:
        if not current_user or not getattr(current_user, "cargo", None):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Permissão negada")

        if current_user.cargo.lower() not in allowed:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Permissão negada")

        return current_user

    return dependency
