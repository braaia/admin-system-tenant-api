from frontend.pages.ui_page import Ui_ApplicationPages
from frontend.qt_core import *
from frontend.widgets.py_push_button import PyPushButton


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")

        # SET INITIAL PARAMETERS
        MainWindow.resize(1280, 720)
        MainWindow.setMaximumSize(1920, 1080)
        MainWindow.setMinimumSize(960, 540)

        # CREATE CENTRAL WIDGET
        self.central_frame = QFrame()

        # CREATE MAIN HORIZONTAL LAYOUT
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)


        #region LEFT MENU
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #44475a")
        self.left_menu.setMaximumWidth(50)
        self.left_menu.setMinimumWidth(50)
        #///////////////////////////////////////////////////////
        self.left_menu.setVisible(True)
        # LEFT MANU LAYOUT
        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_layout.setSpacing(0)
        #endregion

        #region TOP FRAME MENU
        self.left_menu_top_frame = QFrame()
        # self.left_menu_top_frame.setMaximumHeight(30)
        self.left_menu_top_frame.setMinimumHeight(50)
        self.left_menu_top_frame.setObjectName("left_menu_top_frame")

        # TOP FRAME MENU LAYOUT
        self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
        self.left_menu_top_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_top_layout.setSpacing(5)

        # TOP BUTTONS
        self.toggle_menu = PyPushButton("Ocultar Menu", icon_path="icon_menu.svg", icon_color="white")
        self.btn_materiais = PyPushButton("Materiais", is_active=True, icon_path="icon_materials.svg", icon_color="white")
        self.btn_estoque = PyPushButton("Estoque", icon_path="icon_stock.svg", icon_color="white")

        # ADD BUTTONS
        self.left_menu_top_layout.addWidget(self.toggle_menu)
        self.left_menu_top_layout.addWidget(self.btn_materiais)
        self.left_menu_top_layout.addWidget(self.btn_estoque)
        #endregion

        # TOP SPACER MENU
        self.left_menu_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        #region BOTTOM FRAME MENU
        self.left_menu_bottom_frame = QFrame()
        # self.left_menu_bottom_frame.setMaximumHeight(50)
        self.left_menu_bottom_frame.setMinimumHeight(50)
        self.left_menu_bottom_frame.setObjectName("left_menu_bottom_frame")

        # BOTTOM FRAME MENU LAYOUT
        self.left_menu_bottom_layout = QVBoxLayout(self.left_menu_bottom_frame)
        self.left_menu_bottom_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_bottom_layout.setSpacing(0)

        # BOTTOM BUTTONS
        self.btn_settings = PyPushButton("Configurações", icon_path="icon_settings.svg", icon_color="white")
        self.btn_admin = PyPushButton("Admin", icon_path="icon_admin.svg", icon_color="white")
        #////////////////////////////////////////////////////////////////////////////////////////////////////////////
        self.btn_admin.setVisible(False)

        # ADD BUTTONS
        self.left_menu_bottom_layout.addWidget(self.btn_settings)
        self.left_menu_bottom_layout.addWidget(self.btn_admin)
        #endregion


        #region LABEL VERSION
        self.left_menu_label_version = QLabel("v1.0.0.0")
        self.left_menu_label_version.setAlignment(Qt.AlignCenter)
        self.left_menu_label_version.setMaximumHeight(30)
        self.left_menu_label_version.setMinimumHeight(30)
        self.left_menu_label_version.setStyleSheet("color: #c3ccdf")

        # ADD WIDGETS
        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addItem(self.left_menu_spacer)
        self.left_menu_layout.addWidget(self.left_menu_bottom_frame)
        self.left_menu_layout.addWidget(self.left_menu_label_version)
        #endregion


        # CONTENT
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #282a36")

        # MAIN CONTENT LAYOUT
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)


        #region TOP BAR
        self.top_bar = QFrame()
        self.top_bar.setMaximumHeight(40)
        self.top_bar.setMinimumHeight(40)
        self.top_bar.setStyleSheet("background-color: #21232d; color: #6272a4")
        #//////////////////////////////////////////////////////////////////////////
        self.top_bar.setVisible(True)
        # TOP BAR LAYOUT
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(10, 0, 10, 0)

        # TOP LEFT LABEL
        self.top_left_label = QLabel("Sistema de Estoque")
        self.top_left_label.setStyleSheet("font-size: 12pt")

        # TOP MIDDLE SPACER
        self.top_middle_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # TOP RIGHT LABEL
        self.top_right_label = QLabel()
        self.top_right_label.setStyleSheet("font-size: 12pt")

        # ADD WIDGETS TO TOP BAR LAYOUT
        self.top_bar_layout.addWidget(self.top_left_label)
        self.top_bar_layout.addItem(self.top_middle_spacer)
        self.top_bar_layout.addWidget(self.top_right_label)
        #endregion


        #region APP PAGES
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 12pt; color: #f8f8f2")
        self.ui_pages = Ui_ApplicationPages()
        self.ui_pages.setupUi(self.pages)
        self.pages.setCurrentWidget(self.ui_pages.login_page)
        #endregion


        #region BASEBOARD
        self.bottom_bar = QFrame()
        self.bottom_bar.setMaximumHeight(30)
        self.bottom_bar.setMinimumHeight(30)
        self.bottom_bar.setStyleSheet("background-color: #21232d; color: #6272a4")
        # BOTTOM BAR LAYOUT
        self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)
        self.bottom_bar_layout.setContentsMargins(10, 0, 10, 0)

        # BASEBOARD
        self.bottom_left_label = QLabel("Criado por: Wesley Nogueira")
        self.bottom_left_label.setStyleSheet("font: 700 8pt 'Segoi UI'")

        # BOTTOM MIDDLE SPACER
        self.bottom_middle_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # TOP RIGHT LABEL
        self.bottom_right_label = QLabel("© 2026")

        # ADD WIDGETS TO BOTTOM BAR LAYOUT
        self.bottom_bar_layout.addWidget(self.bottom_left_label)
        self.bottom_bar_layout.addItem(self.bottom_middle_spacer)
        self.bottom_bar_layout.addWidget(self.bottom_right_label)
        #endregion


        #region ADD WIDGETS
        # ADD WIDGETS TO CONTENT LAYOUT
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.bottom_bar)

        # ADD WIDGETS TO APP
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)
        #endregion


        MainWindow.setCentralWidget(self.central_frame)