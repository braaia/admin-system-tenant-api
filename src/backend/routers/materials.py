from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.dependencies import get_db
from backend.models.models import Material, EntradaMaterial, SaidaMaterial
from backend.schemas import MateriaisIn, MateriaisOut, MateriaisInUpdate, EntradaOut, SaidaOut
from backend.services.materialService import MaterialService

router = APIRouter(prefix="/estoque-materiais")
roles = ["tech", "admin"]


@router.post("/cadastrar-material", response_model=MateriaisOut,
             tags=["Materiais"], name="Cadastrar um Material", status_code=201)
def cadastrar_material(material: MateriaisIn, db: Session = Depends(get_db)):
    return MaterialService.cadastrar_material(material, db)


@router.get("/listar-materiais", response_model=List[MateriaisOut],
            name="Listar Materiais", tags=["Materiais"])
def listar_materiais(db: Session = Depends(get_db)) -> list[type[Material]]:
    return db.query(Material).order_by(Material.id).all()


@router.put("/atualizar-material-id-{id_material}", response_model=MateriaisOut,
            tags=["Materiais"], name="Modificar um Material", status_code=200)
def atualizar_material(id_material: int, material: MateriaisInUpdate,
                       db: Session = Depends(get_db)) -> Material:
    material_alterado = MaterialService.atualizar_material(id_material, material, db)

    if not material_alterado:
        raise HTTPException(status_code=404, detail="Material não encontrado")

    return material_alterado


@router.delete("/deletar-material-id-{id_material}", tags=["Materiais"],
               name="Deletar um Material", status_code=204)
def deletar_material(id_material: int, db: Session = Depends(get_db)) -> None:
    sucesso = MaterialService.deletar_material(id_material, db)

    if not sucesso:
        raise HTTPException(status_code=404, detail="Material não encontrado")


@router.patch("/atualizar-{sub_or_sum}-quant-{quant}-material-id-{id_material}",
              response_model=MateriaisOut, tags=["Materiais"],
              name="Atualizar apenas a quantidade (estoque atualizado automaticamente)", status_code=200)
def atualizar_quantidade_material(id_material: int, sub_or_sum: int, quant: int, bloco: str = None,
                                  db: Session = Depends(get_db)) -> MateriaisOut:
    material_alterado = MaterialService.atualizar_quantidade(id_material, sub_or_sum, bloco, quant, db)

    if not material_alterado:
        raise HTTPException(status_code=404, detail="Material não encontrado")

    return material_alterado


@router.patch("/atualizar-valor-uni-para-{valor}-material-id-{id_material}",
              response_model=MateriaisOut, tags=["Materiais"],
              name="Atualizar apenas o valor unitario (preço total atualizado automaticamente)", status_code=200)
def atualizar_valor_unitario(id_material: int, valor: int, db: Session = Depends(get_db)) -> MateriaisOut:
    material_alterado = MaterialService.atualizar_valor(id_material, valor, db)

    if not material_alterado:
        raise HTTPException(status_code=404, detail="Material não encontrado")

    return material_alterado


@router.get("/listar-entrada", response_model=List[EntradaOut],
            name="Listar Entrada de Materiais", tags=["Materiais"])
def listar_entrada_almoxarifado(db: Session = Depends(get_db)) -> list[type[EntradaMaterial]]:
    return db.query(EntradaMaterial).order_by(EntradaMaterial.id).all()


@router.get("/listar-saida", response_model=List[SaidaOut],
            name="Listar Saida de Materiais", tags=["Materiais"])
def listar_entrada_almoxarifado(db: Session = Depends(get_db)) -> list[type[SaidaMaterial]]:
    return db.query(SaidaMaterial).order_by(SaidaMaterial.id).all()
