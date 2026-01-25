# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagewlWWkk.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
 # noinspection PyUnresolvedReferences
from frontend.images import resources_rc

class Ui_ApplicationPages(object):
    def setupUi(self, ApplicationPages):
        if not ApplicationPages.objectName():
            ApplicationPages.setObjectName(u"ApplicationPages")
        ApplicationPages.resize(1230, 654)
        ApplicationPages.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        ApplicationPages.setStyleSheet(u"")
        ApplicationPages.setLineWidth(3)
        self.materials_page = QWidget()
        self.materials_page.setObjectName(u"materials_page")
        self.materials_page.setStyleSheet(u"#materials_page {\n"
"	background-color: rgb(235, 235, 235);\n"
"}\n"
"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 6px;\n"
"	border: 1px solid black;	\n"
"}\n"
"#frame_11 {\n"
"	background-color: rgb(235, 235, 235);\n"
"	border: none;\n"
"}\n"
"#frame_19 {\n"
"	background-color: rgb(235, 235, 235);\n"
"}\n"
"#frame_15 {\n"
"	border: none;\n"
"}\n"
"#frame_16 {\n"
"	border: none;\n"
"}\n"
"#frame_17 {\n"
"	border: none;\n"
"}\n"
"QLabel {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border: none;\n"
"}\n"
"#label_2 {\n"
"	background-color: rgb(235, 235, 235);\n"
"}\n"
"#label_4 {	\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(50, 50, 50); /* Dark gray background */\n"
"    color: rgb(255, 255, 255);        /* White text color */\n"
"    selection-background-color: rgb(0, 120, 215); /* Color when an i"
                        "tem is highlighted */\n"
"    selection-color: rgb(255, 255, 255);          /* Text color when highlighted */\n"
"}\n"
"QTableWidget {\n"
"	border: none;\n"
"	background-color: rgb(255, 255, 255);\n"
"	gridline-color: #cccccc;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QHeaderView {\n"
"	border: none;\n"
"	background-color: #cccccc;\n"
"	color: rgb(0, 0, 0);\n"
"	border: 2px solid black;\n"
"}\n"
"QHeaderView::section {\n"
"	border: none;\n"
"	background-color: #cccccc;\n"
"	color: rgb(0, 0, 0);\n"
"	font: 13px;\n"
"}\n"
"#txt_filtrar_mat_ent_sai {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border: none;\n"
"	border-bottom: 2px solid #cccccc;\n"
"}\n"
"#txt_filtrar_mat_ent_sai:focus {\n"
"	border-bottom: 2px solid grey;\n"
"}\n"
"#btn_gerar_relatorio_ent_sai {\n"
"	background-color: rgb(85, 206, 57);\n"
"	border: 1px solid black;\n"
"	border-radius: 4px;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"#btn_gerar_relatorio_ent_sai:hover {\n"
"	background-color: rgb(67, 159, 44);\n"
"}\n"
"#btn_atual"
                        "izar_lista_materiais {\n"
"	background-color: rgb(44, 128, 255);\n"
"	border: 1px solid black;\n"
"	border-radius: 4px;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"#btn_atualizar_lista_materiais:hover {\n"
"	background-color: rgb(30, 90, 147);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.horizontalLayout_10 = QHBoxLayout(self.materials_page)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_11 = QFrame(self.materials_page)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_11)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setHorizontalSpacing(10)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.frame_11)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_19)
        self.verticalLayout_24.setSpacing(10)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.frame_19)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 50))
        self.frame_15.setMaximumSize(QSize(16777215, 50))
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.cbox_filtrar_mes = QComboBox(self.frame_15)
        self.cbox_filtrar_mes.addItem("")
        self.cbox_filtrar_mes.addItem("")
        self.cbox_filtrar_mes.addItem("")
        self.cbox_filtrar_mes.addItem("")
        self.cbox_filtrar_mes.addItem("")
        self.cbox_filtrar_mes.addItem("")
        self.cbox_filtrar_mes.addItem("")
        self.cbox_filtrar_mes.addItem("")
        self.cbox_filtrar_mes.addItem("")
        self.cbox_filtrar_mes.addItem("")
        self.cbox_filtrar_mes.addItem("")
        self.cbox_filtrar_mes.addItem("")
        self.cbox_filtrar_mes.addItem("")
        self.cbox_filtrar_mes.setObjectName(u"cbox_filtrar_mes")
        font = QFont()
        font.setPointSize(11)
        self.cbox_filtrar_mes.setFont(font)
        self.cbox_filtrar_mes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_8.addWidget(self.cbox_filtrar_mes)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_10)


        self.verticalLayout_24.addWidget(self.frame_15)

        self.frame_17 = QFrame(self.frame_19)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 50))
        self.frame_17.setMaximumSize(QSize(16777215, 50))
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_4 = QLabel(self.frame_17)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(30, 0))
        self.label_4.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_9.addWidget(self.label_4)

        self.txt_filtrar_mat_ent_sai = QLineEdit(self.frame_17)
        self.txt_filtrar_mat_ent_sai.setObjectName(u"txt_filtrar_mat_ent_sai")
        self.txt_filtrar_mat_ent_sai.setMinimumSize(QSize(300, 0))
        self.txt_filtrar_mat_ent_sai.setMaximumSize(QSize(300, 16777215))
        self.txt_filtrar_mat_ent_sai.setFont(font)

        self.horizontalLayout_9.addWidget(self.txt_filtrar_mat_ent_sai)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_9)

        self.horizontalSpacer_9 = QSpacerItem(850, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_9)


        self.verticalLayout_24.addWidget(self.frame_17)

        self.frame_16 = QFrame(self.frame_19)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_7.setSpacing(8)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.ent_table_widget = QTableWidget(self.frame_16)
        if (self.ent_table_widget.columnCount() < 6):
            self.ent_table_widget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.ent_table_widget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.ent_table_widget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.ent_table_widget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.ent_table_widget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.ent_table_widget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.ent_table_widget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.ent_table_widget.rowCount() < 3):
            self.ent_table_widget.setRowCount(3)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.ent_table_widget.setVerticalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.ent_table_widget.setVerticalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.ent_table_widget.setVerticalHeaderItem(2, __qtablewidgetitem8)
        self.ent_table_widget.setObjectName(u"ent_table_widget")
        self.ent_table_widget.setMinimumSize(QSize(0, 0))
        self.ent_table_widget.setFont(font)
        self.ent_table_widget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.horizontalLayout_7.addWidget(self.ent_table_widget)

        self.saida_table_widget = QTableWidget(self.frame_16)
        if (self.saida_table_widget.columnCount() < 6):
            self.saida_table_widget.setColumnCount(6)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.saida_table_widget.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.saida_table_widget.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.saida_table_widget.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.saida_table_widget.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.saida_table_widget.setHorizontalHeaderItem(4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.saida_table_widget.setHorizontalHeaderItem(5, __qtablewidgetitem14)
        if (self.saida_table_widget.rowCount() < 3):
            self.saida_table_widget.setRowCount(3)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.saida_table_widget.setVerticalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.saida_table_widget.setVerticalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.saida_table_widget.setVerticalHeaderItem(2, __qtablewidgetitem17)
        self.saida_table_widget.setObjectName(u"saida_table_widget")
        self.saida_table_widget.setFont(font)
        self.saida_table_widget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.horizontalLayout_7.addWidget(self.saida_table_widget)

        self.frame_18 = QFrame(self.frame_16)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_18)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.btn_gerar_relatorio_ent_sai = QPushButton(self.frame_18)
        self.btn_gerar_relatorio_ent_sai.setObjectName(u"btn_gerar_relatorio_ent_sai")
        self.btn_gerar_relatorio_ent_sai.setMinimumSize(QSize(140, 40))
        self.btn_gerar_relatorio_ent_sai.setMaximumSize(QSize(140, 16777215))
        self.btn_gerar_relatorio_ent_sai.setFont(font)
        self.btn_gerar_relatorio_ent_sai.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_25.addWidget(self.btn_gerar_relatorio_ent_sai)

        self.btn_atualizar_lista_materiais = QPushButton(self.frame_18)
        self.btn_atualizar_lista_materiais.setObjectName(u"btn_atualizar_lista_materiais")
        self.btn_atualizar_lista_materiais.setMinimumSize(QSize(140, 40))
        self.btn_atualizar_lista_materiais.setMaximumSize(QSize(140, 16777215))
        self.btn_atualizar_lista_materiais.setFont(font)
        self.btn_atualizar_lista_materiais.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_25.addWidget(self.btn_atualizar_lista_materiais)

        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_14)


        self.horizontalLayout_7.addWidget(self.frame_18)


        self.verticalLayout_24.addWidget(self.frame_16)


        self.gridLayout_9.addWidget(self.frame_19, 4, 0, 1, 3)

        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(250, 130))
        self.frame_12.setMaximumSize(QSize(250, 130))
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_12)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(50, -1, -1, -1)
        self.label_26 = QLabel(self.frame_12)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(30, 0))
        self.label_26.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_12.addWidget(self.label_26)

        self.label_17 = QLabel(self.frame_12)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_12.addWidget(self.label_17)


        self.verticalLayout_28.addLayout(self.horizontalLayout_12)

        self.entrada_label = QLabel(self.frame_12)
        self.entrada_label.setObjectName(u"entrada_label")

        self.verticalLayout_28.addWidget(self.entrada_label)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_18 = QLabel(self.frame_12)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(30, 0))
        self.label_18.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_15.addWidget(self.label_18)

        self.label_29 = QLabel(self.frame_12)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_15.addWidget(self.label_29)


        self.verticalLayout_28.addLayout(self.horizontalLayout_15)


        self.verticalLayout_29.addLayout(self.verticalLayout_28)


        self.gridLayout_9.addWidget(self.frame_12, 2, 0, 1, 1)

        self.frame_14 = QFrame(self.frame_11)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(250, 130))
        self.frame_14.setMaximumSize(QSize(16777215, 130))
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(15)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(45, -1, -1, -1)
        self.label_23 = QLabel(self.frame_14)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(30, 0))
        self.label_23.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_14.addWidget(self.label_23)

        self.label_28 = QLabel(self.frame_14)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_14.addWidget(self.label_28)


        self.verticalLayout_26.addLayout(self.horizontalLayout_14)

        self.saldo_atual_label = QLabel(self.frame_14)
        self.saldo_atual_label.setObjectName(u"saldo_atual_label")

        self.verticalLayout_26.addWidget(self.saldo_atual_label)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(10)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_25 = QLabel(self.frame_14)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(30, 0))
        self.label_25.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_17.addWidget(self.label_25)

        self.label_31 = QLabel(self.frame_14)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_17.addWidget(self.label_31)


        self.verticalLayout_26.addLayout(self.horizontalLayout_17)


        self.horizontalLayout_18.addLayout(self.verticalLayout_26)

        self.horizontalSpacer_13 = QSpacerItem(420, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_13)


        self.gridLayout_9.addWidget(self.frame_14, 2, 2, 1, 1)

        self.verticalSpacer_17 = QSpacerItem(20, 4, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout_9.addItem(self.verticalSpacer_17, 1, 0, 1, 1)

        self.label_2 = QLabel(self.frame_11)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 40))
        self.label_2.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_9.addWidget(self.label_2, 0, 0, 1, 3)

        self.verticalSpacer_16 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout_9.addItem(self.verticalSpacer_16, 3, 1, 1, 1)

        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(250, 130))
        self.frame_13.setMaximumSize(QSize(250, 130))
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_13)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(57, -1, -1, -1)
        self.label_20 = QLabel(self.frame_13)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(30, 0))
        self.label_20.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_13.addWidget(self.label_20)

        self.label_27 = QLabel(self.frame_13)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_13.addWidget(self.label_27)


        self.verticalLayout_27.addLayout(self.horizontalLayout_13)

        self.saida_label = QLabel(self.frame_13)
        self.saida_label.setObjectName(u"saida_label")

        self.verticalLayout_27.addWidget(self.saida_label)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(10)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_22 = QLabel(self.frame_13)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(30, 0))
        self.label_22.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_16.addWidget(self.label_22)

        self.label_30 = QLabel(self.frame_13)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_16.addWidget(self.label_30)


        self.verticalLayout_27.addLayout(self.horizontalLayout_16)


        self.verticalLayout_30.addLayout(self.verticalLayout_27)


        self.gridLayout_9.addWidget(self.frame_13, 2, 1, 1, 1)


        self.horizontalLayout_10.addWidget(self.frame_11)

        ApplicationPages.addWidget(self.materials_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.label = QLabel(self.settings_page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(490, 290, 211, 71))
        ApplicationPages.addWidget(self.settings_page)
        self.login_page = QWidget()
        self.login_page.setObjectName(u"login_page")
        self.login_page.setStyleSheet(u"/*Set image background*/\n"
"#login_page {\n"
"	border-image: url(:/images/login_background.jpg)\n"
"}\n"
"\n"
"/* Set color login background*/\n"
"#widget {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"/*Set style for QLaber*/\n"
"QLabel {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(118, 96, 166)\n"
"}\n"
"\n"
"QLabel#label_5 {\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"/*Set style for QLineEdit*/\n"
"QLineEdit {\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-bottom: 2px solid #cccccc;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom: 2px solid rgb(118, 96, 166);\n"
"}\n"
"\n"
"/*Set style for QPushButton*/\n"
"QPushButton {\n"
"	background-color: rgb(48, 32, 58);\n"
"	border: 2px solid #fff;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 12px;\n"
"	padding: 10px;\n"
"	margin-top: 6px;\n"
"}\n"
"\n"
"QPushButton#btn_register {\n"
"	margin-top: 0px;\n"
"}\n"
"\n"
"QPushButton:hover,\n"
"QPushButton:"
                        "clicked {\n"
"	background-color: rgb(34, 23, 42);\n"
"	border: 2px solid #9ac3fe;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.gridLayout_4 = QGridLayout(self.login_page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalSpacer_7 = QSpacerItem(20, 164, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_7, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(397, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.widget = QWidget(self.login_page)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(400, 450))
        self.widget.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer = QSpacerItem(114, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 0, 1, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(20)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setPointSize(18)
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.username_login_label = QLabel(self.widget)
        self.username_login_label.setObjectName(u"username_login_label")
        font2 = QFont()
        font2.setPointSize(10)
        self.username_login_label.setFont(font2)

        self.verticalLayout_5.addWidget(self.username_login_label)

        self.txt_login_username = QLineEdit(self.widget)
        self.txt_login_username.setObjectName(u"txt_login_username")
        self.txt_login_username.setMinimumSize(QSize(250, 30))
        self.txt_login_username.setFont(font)

        self.verticalLayout_5.addWidget(self.txt_login_username)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.password_login_label = QLabel(self.widget)
        self.password_login_label.setObjectName(u"password_login_label")
        self.password_login_label.setFont(font2)

        self.verticalLayout_4.addWidget(self.password_login_label)

        self.txt_login_password = QLineEdit(self.widget)
        self.txt_login_password.setObjectName(u"txt_login_password")
        self.txt_login_password.setMinimumSize(QSize(250, 30))
        self.txt_login_password.setFont(font)

        self.verticalLayout_4.addWidget(self.txt_login_password)


        self.verticalLayout_6.addLayout(self.verticalLayout_4)

        self.btn_login = QPushButton(self.widget)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setMinimumSize(QSize(250, 30))
        self.btn_login.setFont(font)
        self.btn_login.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.btn_login)

        self.btn_register = QPushButton(self.widget)
        self.btn_register.setObjectName(u"btn_register")
        self.btn_register.setMinimumSize(QSize(250, 30))
        self.btn_register.setFont(font)
        self.btn_register.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_6.addWidget(self.btn_register)


        self.gridLayout_2.addLayout(self.verticalLayout_6, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(113, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_6, 2, 1, 1, 1)


        self.gridLayout_4.addWidget(self.widget, 1, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(397, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 163, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_8, 2, 1, 1, 1)

        ApplicationPages.addWidget(self.login_page)
        self.register_page = QWidget()
        self.register_page.setObjectName(u"register_page")
        self.register_page.setStyleSheet(u"/*Set image background*/\n"
"#register_page {\n"
"	border-image: url(:/images/login_background.jpg)\n"
"}\n"
"\n"
"/* Set color login background*/\n"
"#widget_2 {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"/*Set style for QLaber*/\n"
"QLabel {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(118, 96, 166)\n"
"}\n"
"\n"
"QLabel#label_7 {\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"/*Set style for QLineEdit*/\n"
"QLineEdit {\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: none;\n"
"	border-bottom: 2px solid #cccccc;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"	border-bottom: 2px solid rgb(118, 96, 166);\n"
"}\n"
"\n"
"/*Set style for QPushButton*/\n"
"QPushButton {\n"
"	background-color: rgb(48, 32, 58);\n"
"	border: 2px solid #fff;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 12px;\n"
"	padding: 10px;\n"
"	margin-top: 6px;\n"
"}\n"
"\n"
"/*QPushButton#btn_register {\n"
"	margin-top: 0px;\n"
"}*/\n"
"\n"
"QPushButton:hover,\n"
"QPu"
                        "shButton:clicked {\n"
"	background-color: rgb(34, 23, 42);\n"
"	border: 2px solid #9ac3fe;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.gridLayout_6 = QGridLayout(self.register_page)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalSpacer_11 = QSpacerItem(20, 57, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_11, 0, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(347, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_7, 1, 0, 1, 1)

        self.widget_2 = QWidget(self.register_page)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(500, 500))
        self.widget_2.setMaximumSize(QSize(500, 500))
        self.gridLayout_5 = QGridLayout(self.widget_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalSpacer_10 = QSpacerItem(20, 42, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_10, 0, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(105, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_5, 1, 0, 1, 1)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(20)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.verticalLayout_11.addWidget(self.label_7)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.username_reg_label = QLabel(self.widget_2)
        self.username_reg_label.setObjectName(u"username_reg_label")
        self.username_reg_label.setFont(font2)

        self.verticalLayout_9.addWidget(self.username_reg_label)

        self.txt_reg_username = QLineEdit(self.widget_2)
        self.txt_reg_username.setObjectName(u"txt_reg_username")
        self.txt_reg_username.setMinimumSize(QSize(250, 0))
        self.txt_reg_username.setFont(font)

        self.verticalLayout_9.addWidget(self.txt_reg_username)


        self.verticalLayout_11.addLayout(self.verticalLayout_9)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.lastname_reg_label = QLabel(self.widget_2)
        self.lastname_reg_label.setObjectName(u"lastname_reg_label")
        self.lastname_reg_label.setFont(font2)

        self.verticalLayout_10.addWidget(self.lastname_reg_label)

        self.txt_reg_lastname = QLineEdit(self.widget_2)
        self.txt_reg_lastname.setObjectName(u"txt_reg_lastname")
        self.txt_reg_lastname.setFont(font)

        self.verticalLayout_10.addWidget(self.txt_reg_lastname)


        self.verticalLayout_11.addLayout(self.verticalLayout_10)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.email_reg_label = QLabel(self.widget_2)
        self.email_reg_label.setObjectName(u"email_reg_label")
        self.email_reg_label.setFont(font2)

        self.verticalLayout_8.addWidget(self.email_reg_label)

        self.txt_reg_email = QLineEdit(self.widget_2)
        self.txt_reg_email.setObjectName(u"txt_reg_email")
        self.txt_reg_email.setFont(font)

        self.verticalLayout_8.addWidget(self.txt_reg_email)


        self.verticalLayout_11.addLayout(self.verticalLayout_8)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.password_reg_label = QLabel(self.widget_2)
        self.password_reg_label.setObjectName(u"password_reg_label")
        self.password_reg_label.setFont(font2)

        self.verticalLayout_7.addWidget(self.password_reg_label)

        self.txt_reg_password = QLineEdit(self.widget_2)
        self.txt_reg_password.setObjectName(u"txt_reg_password")
        self.txt_reg_password.setFont(font)

        self.verticalLayout_7.addWidget(self.txt_reg_password)


        self.verticalLayout_11.addLayout(self.verticalLayout_7)

        self.btn_register_acc = QPushButton(self.widget_2)
        self.btn_register_acc.setObjectName(u"btn_register_acc")
        self.btn_register_acc.setFont(font)
        self.btn_register_acc.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_11.addWidget(self.btn_register_acc)


        self.gridLayout_5.addLayout(self.verticalLayout_11, 1, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(105, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_6, 1, 2, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 42, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_9, 2, 1, 1, 1)


        self.gridLayout_6.addWidget(self.widget_2, 1, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(347, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_8, 1, 2, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 56, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_12, 2, 1, 1, 1)

        ApplicationPages.addWidget(self.register_page)
        self.sobre_page = QWidget()
        self.sobre_page.setObjectName(u"sobre_page")
        self.verticalLayout_12 = QVBoxLayout(self.sobre_page)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_9 = QFrame(self.sobre_page)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setCursor(QCursor(Qt.CursorShape.ForbiddenCursor))
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_9)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_8 = QLabel(self.frame_9)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setCursor(QCursor(Qt.CursorShape.ForbiddenCursor))

        self.verticalLayout_13.addWidget(self.label_8, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_12.addWidget(self.frame_9)

        ApplicationPages.addWidget(self.sobre_page)
        self.stock_page = QWidget()
        self.stock_page.setObjectName(u"stock_page")
        self.gridLayout_3 = QGridLayout(self.stock_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidgetStock = QTabWidget(self.stock_page)
        self.tabWidgetStock.setObjectName(u"tabWidgetStock")
        self.tabWidgetStock.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.tabWidgetStock.setStyleSheet(u"QTabWidget {\n"
"	background-color: rgb(235, 235, 235);\n"
"	border: 1px solid #cccccc;\n"
"	border-radius: none;\n"
"}\n"
"QTabBar:tab {\n"
"	background-color: rgb(235, 235, 235);\n"
"	color: rgb(0, 0, 0);\n"
"	width: 150;\n"
"	height: 35;\n"
"	font: 500 15px;\n"
"	border: 1px solid #cccccc;\n"
"}\n"
"QTabBar:tab:selected {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QTabBar:tab:hover {\n"
"	background-color: rgb(209, 209, 209);\n"
"}")
        self.tab_cadastrar_mat = QWidget()
        self.tab_cadastrar_mat.setObjectName(u"tab_cadastrar_mat")
        self.tab_cadastrar_mat.setStyleSheet(u"#tab_cadastrar_mat {\n"
"	background-color: rgb(235, 235, 235);\n"
"	border: none;\n"
"}\n"
"#cadastrar_mat_label {\n"
"	background-color: rgb(235, 235, 235);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"#frame_3 {\n"
"	background-color: rgb(235, 235, 235);\n"
"	border: none;\n"
"}\n"
"QLineEdit {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border: none;\n"
"	border-radius: 6px;\n"
"	border-bottom: 2px solid #cccccc;\n"
"}\n"
"QLineEdit:focus {\n"
"	border-bottom: 2px solid grey;\n"
"}\n"
"#btn_cadastrar_mat {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: 1px solid black;\n"
"	border-radius: 6px;\n"
"	color: black;\n"
"}\n"
"#btn_cadastrar_mat:hover {\n"
"	background-color: rgb(220, 220, 220);\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.tab_cadastrar_mat)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_3 = QFrame(self.tab_cadastrar_mat)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.cadastrar_mat_label = QLabel(self.frame_3)
        self.cadastrar_mat_label.setObjectName(u"cadastrar_mat_label")
        self.cadastrar_mat_label.setMinimumSize(QSize(0, 80))
        self.cadastrar_mat_label.setMaximumSize(QSize(16777215, 80))
        self.cadastrar_mat_label.setFont(font1)

        self.gridLayout.addWidget(self.cadastrar_mat_label, 0, 0, 1, 5)

        self.txt_fornecedor = QLineEdit(self.frame_3)
        self.txt_fornecedor.setObjectName(u"txt_fornecedor")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_fornecedor.sizePolicy().hasHeightForWidth())
        self.txt_fornecedor.setSizePolicy(sizePolicy)
        self.txt_fornecedor.setMinimumSize(QSize(700, 40))
        self.txt_fornecedor.setFont(font)
        self.txt_fornecedor.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_fornecedor, 4, 0, 1, 2)

        self.txt_quant = QLineEdit(self.frame_3)
        self.txt_quant.setObjectName(u"txt_quant")
        sizePolicy.setHeightForWidth(self.txt_quant.sizePolicy().hasHeightForWidth())
        self.txt_quant.setSizePolicy(sizePolicy)
        self.txt_quant.setMinimumSize(QSize(220, 40))
        self.txt_quant.setFont(font)
        self.txt_quant.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_quant, 4, 4, 1, 1)

        self.txt_categoria = QLineEdit(self.frame_3)
        self.txt_categoria.setObjectName(u"txt_categoria")
        sizePolicy.setHeightForWidth(self.txt_categoria.sizePolicy().hasHeightForWidth())
        self.txt_categoria.setSizePolicy(sizePolicy)
        self.txt_categoria.setMinimumSize(QSize(0, 40))
        self.txt_categoria.setFont(font)
        self.txt_categoria.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_categoria, 3, 3, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.txt_codigo = QLineEdit(self.frame_3)
        self.txt_codigo.setObjectName(u"txt_codigo")
        sizePolicy.setHeightForWidth(self.txt_codigo.sizePolicy().hasHeightForWidth())
        self.txt_codigo.setSizePolicy(sizePolicy)
        self.txt_codigo.setMinimumSize(QSize(0, 40))
        self.txt_codigo.setMaximumSize(QSize(200, 16777215))
        self.txt_codigo.setFont(font)
        self.txt_codigo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_codigo, 3, 0, 1, 1)

        self.txt_valor_uni = QLineEdit(self.frame_3)
        self.txt_valor_uni.setObjectName(u"txt_valor_uni")
        sizePolicy.setHeightForWidth(self.txt_valor_uni.sizePolicy().hasHeightForWidth())
        self.txt_valor_uni.setSizePolicy(sizePolicy)
        self.txt_valor_uni.setMinimumSize(QSize(100, 40))
        self.txt_valor_uni.setFont(font)
        self.txt_valor_uni.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_valor_uni, 4, 2, 1, 2)

        self.verticalSpacer_3 = QSpacerItem(20, 50, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.gridLayout.addItem(self.verticalSpacer_3, 5, 2, 1, 1)

        self.txt_nome = QLineEdit(self.frame_3)
        self.txt_nome.setObjectName(u"txt_nome")
        sizePolicy.setHeightForWidth(self.txt_nome.sizePolicy().hasHeightForWidth())
        self.txt_nome.setSizePolicy(sizePolicy)
        self.txt_nome.setMinimumSize(QSize(600, 40))
        self.txt_nome.setFont(font)
        self.txt_nome.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.txt_nome, 3, 1, 1, 2)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.btn_cadastrar_mat = QPushButton(self.tab_cadastrar_mat)
        self.btn_cadastrar_mat.setObjectName(u"btn_cadastrar_mat")
        self.btn_cadastrar_mat.setMinimumSize(QSize(200, 40))
        self.btn_cadastrar_mat.setFont(font)
        self.btn_cadastrar_mat.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cadastrar_mat.setAcceptDrops(False)

        self.verticalLayout_2.addWidget(self.btn_cadastrar_mat, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 150, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.tabWidgetStock.addTab(self.tab_cadastrar_mat, "")
        self.tab_verificar_materiais = QWidget()
        self.tab_verificar_materiais.setObjectName(u"tab_verificar_materiais")
        self.tab_verificar_materiais.setStyleSheet(u"#tab_verificar_materiais {\n"
"	background-color: rgb(235, 235, 235);\n"
"	border: none;\n"
"}\n"
"#frame_4 {\n"
"	background-color: rgb(235, 235, 235);\n"
"}\n"
"#label_2 {\n"
"	background-color: rgb(235, 235, 235);\n"
"}\n"
"#frame_4 {\n"
"	border: none;\n"
"}\n"
"#frame {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"/*Part 2*/\n"
"#txt_filtrar_mat_estoque {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border: none;\n"
"	border-bottom: 2px solid #cccccc;\n"
"}\n"
"#txt_filtrar_mat_estoque:focus {\n"
"	border-bottom: 2px solid grey;\n"
"}\n"
"#frame_5 {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 6px;\n"
"	border: 1px solid black;\n"
"}\n"
"/*Part3*/\n"
"#fra {\n"
"	background-color: rgb(235, 235, 235);\n"
"	border: none;\n"
"}\n"
"#btn_gerar_relatorio_estoque {\n"
"	background-color: rgb(85, 206, 57);\n"
"	border: 1px solid black;\n"
"	border-radius: 4px;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"#btn_gerar_relatorio_estoque:hover {\n"
"	background-color: rgb"
                        "(67, 159, 44);\n"
"}\n"
"#btn_modificar_mat {\n"
"	background-color: rgb(255, 255, 15);\n"
"	border: 1px solid black;\n"
"	border-radius: 4px;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"#btn_modificar_mat:hover {\n"
"	background-color: rgb(198, 198, 12);\n"
"}\n"
"#btn_atualizar_lista_estoque {\n"
"	background-color: rgb(44, 128, 255);\n"
"	border: 1px solid black;\n"
"	border-radius: 4px;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"#btn_atualizar_lista_estoque:hover {\n"
"	background-color: rgb(30, 90, 147);\n"
"}\n"
"QComboBox {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"    background-color: rgb(50, 50, 50); /* Dark gray background */\n"
"    color: rgb(255, 255, 255);        /* White text color */\n"
"    selection-background-color: rgb(0, 120, 215); /* Color when an item is highlighted */\n"
"    selection-color: rgb(255, 255, 255);          /* Text color when highlighted */\n"
"}\n"
"QTableWidget {\n"
"	border: none;\n"
"	background-color: rgb(255, 2"
                        "55, 255);\n"
"	gridline-color: #cccccc;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QHeaderView {\n"
"	border: none;\n"
"	background-color: #cccccc;\n"
"	color: rgb(0, 0, 0);\n"
"	border: 2px solid black;\n"
"}\n"
"QHeaderView::section {\n"
"	border: none;\n"
"	background-color: #cccccc;\n"
"	color: rgb(0, 0, 0);\n"
"	font: 13px;\n"
"}\n"
"QFrame {\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 6px;\n"
"	border: 1px solid black;\n"
"}\n"
"QLabel {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border:none\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.tab_verificar_materiais)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_4 = QFrame(self.tab_verificar_materiais)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(15)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_4)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(320, 55))
        self.frame.setMaximumSize(QSize(320, 55))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 10, -1)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.txt_filtrar_mat_estoque = QLineEdit(self.frame)
        self.txt_filtrar_mat_estoque.setObjectName(u"txt_filtrar_mat_estoque")
        font3 = QFont()
        font3.setPointSize(12)
        self.txt_filtrar_mat_estoque.setFont(font3)

        self.horizontalLayout_2.addWidget(self.txt_filtrar_mat_estoque)


        self.verticalLayout_22.addLayout(self.horizontalLayout_2)


        self.gridLayout_7.addWidget(self.frame, 2, 0, 1, 2)

        self.verticalSpacer_13 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout_7.addItem(self.verticalSpacer_13, 1, 2, 1, 1)

        self.verticalSpacer_15 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout_7.addItem(self.verticalSpacer_15, 3, 2, 1, 1)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(250, 110))
        self.frame_7.setMaximumSize(QSize(250, 110))
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_7)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(45, -1, -1, -1)
        self.label_12 = QLabel(self.frame_7)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(30, 0))
        self.label_12.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_5.addWidget(self.label_12)

        self.label_13 = QLabel(self.frame_7)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_5.addWidget(self.label_13)


        self.verticalLayout_15.addLayout(self.horizontalLayout_5)

        self.emestoque_label = QLabel(self.frame_7)
        self.emestoque_label.setObjectName(u"emestoque_label")

        self.verticalLayout_15.addWidget(self.emestoque_label)


        self.verticalLayout_17.addLayout(self.verticalLayout_15)


        self.gridLayout_7.addWidget(self.frame_7, 0, 2, 1, 1)

        self.frame_10 = QFrame(self.frame_4)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(250, 110))
        self.frame_10.setMaximumSize(QSize(250, 110))
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_10)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(15, -1, -1, -1)
        self.label_11 = QLabel(self.frame_10)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(30, 0))
        self.label_11.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_6.addWidget(self.label_11)

        self.label_14 = QLabel(self.frame_10)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_6.addWidget(self.label_14)


        self.verticalLayout_20.addLayout(self.horizontalLayout_6)

        self.abaixodomin_label = QLabel(self.frame_10)
        self.abaixodomin_label.setObjectName(u"abaixodomin_label")

        self.verticalLayout_20.addWidget(self.abaixodomin_label)


        self.verticalLayout_21.addLayout(self.verticalLayout_20)


        self.gridLayout_7.addWidget(self.frame_10, 0, 4, 1, 1)

        self.frame_8 = QFrame(self.frame_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(250, 110))
        self.frame_8.setMaximumSize(QSize(250, 110))
        self.frame_8.setStyleSheet(u"")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_8)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(12)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(55, -1, -1, -1)
        self.label_15 = QLabel(self.frame_8)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(30, 0))
        self.label_15.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_4.addWidget(self.label_15)

        self.label_16 = QLabel(self.frame_8)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_4.addWidget(self.label_16)


        self.verticalLayout_18.addLayout(self.horizontalLayout_4)

        self.emfalta_label = QLabel(self.frame_8)
        self.emfalta_label.setObjectName(u"emfalta_label")

        self.verticalLayout_18.addWidget(self.emfalta_label)


        self.verticalLayout_19.addLayout(self.verticalLayout_18)


        self.gridLayout_7.addWidget(self.frame_8, 0, 3, 1, 1)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(250, 110))
        self.frame_6.setMaximumSize(QSize(250, 110))
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_6)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, -1, -1, -1)
        self.label_10 = QLabel(self.frame_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(30, 0))
        self.label_10.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_3.addWidget(self.label_10)

        self.label_9 = QLabel(self.frame_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(140, 0))
        self.label_9.setMaximumSize(QSize(140, 16777215))

        self.horizontalLayout_3.addWidget(self.label_9)


        self.verticalLayout_14.addLayout(self.horizontalLayout_3)

        self.prod_totais_label = QLabel(self.frame_6)
        self.prod_totais_label.setObjectName(u"prod_totais_label")

        self.verticalLayout_14.addWidget(self.prod_totais_label)


        self.verticalLayout_16.addLayout(self.verticalLayout_14)


        self.gridLayout_7.addWidget(self.frame_6, 0, 1, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_12, 0, 5, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_11, 0, 0, 1, 1)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_5)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.cbox_filtrar_status = QComboBox(self.frame_5)
        self.cbox_filtrar_status.addItem("")
        self.cbox_filtrar_status.addItem("")
        self.cbox_filtrar_status.addItem("")
        self.cbox_filtrar_status.addItem("")
        self.cbox_filtrar_status.setObjectName(u"cbox_filtrar_status")
        self.cbox_filtrar_status.setMinimumSize(QSize(150, 35))
        self.cbox_filtrar_status.setFont(font)
        self.cbox_filtrar_status.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_23.addWidget(self.cbox_filtrar_status)


        self.gridLayout_7.addWidget(self.frame_5, 2, 2, 1, 1)

        self.fra = QFrame(self.frame_4)
        self.fra.setObjectName(u"fra")
        self.horizontalLayout = QHBoxLayout(self.fra)
        self.horizontalLayout.setSpacing(25)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.stock_table_widget = QTableWidget(self.fra)
        if (self.stock_table_widget.columnCount() < 8):
            self.stock_table_widget.setColumnCount(8)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.stock_table_widget.setHorizontalHeaderItem(0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.stock_table_widget.setHorizontalHeaderItem(1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.stock_table_widget.setHorizontalHeaderItem(2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.stock_table_widget.setHorizontalHeaderItem(3, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.stock_table_widget.setHorizontalHeaderItem(4, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.stock_table_widget.setHorizontalHeaderItem(5, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.stock_table_widget.setHorizontalHeaderItem(6, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.stock_table_widget.setHorizontalHeaderItem(7, __qtablewidgetitem25)
        if (self.stock_table_widget.rowCount() < 3):
            self.stock_table_widget.setRowCount(3)
        self.stock_table_widget.setObjectName(u"stock_table_widget")
        self.stock_table_widget.setMinimumSize(QSize(0, 377))
        self.stock_table_widget.setMaximumSize(QSize(16777215, 377))
        self.stock_table_widget.setFont(font)
        self.stock_table_widget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.horizontalLayout.addWidget(self.stock_table_widget)

        self.frame_2 = QFrame(self.fra)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 377))
        self.frame_2.setMaximumSize(QSize(16777215, 377))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_gerar_relatorio_estoque = QPushButton(self.frame_2)
        self.btn_gerar_relatorio_estoque.setObjectName(u"btn_gerar_relatorio_estoque")
        self.btn_gerar_relatorio_estoque.setMinimumSize(QSize(170, 40))
        self.btn_gerar_relatorio_estoque.setMaximumSize(QSize(150, 16777215))
        self.btn_gerar_relatorio_estoque.setFont(font)
        self.btn_gerar_relatorio_estoque.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.btn_gerar_relatorio_estoque)

        self.btn_modificar_mat = QPushButton(self.frame_2)
        self.btn_modificar_mat.setObjectName(u"btn_modificar_mat")
        self.btn_modificar_mat.setMinimumSize(QSize(170, 40))
        self.btn_modificar_mat.setMaximumSize(QSize(150, 16777215))
        self.btn_modificar_mat.setFont(font)
        self.btn_modificar_mat.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.btn_modificar_mat)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.btn_atualizar_lista_estoque = QPushButton(self.frame_2)
        self.btn_atualizar_lista_estoque.setObjectName(u"btn_atualizar_lista_estoque")
        self.btn_atualizar_lista_estoque.setMinimumSize(QSize(170, 40))
        self.btn_atualizar_lista_estoque.setMaximumSize(QSize(150, 16777215))
        self.btn_atualizar_lista_estoque.setFont(font)
        self.btn_atualizar_lista_estoque.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.btn_atualizar_lista_estoque)


        self.horizontalLayout.addWidget(self.frame_2)


        self.gridLayout_7.addWidget(self.fra, 4, 0, 1, 6)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.tabWidgetStock.addTab(self.tab_verificar_materiais, "")

        self.gridLayout_3.addWidget(self.tabWidgetStock, 0, 0, 1, 1)

        ApplicationPages.addWidget(self.stock_page)
        self.change_materials_page = QWidget()
        self.change_materials_page.setObjectName(u"change_materials_page")
        ApplicationPages.addWidget(self.change_materials_page)
        self.admin_page = QWidget()
        self.admin_page.setObjectName(u"admin_page")
        self.label_3 = QLabel(self.admin_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(430, 260, 181, 101))
        ApplicationPages.addWidget(self.admin_page)

        self.retranslateUi(ApplicationPages)

        ApplicationPages.setCurrentIndex(0)
        self.tabWidgetStock.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(ApplicationPages)
    # setupUi

    def retranslateUi(self, ApplicationPages):
        ApplicationPages.setWindowTitle(QCoreApplication.translate("ApplicationPages", u"StackedWidget", None))
        self.cbox_filtrar_mes.setItemText(0, QCoreApplication.translate("ApplicationPages", u"Filtrar por m\u00eas", None))
        self.cbox_filtrar_mes.setItemText(1, QCoreApplication.translate("ApplicationPages", u"Janeiro", None))
        self.cbox_filtrar_mes.setItemText(2, QCoreApplication.translate("ApplicationPages", u"Fevereiro", None))
        self.cbox_filtrar_mes.setItemText(3, QCoreApplication.translate("ApplicationPages", u"Mar\u00e7o", None))
        self.cbox_filtrar_mes.setItemText(4, QCoreApplication.translate("ApplicationPages", u"Abril", None))
        self.cbox_filtrar_mes.setItemText(5, QCoreApplication.translate("ApplicationPages", u"Maio", None))
        self.cbox_filtrar_mes.setItemText(6, QCoreApplication.translate("ApplicationPages", u"Junho", None))
        self.cbox_filtrar_mes.setItemText(7, QCoreApplication.translate("ApplicationPages", u"Julho", None))
        self.cbox_filtrar_mes.setItemText(8, QCoreApplication.translate("ApplicationPages", u"Agosto", None))
        self.cbox_filtrar_mes.setItemText(9, QCoreApplication.translate("ApplicationPages", u"Setembro", None))
        self.cbox_filtrar_mes.setItemText(10, QCoreApplication.translate("ApplicationPages", u"Outubro", None))
        self.cbox_filtrar_mes.setItemText(11, QCoreApplication.translate("ApplicationPages", u"Novembro", None))
        self.cbox_filtrar_mes.setItemText(12, QCoreApplication.translate("ApplicationPages", u"Dezembro\n"
"", None))

        self.cbox_filtrar_mes.setCurrentText("")
        self.cbox_filtrar_mes.setPlaceholderText(QCoreApplication.translate("ApplicationPages", u"Filtrar por m\u00eas", None))
        self.label_4.setText(QCoreApplication.translate("ApplicationPages", u"<html><head/><body><p><img src=\":/icons/icons/icon_search.png\"/></p></body></html>", None))
        self.txt_filtrar_mat_ent_sai.setPlaceholderText(QCoreApplication.translate("ApplicationPages", u"Buscar movimenta\u00e7\u00f5es...", None))
        ___qtablewidgetitem = self.ent_table_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ApplicationPages", u"Data Entrada", None));
        ___qtablewidgetitem1 = self.ent_table_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ApplicationPages", u"Material", None));
        ___qtablewidgetitem2 = self.ent_table_widget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ApplicationPages", u"Fornecedor", None));
        ___qtablewidgetitem3 = self.ent_table_widget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ApplicationPages", u"Quantidade", None));
        ___qtablewidgetitem4 = self.ent_table_widget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("ApplicationPages", u"Valor Unit\u00e1rio", None));
        ___qtablewidgetitem5 = self.ent_table_widget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("ApplicationPages", u"Pre\u00e7o Total", None));
        ___qtablewidgetitem6 = self.ent_table_widget.verticalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("ApplicationPages", u"0", None));
        ___qtablewidgetitem7 = self.ent_table_widget.verticalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("ApplicationPages", u"1", None));
        ___qtablewidgetitem8 = self.ent_table_widget.verticalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("ApplicationPages", u"2", None));
        ___qtablewidgetitem9 = self.saida_table_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("ApplicationPages", u"Data Sa\u00edda", None));
        ___qtablewidgetitem10 = self.saida_table_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("ApplicationPages", u"Material", None));
        ___qtablewidgetitem11 = self.saida_table_widget.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("ApplicationPages", u"Bloco", None));
        ___qtablewidgetitem12 = self.saida_table_widget.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("ApplicationPages", u"Quantidade", None));
        ___qtablewidgetitem13 = self.saida_table_widget.horizontalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("ApplicationPages", u"Valor Unit\u00e1rio", None));
        ___qtablewidgetitem14 = self.saida_table_widget.horizontalHeaderItem(5)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("ApplicationPages", u"Pre\u00e7o Total", None));
        ___qtablewidgetitem15 = self.saida_table_widget.verticalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("ApplicationPages", u"0", None));
        ___qtablewidgetitem16 = self.saida_table_widget.verticalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("ApplicationPages", u"1", None));
        ___qtablewidgetitem17 = self.saida_table_widget.verticalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("ApplicationPages", u"2", None));
        self.btn_gerar_relatorio_ent_sai.setText(QCoreApplication.translate("ApplicationPages", u"Gerar Relat\u00f3rio", None))
        self.btn_atualizar_lista_materiais.setText(QCoreApplication.translate("ApplicationPages", u"Atualizar Lista", None))
        self.label_26.setText(QCoreApplication.translate("ApplicationPages", u"<html><head/><body><p><img src=\":/icons/icons/icon_arrow.png\"/></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("ApplicationPages", u"<html><head/><body><p><span style=\" font-size:14pt;\">Entradas</span></p></body></html>", None))
        self.entrada_label.setText(QCoreApplication.translate("ApplicationPages", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">+350</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("ApplicationPages", u"<html><head/><body><p><img src=\":/icons/icons/icon_days.svg\"/></p></body></html>", None))
        self.label_29.setText(QCoreApplication.translate("ApplicationPages", u"<html><head/><body><p>\u00daltimos 30 dias</p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate("ApplicationPages", u"<html><head/><body><p><img src=\":/icons/icons/icon_stock.png\"/></p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate("ApplicationPages", u"<html><head/><body><p><span style=\" font-size:14pt;\">Saldo Atual</span></p></body></html>", None))
        self.saldo_atual_label.setText(QCoreApplication.translate("ApplicationPages", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">230</span></p></body></html>", None))
        self.label_25.setText(QCoreApplication.translate("ApplicationPages", u"<html><head/><body><p><img src=\":/icons/icons/icon_days.svg\"/></p></body></html>", None))
        self.label_31.setText(QCoreApplication.translate("ApplicationPages", u"\u00daltimos 30 dias", None))
        self.label_2.setText(QCoreApplication.translate("ApplicationPages", u"<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">Movimenta\u00e7\u00f5es de Estoque</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("ApplicationPages", u"<html><head/><body><p><img src=\":/icons/icons/icon_down.png\"/></p></body></html>", None))
        self.label_27.setText(QCoreApplication.translate("ApplicationPages", u"<html><head/><body><p><span style=\" font-size:14pt;\">Sa\u00eddas</span></p></body></html>", None))
        self.saida_label.setText(QCoreApplication.translate("ApplicationPages", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">-120</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("ApplicationPages", u"<html><head/><body><p><img src=\":/icons/icons/icon_days.svg\"/></p></body></html>", None))
        self.label_30.setText(QCoreApplication.translate("ApplicationPages", u"\u00daltimos 30 dias", None))
        self.label.setText(QCoreApplication.translate("ApplicationPages", u"settings page", None))
        self.label_5.setText(QCoreApplication.translate("ApplicationPages", u"<html><head/><body><p><span style=\" font-weight:700;\">Bem-Vindo</span></p></body></html>", None))
        self.username_login_label.setText(QCoreApplication.translate("ApplicationPages", u"Email", None))
        self.password_login_label.setText(QCoreApplication.translate("ApplicationPages", u"Senha", None))
        self.btn_login.setText(QCoreApplication.translate("ApplicationPages", u"Entrar", None))
        self.btn_register.setText(QCoreApplication.translate("ApplicationPages", u"Se Registrar", None))
        self.label_7.setText(QCoreApplication.translate("ApplicationPages", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Se Registre</span></p></body></html>", None))
        self.username_reg_label.setText(QCoreApplication.translate("ApplicationPages", u"Nome", None))
        self.lastname_reg_label.setText(QCoreApplication.translate("ApplicationPages", u"Sobrenome", None))
        self.email_reg_label.setText(QCoreApplication.translate("ApplicationPages", u"Email", None))
        self.password_reg_label.setText(QCoreApplication.translate("ApplicationPages", u"Senha", None))
        self.btn_register_acc.setText(QCoreApplication.translate("ApplicationPages", u"Registrar", None))
        self.label_8.setText(QCoreApplication.translate("ApplicationPages", u"Por favor, entre em contato com o dono do software para ter acesso as funcionalidades!", None))
        self.cadastrar_mat_label.setText(QCoreApplication.translate("ApplicationPages", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Cadastrar Material</span></p></body></html>", None))
        self.txt_fornecedor.setPlaceholderText(QCoreApplication.translate("ApplicationPages", u"Fornecedor", None))
        self.txt_quant.setPlaceholderText(QCoreApplication.translate("ApplicationPages", u"Quantidade", None))
        self.txt_categoria.setPlaceholderText(QCoreApplication.translate("ApplicationPages", u"Categoria", None))
        self.txt_codigo.setPlaceholderText(QCoreApplication.translate("ApplicationPages", u"C\u00f3digo", None))
        self.txt_valor_uni.setPlaceholderText(QCoreApplication.translate("ApplicationPages", u"Valor Unit\u00e1rio", None))
        self.txt_nome.setPlaceholderText(QCoreApplication.translate("ApplicationPages", u"Nome do Material", None))
        self.btn_cadastrar_mat.setText(QCoreApplication.translate("ApplicationPages", u"Cadastrar", None))
        self.tabWidgetStock.setTabText(self.tabWidgetStock.indexOf(self.tab_cadastrar_mat), QCoreApplication.translate("ApplicationPages", u"Cadastrar", None))
        self.label_6.setText(QCoreApplication.translate("ApplicationPages", u"<html><head/><body><p><img src=\":/icons/icons/icon_search.png\"/></p></body></html>", None))
        self.txt_filtrar_mat_estoque.setPlaceholderText(QCoreApplication.translate("ApplicationPages", u"Filtrar materiais...", None))
        self.label_12.setText(QCoreApplication.translate("ApplicationPages", u"<html><head/><body><p><img src=\":/icons/icons/icon_in_stock.png\"/></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("ApplicationPages", u"<html><head/><body><p><span style=\" font-size:14pt;\">Em estoque</span></p></body></html>", None))
        self.emestoque_label.setText(QCoreApplication.translate("ApplicationPages", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">350</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("ApplicationPages", u"<html><head/><body><p><img src=\":/icons/icons/icon_orange_warning.png\"/></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("ApplicationPages", u"<html><head/><body><p><span style=\" font-size:14pt;\">Abaixo do m\u00ednimo</span></p></body></html>", None))
        self.abaixodomin_label.setText(QCoreApplication.translate("ApplicationPages", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">120</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("ApplicationPages", u"<html><head/><body><p><img src=\":/icons/icons/icon_red_warning.png\"/></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("ApplicationPages", u"<html><head/><body><p><span style=\" font-size:14pt;\">Em falta</span></p></body></html>", None))
        self.emfalta_label.setText(QCoreApplication.translate("ApplicationPages", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">50</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("ApplicationPages", u"<html><head/><body><p><img src=\":/icons/icons/icon_stock.png\"/></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("ApplicationPages", u"<html><head/><body><p><span style=\" font-size:14pt;\">Produtos totais</span></p></body></html>", None))
        self.prod_totais_label.setText(QCoreApplication.translate("ApplicationPages", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">400</span></p></body></html>", None))
        self.cbox_filtrar_status.setItemText(0, QCoreApplication.translate("ApplicationPages", u"Todos", None))
        self.cbox_filtrar_status.setItemText(1, QCoreApplication.translate("ApplicationPages", u"Disponivel", None))
        self.cbox_filtrar_status.setItemText(2, QCoreApplication.translate("ApplicationPages", u"Abaixo do minimo", None))
        self.cbox_filtrar_status.setItemText(3, QCoreApplication.translate("ApplicationPages", u"Em falta", None))

        self.cbox_filtrar_status.setPlaceholderText(QCoreApplication.translate("ApplicationPages", u"Filtrar por status", None))
        ___qtablewidgetitem18 = self.stock_table_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("ApplicationPages", u"C\u00f3digo", None));
        ___qtablewidgetitem19 = self.stock_table_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("ApplicationPages", u"Material", None));
        ___qtablewidgetitem20 = self.stock_table_widget.horizontalHeaderItem(2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("ApplicationPages", u"Fornecedor", None));
        ___qtablewidgetitem21 = self.stock_table_widget.horizontalHeaderItem(3)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("ApplicationPages", u"Categoria", None));
        ___qtablewidgetitem22 = self.stock_table_widget.horizontalHeaderItem(4)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("ApplicationPages", u"Valor Unit\u00e1rio", None));
        ___qtablewidgetitem23 = self.stock_table_widget.horizontalHeaderItem(5)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("ApplicationPages", u"Pre\u00e7o Total", None));
        ___qtablewidgetitem24 = self.stock_table_widget.horizontalHeaderItem(6)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("ApplicationPages", u"Quantidade", None));
        ___qtablewidgetitem25 = self.stock_table_widget.horizontalHeaderItem(7)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("ApplicationPages", u"Status", None));
        self.btn_gerar_relatorio_estoque.setText(QCoreApplication.translate("ApplicationPages", u"Gerar Relat\u00f3rio", None))
        self.btn_modificar_mat.setText(QCoreApplication.translate("ApplicationPages", u"Modificar Material", None))
        self.btn_atualizar_lista_estoque.setText(QCoreApplication.translate("ApplicationPages", u"Atualizar Lista", None))
        self.tabWidgetStock.setTabText(self.tabWidgetStock.indexOf(self.tab_verificar_materiais), QCoreApplication.translate("ApplicationPages", u"Materiais", None))
        self.label_3.setText(QCoreApplication.translate("ApplicationPages", u"admin page", None))
    # retranslateUi

