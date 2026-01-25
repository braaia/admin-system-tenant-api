from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.dependencies import get_db
from backend.models.models import Material, EntradaMaterial, SaidaMaterial
from backend.schemas import MateriaisAlmoxarifadoIn, MateriaisAlmoxarifadoOut, MateriaisAlmoxarifadoInUpdate, EntradaAlmoxarifadoIn, EntradaAlmoxarifadoOut, SaidaAlmoxarifadoIn, SaidaAlmoxarifadoOut
from backend.services.materialService import MaterialService

router = APIRouter(prefix="/estoque-materiais")


@router.post("/cadastrar-material-almoxarifado", response_model=MateriaisAlmoxarifadoOut,
             tags=["MateriaisAlmoxarifado"], name="Cadastrar um Material na tabela do Almoxarifado", status_code=201)
def cadastrar_material_almoxarifado(material: MateriaisAlmoxarifadoIn, db: Session = Depends(get_db)):
    return MaterialService.cadastrar_material(material, db)


@router.get("/listar-materiais-almoxarifado", response_model=List[MateriaisAlmoxarifadoOut],
            name="Listar Materiais do Almoxarifado", tags=["MateriaisAlmoxarifado"])
def listar_materiais_almoxarifado(db: Session = Depends(get_db)) -> list[type[Material]]:
    return db.query(Material).order_by(Material.id).all()


@router.put("/atualizar-material-id-{id_material_almoxarifado}-almoxarifado", response_model=MateriaisAlmoxarifadoOut,
            tags=["MateriaisAlmoxarifado"], name="Modificar um Material da tabela do Almoxarifado", status_code=200)
def atualizar_material_almoxarifado(id_material_almoxarifado: int, material: MateriaisAlmoxarifadoInUpdate,
                                    db: Session = Depends(get_db)) -> MateriaisAlmoxarifadoOut:
    material_alterado = MaterialService.atualizar_material(id_material_almoxarifado, material, db)

    if not material_alterado:
        raise HTTPException(status_code=404, detail="Material não encontrado")

    return material_alterado


@router.delete("/deletar-material-id-{id_material_almoxarifado}-almoxarifado", tags=["MateriaisAlmoxarifado"],
               name="Deletar um Material da tabela do Almoxarifado", status_code=204)
def deletar_material_almoxarifado(id_material_almoxarifado: int, db: Session = Depends(get_db)) -> None:
    sucesso = MaterialService.deletar_material(id_material_almoxarifado, db)

    if not sucesso:
        raise HTTPException(status_code=404, detail="Material não encontrado")


@router.patch("/atualizar-{sub_or_sum}-quant-{quant}-material-id-{id_material}-almoxarifado",
              response_model=MateriaisAlmoxarifadoOut, tags=["MateriaisAlmoxarifado"],
              name="Atualizar apenas a quantidade (estoque atualizado automaticamente)", status_code=200)
def atualizar_quantidade_material(id_material: int, sub_or_sum: int, quant: int, bloco: str = None,
                                  db: Session = Depends(get_db)) -> MateriaisAlmoxarifadoOut:
    """
    Atualiza apenas a quantidade de um material.
    A coluna 'estoque' é atualizada automaticamente:
    - Se quantidade > 0: estoque = True
    - Se quantidade <= 0: estoque = False
    """
    material_alterado = MaterialService.atualizar_quantidade(id_material, sub_or_sum, bloco, quant, db)

    if not material_alterado:
        raise HTTPException(status_code=404, detail="Material não encontrado")

    return material_alterado


@router.patch("/atualizar-valor-uni-para-{valor}-material-id-{id_material}-almoxarifado",
              response_model=MateriaisAlmoxarifadoOut, tags=["MateriaisAlmoxarifado"],
              name="Atualizar apenas o valor unitario (preço total atualizado automaticamente)", status_code=200)
def atualizar_valor_unitario(id_material: int, valor: int, db: Session = Depends(get_db)) -> MateriaisAlmoxarifadoOut:
    """
    Atualiza apenas valor unitario de um material.
    A coluna 'preco_total' é atualizada automaticamente
    """
    material_alterado = MaterialService.atualizar_valor(id_material, valor, db)

    if not material_alterado:
        raise HTTPException(status_code=404, detail="Material não encontrado")

    return material_alterado


@router.get("/listar-entrada-almoxarifado", response_model=List[EntradaAlmoxarifadoOut],
            name="Listar Entrada de Materiais do Almoxarifado", tags=["MateriaisAlmoxarifado"])
def listar_entrada_almoxarifado(db: Session = Depends(get_db)) -> list[type[EntradaMaterial]]:
    return db.query(EntradaMaterial).order_by(EntradaMaterial.id).all()


@router.get("/listar-saida-almoxarifado", response_model=List[SaidaAlmoxarifadoOut],
            name="Listar Saida de Materiais do Almoxarifado", tags=["MateriaisAlmoxarifado"])
def listar_entrada_almoxarifado(db: Session = Depends(get_db)) -> list[type[SaidaMaterial]]:
    return db.query(SaidaMaterial).order_by(SaidaMaterial.id).all()




















