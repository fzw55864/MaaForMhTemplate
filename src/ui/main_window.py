import sys

# -*- coding: UTF-8 -*-
from PySide6.QtWidgets import (
    QHBoxLayout, QGroupBox,QFrame,QComboBox,
     QTableWidget, QTextEdit,
    QSplitter, QHeaderView, QWidget, QVBoxLayout, QPushButton, QLabel,
     QSizePolicy
)
from PySide6.QtGui import QIcon
from PySide6 import QtCore, QtWidgets
from src.service.devices import Devices

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["你好世界", "Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]
        self.resize(800, 600)  # 设置大小
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""

        # 创建主布局
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)

       # 下拉框和按钮组布局
        combo_layout = QHBoxLayout()
        self.combo_box = QComboBox()
        self.combo_box.setMinimumWidth(200)
        combo_layout.addWidget(self.combo_box)

        # 刷新按钮
        self.refresh_btn = QPushButton()
        # self.refresh_btn.setIcon(QIcon('assets/icons/svg_icons/icon_search.svg'))
        self.refresh_btn.setFixedSize(30, 30)
        self.refresh_btn.setToolTip("刷新项目")
        self.refresh_btn.clicked.connect(self.refresh_items)
        combo_layout.addWidget(self.refresh_btn)

        # 编辑按钮
        self.edit_btn = QPushButton()
        # self.edit_btn.setIcon(QIcon('assets/icons/svg_icons/icon_more_options.svg'))
        self.edit_btn.setFixedSize(30, 30)
        self.edit_btn.setToolTip("编辑项目")
        self.edit_btn.clicked.connect(self.edit_items)
        combo_layout.addWidget(self.edit_btn)

        main_layout.addLayout(combo_layout)

        # 分隔线
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(line)

        # 添加按钮
        self.add_btn = QPushButton("添加")
        self.add_btn.setObjectName("addButton")
        self.add_btn.setFixedHeight(35)
        self.add_btn.clicked.connect(self.add_project)
        main_layout.addWidget(self.add_btn)


    def add_project(self):
        devicesStr = Devices().get_all_devices()
        print(devicesStr)

    def edit_items(self):
        print("789")

    def refresh_items(self):
        print("456")
