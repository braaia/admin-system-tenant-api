import os
import sys

from frontend.qt_core import *


class PyPushButton(QPushButton):
    def __init__(
            self,
            text="",
            height=40,
            minimum_width=50,
            text_padding=55,
            text_color="c3ccdf",
            icon_path="",
            icon_color="c3ccdf",
            btn_color="44475a",
            btn_hover="4f5368",
            btn_pressed="282a36",
            is_active=False
    ):
        super().__init__()

        self.setText(text)
        self.setMaximumHeight(height)
        self.setMinimumHeight(height)
        self.setCursor(Qt.PointingHandCursor)

        self.minimum_width = minimum_width
        self.text_padding = text_padding
        self.text_color = text_color
        self.icon_path = icon_path
        self.icon_color = icon_color
        self.btn_color = btn_color
        self.btn_hover = btn_hover
        self.btn_pressed = btn_pressed
        self.is_active = is_active

        self.set_style(
            text_padding=self.text_padding,
            text_color=self.text_color,
            btn_color=self.btn_color,
            btn_hover=self.btn_hover,
            btn_pressed=self.btn_pressed,
            is_active=self.is_active
        )

    def set_active(self, is_active_menu):
        self.set_style(
            text_padding=self.text_padding,
            text_color=self.text_color,
            btn_color=self.btn_color,
            btn_hover=self.btn_hover,
            btn_pressed=self.btn_pressed,
            is_active=is_active_menu
        )

    def set_style(
            self,
            text_padding=55,
            text_color="c3ccdf",
            btn_color="44475a",
            btn_hover="4f5368",
            btn_pressed="282a36",
            is_active=False
    ):
        style = f"""
        QPushButton {{
            color: #{text_color};
            background-color: #{btn_color};
            padding-left: {text_padding}px;
            text-align: left;
            border: none;
        }}
        QPushButton:hover {{
            background-color: #{btn_hover};
        }}
        QPushButton:pressed {{
            background-color: #{btn_pressed};
        }}
        """

        active_style = f"""
        QPushButton {{
            background-color: #{btn_hover};
            border-right: 5px solid #{btn_pressed};
        }}
        """

        if not is_active:
            self.setStyleSheet(style)
        else:
            self.setStyleSheet(style + active_style)

    def paintEvent(self, event):
        # RETURN DEFAULT EVENT
        QPushButton.paintEvent(self, event)

        # PAINTER
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(Qt.NoPen)

        rect = QRect(0, 0, self.minimum_width, self.height())

        self.draw_icon(qp, self.icon_path, rect, self.icon_color)

        qp.end()

    def draw_icon(self, qp, image, rect, color):
        if not image:
            return

        # Prefer Qt resources; fallback to filesystem for dev builds.
        resource_path = f":/icons/icons/{image}"
        icon = QPixmap(resource_path)
        if icon.isNull():
            if hasattr(sys, "_MEIPASS"):
                base_dir = os.path.join(sys._MEIPASS, "frontend")
            else:
                base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
            icon_path = os.path.normpath(os.path.join(base_dir, "images", "icons", image))
            icon = QPixmap(icon_path)
        if icon.isNull():
            return

        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), color)
        qp.drawPixmap(
            (rect.width() - icon.width()) / 2,
            (rect.height() - icon.height()) / 2,
            icon
        )
        painter.end()
