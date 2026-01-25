from backend.models.models import Usuarios
from backend.schemas import UsuariosIn
from .base import BaseRepository


class UserRepository(BaseRepository):
    def create_user(self, user_data: UsuariosIn):
        newUser = Usuarios(**user_data.model_dump(exclude_none=True))
        newUser.cargo = "user"

        self.session.add(newUser)
        self.session.commit()
        self.session.refresh(newUser)

        return newUser

    def user_exists_by_email(self, email: str) -> bool:
        user = self.session.query(Usuarios).filter_by(email=email).first()
        return bool(user)

    def get_user_by_email(self, email: str) -> Usuarios:
        user = self.session.query(Usuarios).filter_by(email=email).first()
        return user

    def get_user_by_id(self, id: int) -> Usuarios:
        user = self.session.query(Usuarios).filter_by(id=id).first()
        return user
