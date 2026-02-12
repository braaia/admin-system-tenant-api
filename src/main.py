import sys

from backend.db_init import create_tenant
from frontend.services.api_client import ApiClient
from frontend.services.async_methods import AsyncMethods
from frontend.services.stock_service import EstoqueService
from frontend.qt_core import *
from frontend.windows.main_window.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.current_tenant = "usuarios"

        # TITLE
        self.setWindowTitle("Sistema de Estoque")

        # SETUP MAIN WINDOW
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # region LOGIN FUNCTIONS
        self.ui.ui_pages.btn_register.clicked.connect(self.show_register_page)

        self.ui.ui_pages.username_login_label.setText("")
        self.ui.ui_pages.password_login_label.setText("")

        self.ui.ui_pages.txt_login_username.setPlaceholderText("Email")
        self.ui.ui_pages.txt_login_password.setPlaceholderText("Senha")

        self.ui.ui_pages.txt_login_username.setClearButtonEnabled(True)
        self.ui.ui_pages.txt_login_password.setClearButtonEnabled(True)

        self.ui.ui_pages.txt_login_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.ui.ui_pages.txt_login_username.textChanged.connect(self.do_username_login_label)
        self.ui.ui_pages.txt_login_password.textChanged.connect(self.do_password_login_label)

        self.ui.ui_pages.btn_login.clicked.connect(lambda: AsyncMethods.async_login_account(self))
        # endregion

        # region REGISTER FUNCTIONS
        self.ui.ui_pages.username_reg_label.setText("")
        self.ui.ui_pages.lastname_reg_label.setText("")
        self.ui.ui_pages.email_reg_label.setText("")
        self.ui.ui_pages.password_reg_label.setText("")

        self.ui.ui_pages.txt_reg_username.setPlaceholderText("Usuário")
        self.ui.ui_pages.txt_reg_lastname.setPlaceholderText("Sobrenome")
        self.ui.ui_pages.txt_reg_email.setPlaceholderText("Email")
        self.ui.ui_pages.txt_reg_password.setPlaceholderText("Senha")

        self.ui.ui_pages.txt_reg_username.setClearButtonEnabled(True)
        self.ui.ui_pages.txt_reg_lastname.setClearButtonEnabled(True)
        self.ui.ui_pages.txt_reg_email.setClearButtonEnabled(True)
        self.ui.ui_pages.txt_reg_password.setClearButtonEnabled(True)

        self.ui.ui_pages.txt_reg_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.ui.ui_pages.txt_reg_username.textChanged.connect(self.do_username_reg_label)
        self.ui.ui_pages.txt_reg_lastname.textChanged.connect(self.do_lastname_reg_label)
        self.ui.ui_pages.txt_reg_email.textChanged.connect(self.do_email_reg_label)
        self.ui.ui_pages.txt_reg_password.textChanged.connect(self.do_password_reg_label)

        self.ui.ui_pages.btn_register_acc.clicked.connect(lambda: AsyncMethods.async_reg_account(self))
        # endregion

        # region FUNCTIONS
        # TOGGLE MENU
        self.ui.toggle_menu.clicked.connect(self.toggle_menu)

        # TABLE WIDGET FILTER
        self.ui.ui_pages.txt_filtrar_mat_estoque.textChanged.connect(lambda: self.apply_filter_stock())
        self.ui.ui_pages.cbox_filtrar_status.currentTextChanged.connect(lambda: self.apply_filter_stock())

        self.ui.ui_pages.txt_filtrar_mat_ent_sai.textChanged.connect(lambda: self.apply_filter_ent_sai())
        self.ui.ui_pages.cbox_filtrar_mes.currentTextChanged.connect(lambda: self.apply_filter_ent_sai())
        # TABLE ADJUST
        self.ui.ui_pages.stock_table_widget.setColumnWidth(0, 80)
        self.ui.ui_pages.stock_table_widget.setColumnWidth(1, 165)
        self.ui.ui_pages.stock_table_widget.setColumnWidth(2, 155)
        self.ui.ui_pages.stock_table_widget.setColumnWidth(3, 130)
        self.ui.ui_pages.stock_table_widget.setColumnWidth(4, 100)
        self.ui.ui_pages.stock_table_widget.setColumnWidth(5, 90)
        self.ui.ui_pages.stock_table_widget.setColumnWidth(6, 90)
        self.ui.ui_pages.stock_table_widget.setColumnWidth(7, 145)

        self.ui.ui_pages.ent_table_widget.setColumnWidth(0, 90)
        self.ui.ui_pages.ent_table_widget.setColumnWidth(1, 140)
        self.ui.ui_pages.ent_table_widget.setColumnWidth(2, 130)
        self.ui.ui_pages.ent_table_widget.setColumnWidth(3, 90)
        self.ui.ui_pages.ent_table_widget.setColumnWidth(4, 90)
        self.ui.ui_pages.ent_table_widget.setColumnWidth(5, 90)

        self.ui.ui_pages.saida_table_widget.setColumnWidth(0, 90)
        self.ui.ui_pages.saida_table_widget.setColumnWidth(1, 140)
        self.ui.ui_pages.saida_table_widget.setColumnWidth(2, 100)
        self.ui.ui_pages.saida_table_widget.setColumnWidth(3, 90)
        self.ui.ui_pages.saida_table_widget.setColumnWidth(4, 90)
        self.ui.ui_pages.saida_table_widget.setColumnWidth(5, 90)
        # endregion

        # region CONNECT PAGE BUTTONS
        self.ui.btn_materiais.clicked.connect(self.show_materials_page)
        self.ui.btn_estoque.clicked.connect(self.show_stock_page)
        self.ui.btn_settings.clicked.connect(self.show_settings_page)
        self.ui.btn_admin.clicked.connect(self.show_admin_page)
        # endregion

        # region CONNECT FUNCTION BUTTONS
        # GET MATERIALS
        self.ui.ui_pages.btn_atualizar_lista_estoque.clicked.connect(lambda: AsyncMethods.async_get_materials(self))
        self.ui.ui_pages.btn_atualizar_lista_estoque.clicked.connect(self.requisition)

        self.ui.ui_pages.btn_atualizar_lista_materiais.clicked.connect(lambda: AsyncMethods.async_get_materials(self))
        self.ui.ui_pages.btn_atualizar_lista_materiais.clicked.connect(self.requisition)

        # POST MATERIAL
        self.ui.ui_pages.btn_cadastrar_mat.clicked.connect(lambda: AsyncMethods.async_post_materials(self))

        # CREATE TENANT
        self.ui.ui_pages.btn_create_tenant.clicked.connect(self.func_create_tenant)
        # endregion

        # DISPLAY THE APP
        self.show()

    # region GET ME
    async def get_me(self):
        try:
            result = await ApiClient.get("usuarios", "/admin/me")

            nome = result["nome"]
            sobrenome = result["sobrenome"]

            self.ui.top_right_label.setText(f"{nome} {sobrenome}")

            self.ui.btn_admin.setVisible(True) if result["cargo"] == "tech" else self.ui.btn_admin.setVisible(False)


        except Exception as e:
            print(f"Erro ao obter dados do usuário: {e}")

    # endregion

    # region PAGE BUTTONS
    def show_login_page(self):
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.login_page)

    def show_register_page(self):
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.register_page)

    def show_materials_page(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.materials_page)
        self.ui.btn_materiais.set_active(True)

    def show_stock_page(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.stock_page)
        self.ui.btn_estoque.set_active(True)

    def show_settings_page(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.settings_page)
        self.ui.btn_settings.set_active(True)

    def show_admin_page(self):
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.admin_page)
        self.ui.btn_admin.set_active(True)

    # endregion

    # region CLEAR ANIMATION
    def lineedit_clear(self, line_edit, new_text=""):
        # guarda refs por widget pra não morrer/ser sobrescrita
        if not hasattr(self, "_clear_anims"):
            self._clear_anims = {}

        # efeito (um por widget)
        effect = line_edit.graphicsEffect()
        if not isinstance(effect, QGraphicsOpacityEffect):
            effect = QGraphicsOpacityEffect(line_edit)
            line_edit.setGraphicsEffect(effect)

        fade_out = QPropertyAnimation(effect, b"opacity", line_edit)
        fade_out.setDuration(120)
        fade_out.setStartValue(1.0)
        fade_out.setEndValue(0.0)

        fade_in = QPropertyAnimation(effect, b"opacity", line_edit)
        fade_in.setDuration(120)
        fade_in.setStartValue(0.0)
        fade_in.setEndValue(1.0)

        group = QSequentialAnimationGroup(line_edit)
        group.addAnimation(fade_out)
        group.addAnimation(fade_in)

        def swap_text():
            line_edit.setText(new_text)

        fade_out.finished.connect(swap_text)

        def cleanup():
            # opcional: remover efeito ao final
            line_edit.setGraphicsEffect(None)
            self._clear_anims.pop(line_edit, None)

        group.finished.connect(cleanup)

        self._clear_anims[line_edit] = group
        group.start()

    # endregion

    # region GET REQUEST FUNCTIONS
    def _populate_get_materials(self, materials):
        page = self.ui.ui_pages.stock_table_widget
        page.clearContents()
        page.setRowCount(len(materials))

        # Ordem das colunas conforme o schema MateriaisAlmoxarifadoOut
        columns = ["codigo", "nome", "fornecedor", "tipo", "valor_unitario", "preco_total", "quantidade", "estoque"]

        for row, material in enumerate(materials):
            if isinstance(material, dict):
                for column, field in enumerate(columns):
                    value = material.get(field, "")
                    page.setItem(row, column, QTableWidgetItem(str(value)))

    def _populate_get_ent_sai(self, entradas, saidas):
        page_ent = self.ui.ui_pages.ent_table_widget
        page_ent.clearContents()
        page_ent.setRowCount(len(entradas))

        page_saida = self.ui.ui_pages.saida_table_widget
        page_saida.clearContents()
        page_saida.setRowCount(len(saidas))

        columns_ent = ["data_entrada", "nome", "fornecedor", "quantidade", "valor_unitario", "preco_total"]
        columns_saida = ["data_saida", "nome", "bloco", "quantidade", "valor_unitario", "preco_total"]

        for row_ent, entrada in enumerate(entradas):
            if isinstance(entrada, dict):
                for column_ent, field_ent in enumerate(columns_ent):
                    value_ent = entrada.get(field_ent, "")
                    page_ent.setItem(row_ent, column_ent, QTableWidgetItem(str(value_ent)))

        for row_saida, saida in enumerate(saidas):
            if isinstance(saida, dict):
                for column_saida, field_saida in enumerate(columns_saida):
                    value_saida = saida.get(field_saida, "")
                    page_saida.setItem(row_saida, column_saida, QTableWidgetItem(str(value_saida)))

    def get_materials_count(self, materials):
        prod_totais = self.ui.ui_pages.prod_totais_label
        em_estoque = self.ui.ui_pages.emestoque_label
        em_falta = self.ui.ui_pages.emfalta_label
        minimo = self.ui.ui_pages.abaixodomin_label

        prod_totais.setAlignment(Qt.AlignCenter)
        prod_totais.setMinimumWidth(228)
        prod_totais.setMinimumHeight(40)
        prod_totais.setStyleSheet("font: 700 18pt; color: black;")

        em_estoque.setAlignment(Qt.AlignCenter)
        em_estoque.setMinimumWidth(228)
        em_estoque.setMinimumHeight(40)
        em_estoque.setStyleSheet("font: 700 18pt; color: black;")

        em_falta.setAlignment(Qt.AlignCenter)
        em_falta.setMinimumWidth(228)
        em_falta.setMinimumHeight(40)
        em_falta.setStyleSheet("font: 700 18pt; color: black;")

        minimo.setAlignment(Qt.AlignCenter)
        minimo.setMinimumWidth(228)
        minimo.setMinimumHeight(40)
        minimo.setStyleSheet("font: 700 18pt; color: black;")

        qnt_prod_totais = 0
        qnt_em_estoque = 0
        qnt_em_falta = 0
        qnt_minimo = 0

        for material in materials:
            qnt_prod_totais += 1
            estoque_status = material.get("estoque", "")
            if estoque_status == "Disponivel":
                qnt_em_estoque += 1
            elif estoque_status == "Em falta":
                qnt_em_falta += 1
            elif estoque_status == "Abaixo do minimo":
                qnt_minimo += 1

        prod_totais.setText(str(qnt_prod_totais))
        em_estoque.setText(str(qnt_em_estoque))
        em_falta.setText(str(qnt_em_falta))
        minimo.setText(str(qnt_minimo))

    def get_ent_sai_count(self, materiais, entradas, saidas):
        entrada = self.ui.ui_pages.entrada_label
        saida = self.ui.ui_pages.saida_label
        saldo_atual = self.ui.ui_pages.saldo_atual_label

        entrada.setAlignment(Qt.AlignCenter)
        entrada.setMinimumWidth(228)
        entrada.setMinimumHeight(40)
        entrada.setStyleSheet("font: 700 18pt; color: black;")

        saida.setAlignment(Qt.AlignCenter)
        saida.setMinimumWidth(228)
        saida.setMinimumHeight(40)
        saida.setStyleSheet("font: 700 18pt; color: black;")

        saldo_atual.setAlignment(Qt.AlignCenter)
        saldo_atual.setMinimumWidth(228)
        saldo_atual.setMinimumHeight(40)
        saldo_atual.setStyleSheet("font: 700 18pt; color: black;")

        qnt_entrada = 0
        qnt_saida = 0
        qnt_saldo_atual = 0

        for _ in entradas:
            qnt_entrada += 1

        for _ in saidas:
            qnt_saida += 1

        for _ in materiais:
            qnt_saldo_atual += 1

        if qnt_entrada == 0:
            entrada.setText(f"{str(qnt_entrada)}")
        else:
            entrada.setText(f"+{str(qnt_entrada)}")
        if qnt_saida == 0:
            saida.setText(f"{str(qnt_saida)}")
        else:
            saida.setText(f"-{str(qnt_saida)}")

        saldo_atual.setText(str(qnt_saldo_atual))

    async def get_materials(self):
        try:
            estoque = await EstoqueService.listar_materiais(self.current_tenant)
            self._populate_get_materials(estoque)
            self.get_materials_count(estoque)
            entrada = await EstoqueService.listar_entradas(self.current_tenant)
            saida = await EstoqueService.listar_saidas(self.current_tenant)
            self._populate_get_ent_sai(entrada, saida)
            self.get_ent_sai_count(estoque, entrada, saida)
        except Exception as e:
            self.requisition_error()
            print(f"Erro na requisição: {e}")

    # endregion

    # region POST REQUEST FUNCTION
    async def post_material(self):
        data = {
            "codigo": self.ui.ui_pages.txt_codigo.text(),
            "fornecedor": self.ui.ui_pages.txt_fornecedor.text(),
            "nome": self.ui.ui_pages.txt_nome.text(),
            "tipo": self.ui.ui_pages.txt_categoria.text(),
            "valor_unitario": self.ui.ui_pages.txt_valor_uni.text(),
            "preco_total": 0,
            "quantidade": self.ui.ui_pages.txt_quant.text(),
            "estoque": "string"
        }
        try:
            await EstoqueService.cadastrar_material(self.current_tenant, data)
            self.lineedit_clear(self.ui.ui_pages.txt_codigo, ""),
            self.lineedit_clear(self.ui.ui_pages.txt_fornecedor, ""),
            self.lineedit_clear(self.ui.ui_pages.txt_nome, ""),
            self.lineedit_clear(self.ui.ui_pages.txt_categoria, ""),
            self.lineedit_clear(self.ui.ui_pages.txt_valor_uni, ""),
            self.lineedit_clear(self.ui.ui_pages.txt_quant, ""),
            self.material_created()
        except Exception as e:
            self.material_created_error()
            print(e)

    # endregion

    # region LOGIN POST REQUEST
    async def login_token(self):
        data = {
            "email": self.ui.ui_pages.txt_login_username.text(),
            "senha": self.ui.ui_pages.txt_login_password.text()
        }
        try:
            token = await EstoqueService.login_account(data)
            ApiClient.set_token(token)
            tenant_schema = token.get("tenant_schema")
            self.current_tenant = tenant_schema
            ApiClient.set_tenant(tenant_schema)
            print(tenant_schema)

            role = ApiClient.get_role()

            if role != "user":
                self.check_token()

                self.ui.pages.setCurrentWidget(self.ui.ui_pages.materials_page)

                await self.get_me()
            else:
                self.ui.pages.setCurrentWidget(self.ui.ui_pages.sobre_page)
        except Exception as e:
            self.requisition_error()
            print(e)

    # endregion

    # region REGISTER POST REQUEST
    async def register_account(self):
        data = {
            "nome": self.ui.ui_pages.txt_reg_username.text(),
            "sobrenome": self.ui.ui_pages.txt_reg_lastname.text(),
            "email": self.ui.ui_pages.txt_reg_email.text(),
            "senha": self.ui.ui_pages.txt_reg_password.text()
        }
        try:
            await EstoqueService.register_account(data)

            self.ui.pages.setCurrentWidget(self.ui.ui_pages.login_page)
        except Exception as e:
            self.requisition_error()
            print(e)

    # endregion

    # region FUNCTIONS
    def func_create_tenant(self):
        name = self.ui.ui_pages.txt_tnt_name.text()
        schema = self.ui.ui_pages.txt_schema_name.text()
        host = self.ui.ui_pages.txt_host_name.text()

        create_tenant(name, schema, host)

    def reset_selection(self):
        for btn in self.ui.left_menu.findChildren(QPushButton):
            try:
                btn.set_active(False)
            except:
                print("erro no reset_selection")
                raise

    def check_token(self):
        token = ApiClient.get_token()
        role = ApiClient.get_role()

        if not token or role == "user":
            self.ui.left_menu.setVisible(False)
            self.ui.top_bar.setVisible(False)
        else:
            self.ui.left_menu.setVisible(True)
            self.ui.top_bar.setVisible(True)

    def apply_filter_stock(self):
        search_text = self.ui.ui_pages.txt_filtrar_mat_estoque.text().strip().lower()
        status = self.ui.ui_pages.cbox_filtrar_status.currentText()

        for r in range(self.ui.ui_pages.stock_table_widget.rowCount()):
            stt = self.ui.ui_pages.stock_table_widget.item(r, 7).text()  # coluna estoque

            # Verifica se o texto de busca está presente em alguma coluna
            match_text = not search_text
            if search_text:
                for c in range(self.ui.ui_pages.stock_table_widget.columnCount()):
                    item = self.ui.ui_pages.stock_table_widget.item(r, c)
                    if item and search_text in item.text().lower():
                        match_text = True
                        break

            match_stt = (status == "Todos") or (stt == status)

            show = match_text and match_stt
            self.ui.ui_pages.stock_table_widget.setRowHidden(r, not show)

    def _extract_month_from_text(self, date_text):
        if not date_text:
            return None

        date_text = date_text.strip()

        if len(date_text) >= 7 and date_text[4] == "-" and date_text[5:7].isdigit():
            return int(date_text[5:7])

        date_part = date_text.split(" ", 1)[0]
        parts = date_part.split("-")
        if len(parts) >= 2 and parts[1].isdigit():
            return int(parts[1])

        return None

    def apply_filter_ent_sai(self):
        search_text = self.ui.ui_pages.txt_filtrar_mat_ent_sai.text().strip().lower()
        month_index = self.ui.ui_pages.cbox_filtrar_mes.currentIndex()
        month_filter = month_index if month_index > 0 else None

        ent_table = self.ui.ui_pages.ent_table_widget
        saida_table = self.ui.ui_pages.saida_table_widget

        for e in range(ent_table.rowCount()):
            # Verifica se o texto de busca esta presente em alguma coluna
            match_text_ent = not search_text
            if search_text:
                for c in range(ent_table.columnCount()):
                    entrada = ent_table.item(e, c)
                    if entrada and search_text in entrada.text().lower():
                        match_text_ent = True
                        break

            match_month_ent = True
            if month_filter:
                date_item = ent_table.item(e, 0)
                month_value = self._extract_month_from_text(date_item.text() if date_item else "")
                match_month_ent = (month_value == month_filter)

            show_ent = match_text_ent and match_month_ent
            ent_table.setRowHidden(e, not show_ent)

        for s in range(saida_table.rowCount()):
            # Verifica se o texto de busca esta presente em alguma coluna
            match_text_sai = not search_text
            if search_text:
                for d in range(saida_table.columnCount()):
                    saida = saida_table.item(s, d)
                    if saida and search_text in saida.text().lower():
                        match_text_sai = True
                        break

            match_month_sai = True
            if month_filter:
                date_item = saida_table.item(s, 0)
                month_value = self._extract_month_from_text(date_item.text() if date_item else "")
                match_month_sai = (month_value == month_filter)

            show_saida = match_text_sai and match_month_sai
            saida_table.setRowHidden(s, not show_saida)

    # region MATERIALS ALERT
    def material_created(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Alerta!")
        dlg.setText("✅ Material criado com sucesso!")
        dlg.setStyleSheet(
            "QMessageBox { background-color: #f0f0f0; border: 1px solid black; }"
            "QLabel { color: black; font-size: 16px; }"
            "QPushButton { background-color: #4CAF50; font: 700 12px; color: black; padding: 5px 25px; border: 1px solid black; border-radius: 6px; }"
            "QPushButton:hover { background-color: #45a049; }"
        )
        dlg.setContentsMargins(0, 0, 30, 0)
        dlg.setIcon(QMessageBox.Information)
        dlg.setWindowIcon(QIcon(":/icons/icons/icon_orange_warning.png"))
        dlg.exec()

    def material_created_error(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Alerta!")
        dlg.setText("❌ Erro - Por favor complete os campos de texto!")
        dlg.setStyleSheet(
            "QMessageBox { background-color: #f0f0f0; border: 1px solid black; }"
            "QLabel { color: black; font-size: 16px; }"
            "QPushButton { background-color: #DC3545; font: 700 12px; color: black; padding: 5px 25px; border: 1px solid black; border-radius: 6px; }"
            "QPushButton:hover { background-color: #9A2530; }"
        )
        dlg.setContentsMargins(0, 0, 30, 0)
        dlg.setIcon(QMessageBox.Warning)
        dlg.setWindowIcon(QIcon(":/icons/icons/icon_orange_warning.png"))
        dlg.exec()

    # endregion

    # region REQUISITIONS ALERT
    def requisition(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Alerta!")
        dlg.setText("✅ Lista atualizada com sucesso!")
        dlg.setStyleSheet(
            "QMessageBox { background-color: #f0f0f0; border: 1px solid black; }"
            "QLabel { color: black; font-size: 16px; }"
            "QPushButton { background-color: #4CAF50; font: 700 12px; color: black; padding: 5px 25px; border: 1px solid black; border-radius: 6px; }"
            "QPushButton:hover { background-color: #45a049; }"
        )
        dlg.setContentsMargins(0, 0, 30, 0)
        dlg.setIcon(QMessageBox.Information)
        dlg.setWindowIcon(QIcon(":/icons/icons/icon_orange_warning.png"))
        dlg.exec()

    def requisition_error(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Alerta!")
        dlg.setText("❌ Erro na requisição!")
        dlg.setStyleSheet(
            "QMessageBox { background-color: #f0f0f0; border: 1px solid black; }"
            "QLabel { color: black; font-size: 16px; }"
            "QPushButton { background-color: #DC3545; font: 700 12px; color: black; padding: 5px 25px; border: 1px solid black; border-radius: 6px; }"
            "QPushButton:hover { background-color: #9A2530; }"
        )
        dlg.setContentsMargins(0, 0, 30, 0)
        dlg.setIcon(QMessageBox.Critical)
        dlg.setWindowIcon(QIcon(":/icons/icons/icon_red_warning.png"))
        dlg.exec()

    # endregion

    def toggle_menu(self):
        menu_width = self.ui.left_menu.width()
        width = 50

        if menu_width == 50:
            width = 240

        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)
        self.animation.start()

    # endregion

    # region LOGIN & REGISTER FUNCTIONS
    # LOGIN
    def do_username_login_label(self, text):
        if text:
            self.ui.ui_pages.username_login_label.setText("Email")
        else:
            self.ui.ui_pages.username_login_label.setText("")

    def do_password_login_label(self, text):
        if text:
            self.ui.ui_pages.password_login_label.setText("Senha")
        else:
            self.ui.ui_pages.password_login_label.setText("")

    # REGISTER
    def do_username_reg_label(self, text):
        if text:
            self.ui.ui_pages.username_reg_label.setText("Nome")
        else:
            self.ui.ui_pages.username_reg_label.setText("")

    def do_lastname_reg_label(self, text):
        if text:
            self.ui.ui_pages.lastname_reg_label.setText("Sobrenome")
        else:
            self.ui.ui_pages.lastname_reg_label.setText("")

    def do_password_reg_label(self, text):
        if text:
            self.ui.ui_pages.password_reg_label.setText("Senha")
        else:
            self.ui.ui_pages.password_reg_label.setText("")

    def do_email_reg_label(self, text):
        if text:
            self.ui.ui_pages.email_reg_label.setText("Email")
        else:
            self.ui.ui_pages.email_reg_label.setText("")
    # endregion


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
