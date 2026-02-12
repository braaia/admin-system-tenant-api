# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modmatwindowoBtzRm.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_ModMatWindow(object):
    def setupUi(self, ModMatWindow):
        if not ModMatWindow.objectName():
            ModMatWindow.setObjectName(u"ModMatWindow")
        ModMatWindow.resize(324, 310)
        self.verticalLayout = QVBoxLayout(ModMatWindow)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(ModMatWindow)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QTabWidget {\n"
"	background-color: rgb(235, 235, 235);\n"
"	border: 1px solid #cccccc;\n"
"	border-radius: none;\n"
"}\n"
"QTabBar:tab {\n"
"	background-color: rgb(235, 235, 235);\n"
"	color: rgb(0, 0, 0);\n"
"	width: 110;\n"
"	height: 25;\n"
"	font: 500 15px;\n"
"	border: 1px solid #cccccc;\n"
"}\n"
"QTabBar:tab:selected {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QTabBar:tab:hover {\n"
"	background-color: rgb(209, 209, 209);\n"
"}\n"
"#tab_qnt {\n"
"	background-color: rgb(235, 235, 235);\n"
"	border: none;\n"
"}\n"
"#tab_valor_uni {\n"
"	background-color: rgb(235, 235, 235);\n"
"	border: none;\n"
"}\n"
"/*Part 2*/\n"
"QLineEdit {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	border: none;\n"
"	border-bottom: 2px solid #cccccc;\n"
"}\n"
"QLineEdit:focus {\n"
"	border-bottom: 2px solid grey;\n"
"}\n"
"/*Part3*/\n"
"#btn_modificar {\n"
"	background-color: rgb(44, 128, 255);\n"
"	border: 1px solid black;\n"
"	border-radius: 4px;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"#btn_mod"
                        "ificar:hover {\n"
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
"	background-color: rgb(255, 255, 255);\n"
"	gridline-color: #cccccc;\n"
"	color: rgb(0, 0, 0);\n"
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
        self.tab_qnt = QWidget()
        self.tab_qnt.setObjectName(u"tab_qnt")
        self.verticalLayout_4 = QVBoxLayout(self.tab_qnt)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 2, -1, -1)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 7, -1, -1)
        self.cbox_012 = QComboBox(self.tab_qnt)
        self.cbox_012.addItem("")
        self.cbox_012.addItem("")
        self.cbox_012.addItem("")
        self.cbox_012.setObjectName(u"cbox_012")
        font = QFont()
        font.setPointSize(11)
        self.cbox_012.setFont(font)

        self.verticalLayout_3.addWidget(self.cbox_012)

        self.verticalSpacer_2 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.txt_material_id = QLineEdit(self.tab_qnt)
        self.txt_material_id.setObjectName(u"txt_material_id")
        self.txt_material_id.setMinimumSize(QSize(0, 30))
        self.txt_material_id.setMaximumSize(QSize(16777215, 30))
        self.txt_material_id.setFont(font)

        self.verticalLayout_2.addWidget(self.txt_material_id)

        self.txt_nova_quantidade = QLineEdit(self.tab_qnt)
        self.txt_nova_quantidade.setObjectName(u"txt_nova_quantidade")
        self.txt_nova_quantidade.setMinimumSize(QSize(0, 30))
        self.txt_nova_quantidade.setMaximumSize(QSize(16777215, 30))
        self.txt_nova_quantidade.setFont(font)

        self.verticalLayout_2.addWidget(self.txt_nova_quantidade)

        self.txt_bloco = QLineEdit(self.tab_qnt)
        self.txt_bloco.setObjectName(u"txt_bloco")
        self.txt_bloco.setMinimumSize(QSize(0, 30))
        self.txt_bloco.setMaximumSize(QSize(16777215, 30))
        self.txt_bloco.setFont(font)

        self.verticalLayout_2.addWidget(self.txt_bloco)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.btn_modificar = QPushButton(self.tab_qnt)
        self.btn_modificar.setObjectName(u"btn_modificar")
        self.btn_modificar.setMinimumSize(QSize(0, 30))
        self.btn_modificar.setMaximumSize(QSize(16777215, 30))
        self.btn_modificar.setFont(font)
        self.btn_modificar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.btn_modificar)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.tabWidget.addTab(self.tab_qnt, "")
        self.tab_valor_uni = QWidget()
        self.tab_valor_uni.setObjectName(u"tab_valor_uni")
        self.tabWidget.addTab(self.tab_valor_uni, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(ModMatWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ModMatWindow)
    # setupUi

    def retranslateUi(self, ModMatWindow):
        ModMatWindow.setWindowTitle(QCoreApplication.translate("ModMatWindow", u"Form", None))
        self.cbox_012.setItemText(0, QCoreApplication.translate("ModMatWindow", u"Adicionar material", None))
        self.cbox_012.setItemText(1, QCoreApplication.translate("ModMatWindow", u"Retirar material", None))
        self.cbox_012.setItemText(2, QCoreApplication.translate("ModMatWindow", u"Definir uma nova quantidade", None))

        self.txt_material_id.setPlaceholderText(QCoreApplication.translate("ModMatWindow", u"ID do material", None))
        self.txt_nova_quantidade.setPlaceholderText(QCoreApplication.translate("ModMatWindow", u"Quantidade", None))
        self.txt_bloco.setPlaceholderText(QCoreApplication.translate("ModMatWindow", u"Bloco", None))
        self.btn_modificar.setText(QCoreApplication.translate("ModMatWindow", u"Modificar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_qnt), QCoreApplication.translate("ModMatWindow", u"Quantidade", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_valor_uni), QCoreApplication.translate("ModMatWindow", u"Valor Unit\u00e1rio", None))
    # retranslateUi

