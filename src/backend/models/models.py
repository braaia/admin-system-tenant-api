from sqlalchemy import Column, Integer, String, VARCHAR, Date, func

from backend.database import Base


class Usuarios(Base):
    __tablename__ = "usuarios"
    __table_args__ = {"schema": "tenant"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    tenant_schema = Column(String(50))
    nome = Column(String(50), nullable=False)
    sobrenome = Column(String(100))
    cargo = Column(String(50), nullable=False, server_default="user")
    email = Column(String(70), nullable=False, unique=True)
    senha = Column(String(250), nullable=False)


class Material(Base):
    __tablename__ = "materiais"
    __table_args__ = {"schema": "tenant"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo = Column(VARCHAR(10), nullable=False, unique=True)
    fornecedor = Column(String(50), nullable=False)
    nome = Column(String(50), nullable=False, unique=True)
    tipo = Column(String(50), nullable=False)
    valor_unitario = Column(Integer, nullable=False)
    preco_total = Column(Integer, nullable=False)
    quantidade = Column(Integer, nullable=False)
    estoque = Column(String, nullable=False)


class EntradaMaterial(Base):
    __tablename__ = "entradas"
    __table_args__ = {"schema": "tenant"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    data_entrada = Column(Date(), server_default=func.now())
    nome = Column(String)
    fornecedor = Column(String)
    quantidade = Column(Integer, nullable=False)
    valor_unitario = Column(Integer, nullable=False)
    preco_total = Column(Integer)


class SaidaMaterial(Base):
    __tablename__ = "saidas"
    __table_args__ = {"schema": "tenant"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    data_saida = Column(Date(), server_default=func.now())
    nome = Column(String)
    bloco = Column(String)
    quantidade = Column(Integer, nullable=False)
    valor_unitario = Column(Integer, nullable=False)
    preco_total = Column(Integer)
