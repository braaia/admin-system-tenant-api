import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from backend.database import Base


class Tenant(Base):
    __tablename__ = "tenants"
    __table_args__ = ({"schema": "shared"},)

    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(sa.String(256), nullable=False, unique=True, index=True)
    schema: Mapped[str] = mapped_column(sa.String(256), nullable=False, unique=True)
    host: Mapped[str] = mapped_column(sa.String(256), nullable=False, unique=True)
