from datetime import date
from typing import Union

from pydantic import BaseModel, EmailStr


# region Usuarios

class UsuariosIn(BaseModel):
    tenant_schema: Union[str, None] = None
    nome: str
    sobrenome: str
    email: EmailStr
    senha: str


class UsuariosOut(BaseModel):
    id: int
    tenant_schema: Union[str, None] = None
    nome: str
    sobrenome: str
    cargo: str
    email: EmailStr


class UsuariosInUpdate(BaseModel):
    id: int
    tenant_schema: Union[str, None] = None
    nome: Union[str, None] = None
    sobrenome: Union[str, None] = None
    cargo: Union[str, None] = None
    email: Union[EmailStr, None] = None
    senha: Union[str, None] = None


class UsuariosInLogin(BaseModel):
    email: EmailStr
    senha: str


class UsuariosWithToken(BaseModel):
    token: str
    cargo: Union[str, None] = None
    tenant_schema: Union[str, None] = None


# endregion

# region Colaboradores

class ColaboradoresIn(BaseModel):
    matricula: int
    nome: str
    funcao: str
    admissao: str


class ColaboradoresOut(ColaboradoresIn):
    id: int

    class Config:
        from_attributes = True


# endregion

# region Materiais

class MateriaisIn(BaseModel):
    codigo: str
    fornecedor: str
    nome: str
    tipo: str
    valor_unitario: int
    preco_total: int
    quantidade: int
    estoque: str


class MateriaisInUpdate(BaseModel):
    codigo: Union[str, None] = None
    fornecedor: Union[str, None] = None
    nome: Union[str, None] = None
    tipo: Union[str, None] = None


class MateriaisOutUpdate(MateriaisInUpdate):
    id: int

    class Config:
        from_attributes = True


class MateriaisOut(MateriaisIn):
    id: int

    class Config:
        from_attributes = True


# endregion

# region Historico de Entrada e Saida

class EntradaIn(BaseModel):
    data_entrada: Union[date, None] = None
    nome: str
    fornecedor: str
    quantidade: int
    valor_unitario: int
    preco_total: int


class EntradaOut(EntradaIn):
    id: int

    class Config:
        from_attributes = True


class SaidaIn(BaseModel):
    data_saida: Union[date, None] = None
    nome: str
    bloco: Union[str, None] = None
    quantidade: int
    preco_total: int


class SaidaOut(SaidaIn):
    id: int

    class Config:
        from_attributes = True

# endregion
