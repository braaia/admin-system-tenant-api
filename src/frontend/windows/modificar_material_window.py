from frontend.pages.ui_modmatwindow import Ui_ModMatWindow
from frontend.qt_core import *
from frontend.services.async_methods import AsyncMethods
from frontend.services.stock_service import EstoqueService


class ModificarMatWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.ui = Ui_ModMatWindow()
        self.ui.setupUi(self)

        self.ui.btn_modificar.clicked.connect(lambda: AsyncMethods.async_refresh_quant(self))

    async def refresh_quant(self):
        id_material = self.ui.txt_material_id.text()
        if self.ui.cbox_012.currentText() == "Adicionar material":
            sub_or_sum = 1
        elif self.ui.cbox_012.currentText() == "Retirar material":
            sub_or_sum = 2
        else:
            sub_or_sum = 0
        quantidade = self.ui.txt_nova_quantidade.text()
        bloco = self.ui.txt_bloco.text()

        try:
            result = await EstoqueService.atualizar_quantidade(self.main_window.current_tenant, id_material, sub_or_sum, quantidade, bloco)
            print(result)
        except Exception as e:
            print(f"Erro ao atualizar quantidade: {e}")
