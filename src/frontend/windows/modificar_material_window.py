from frontend.pages.ui_modmatwindow import Ui_ModMatWindow
from frontend.qt_core import *
from frontend.services.async_methods import AsyncMethods
from frontend.services.stock_service import EstoqueService


class ModificarMatWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.setWindowTitle("Atualizar Materiais")
        self.main_window = main_window
        self.setAttribute(Qt.WA_DeleteOnClose, True)
        self.ui = Ui_ModMatWindow()
        self.ui.setupUi(self)

        self.ui.btn_modificar.clicked.connect(lambda: AsyncMethods.async_refresh_quant(self))

    async def refresh_quant(self):
        id_material = self.ui.txt_material_id.text()
        if self.ui.cbox_012.currentText() == "Adicionar material":
            sub_or_sum = 2
        elif self.ui.cbox_012.currentText() == "Retirar material":
            sub_or_sum = 1
        else:
            sub_or_sum = 0
        quantidade = self.ui.txt_nova_quantidade.text()
        bloco = self.ui.txt_bloco.text() or None

        try:
            await EstoqueService.atualizar_quantidade(self.main_window.current_tenant, id_material, sub_or_sum, quantidade, bloco)
            self.main_window.lineedit_clear(self.ui.txt_material_id, "")
            self.main_window.lineedit_clear(self.ui.txt_nova_quantidade, "")
            self.main_window.lineedit_clear(self.ui.txt_bloco, "")

            estoque = await EstoqueService.listar_materiais(self.main_window.current_tenant)
            self.main_window.populate_get_materials(estoque)
            self.main_window.get_materials_count(estoque)
            entrada = await EstoqueService.listar_entradas(self.main_window.current_tenant)
            saida = await EstoqueService.listar_saidas(self.main_window.current_tenant)
            self.main_window.populate_get_ent_sai(entrada, saida)
            self.main_window.get_ent_sai_count(estoque, entrada, saida)

            self.main_window.material_refreshed()
            self.close()
        except Exception as e:
            self.main_window.material_refresh_error()
            print(f"Erro ao atualizar quantidade: {e}")










