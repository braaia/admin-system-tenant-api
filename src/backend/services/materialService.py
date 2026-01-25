from sqlalchemy.orm import Session

from backend.models.models import Material, EntradaMaterial, SaidaMaterial
from backend.schemas import MateriaisAlmoxarifadoIn, MateriaisAlmoxarifadoInUpdate, MateriaisAlmoxarifadoOut


class MaterialService:
    """Serviço para gerenciar materiais e estoque automaticamente"""

    @staticmethod
    def verificar_e_atualizar_estoque(material: Material) -> None:
        """
        Verifica a quantidade e atualiza automaticamente o status do estoque.
        Se quantidade <= 0, estoque = False
        Se quantidade > 0, estoque = True
        """
        material.estoque = "Disponivel" if material.quantidade >= 50 else "Abaixo do minimo" if material.quantidade > 0 else "Em falta"

    @staticmethod
    def verificar_e_atualizar_preco(material: Material) -> None:
        material.preco_total = material.valor_unitario * material.quantidade

    @staticmethod
    def verificar_e_atualizar_preco_entrada(entrada_material: EntradaMaterial) -> None:
        entrada_material.preco_total = entrada_material.valor_unitario * entrada_material.quantidade

    @staticmethod
    def cadastrar_material(material_dados: MateriaisAlmoxarifadoIn, db: Session) -> Material:
        """Cria um novo material e atualiza o estoque automaticamente"""
        novo_material = Material(
            **material_dados.model_dump(exclude_none=True)
        )

        # Verifica e atualiza o estoque automaticamente
        MaterialService.verificar_e_atualizar_estoque(novo_material)
        MaterialService.verificar_e_atualizar_preco(novo_material)

        entrada_material = EntradaMaterial(
            nome=material_dados.nome,
            fornecedor=material_dados.fornecedor,
            quantidade=material_dados.quantidade,
            valor_unitario=material_dados.valor_unitario,
            preco_total=material_dados.valor_unitario * material_dados.quantidade
        )

        db.add(novo_material)
        db.add(entrada_material)
        db.commit()
        db.refresh(novo_material)
        db.refresh(entrada_material)

        return novo_material

    @staticmethod
    def atualizar_material(id_material: int, material_dados: MateriaisAlmoxarifadoInUpdate,
                           db: Session) -> Material | None:
        """Atualiza um material e recalcula o estoque automaticamente"""
        material_alterado: Material = db.get(Material, id_material)
        entrada_alterada: EntradaMaterial = db.get(EntradaMaterial, id_material)

        if not material_alterado:
            return None
        if not entrada_alterada:
            return None

        # Atualiza apenas campos enviados
        if material_dados.codigo is not None:
            material_alterado.codigo = material_dados.codigo
        if material_dados.nome is not None:
            material_alterado.nome = material_dados.nome
        if material_dados.fornecedor is not None:
            material_alterado.fornecedor = material_dados.fornecedor
        if material_dados.tipo is not None:
            material_alterado.tipo = material_dados.tipo

        MaterialService.verificar_e_atualizar_estoque(material_alterado)

        if material_dados.nome is not None:
            entrada_alterada.nome = material_dados.nome
        if material_dados.fornecedor is not None:
            entrada_alterada.fornecedor = material_dados.fornecedor

        db.add(material_alterado)
        db.add(entrada_alterada)
        db.commit()
        db.refresh(material_alterado)
        db.refresh(entrada_alterada)

        return material_alterado

    @staticmethod
    def deletar_material(id_material: int, db: Session) -> bool:
        """Deleta um material"""
        material_deletado = db.get(Material, id_material)

        if not material_deletado:
            return False

        db.delete(material_deletado)
        db.commit()
        return True

    @staticmethod
    def atualizar_quantidade(id_material: int, sub_or_sum: int, bloco: str, nova_quantidade: int,
                             db: Session) -> MateriaisAlmoxarifadoOut | None:
        """
        Atualiza apenas a quantidade de um material e recalcula o estoque.
        Útil para saídas/entradas rápidas de estoque.
        """
        material = db.get(Material, id_material)

        if not material:
            return None

        # sub_or_sum: 0 = set, 1 = subtract, 2 = add
        if sub_or_sum == 0:
            material.quantidade = nova_quantidade
        elif sub_or_sum == 1:
            if material.quantidade - nova_quantidade < 0:
                raise ValueError("Operação resultaria em quantidade negativa")
            material.quantidade = material.quantidade - nova_quantidade
            saida = SaidaMaterial(
                nome=material.nome,
                bloco=bloco,
                quantidade=nova_quantidade,
                valor_unitario=material.valor_unitario,
                preco_total=material.valor_unitario * nova_quantidade,
            )
            db.add(saida)
        elif sub_or_sum == 2:
            material.quantidade = material.quantidade + nova_quantidade
            entrada = EntradaMaterial(
                nome=material.nome,
                fornecedor=material.fornecedor,
                quantidade=nova_quantidade,
                valor_unitario=material.valor_unitario,
                preco_total=material.valor_unitario * nova_quantidade,
            )
            db.add(entrada)

        MaterialService.verificar_e_atualizar_estoque(material)
        MaterialService.verificar_e_atualizar_preco(material)

        db.add(material)
        db.commit()
        db.refresh(material)

        return material

    @staticmethod
    def atualizar_valor(id_material: int, novo_valor: int, db: Session) -> MateriaisAlmoxarifadoOut | None:
        """
        Atualiza apenas valor de um material e recalcula o preço total.
        Útil para saídas/entradas rápidas de estoque.
        """
        material = db.get(Material, id_material)

        if not material:
            return None

        material.valor_unitario = novo_valor

        MaterialService.verificar_e_atualizar_preco(material)

        db.add(material)
        db.commit()
        db.refresh(material)

        return material
