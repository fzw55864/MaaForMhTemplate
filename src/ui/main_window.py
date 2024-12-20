import sys
from datetime import datetime, time

# -*- coding: UTF-8 -*-
from PySide6.QtWidgets import (
    QHBoxLayout, QGroupBox,QFrame,QComboBox,
     QTableWidget, QTextEdit,
    QSplitter, QHeaderView, QWidget, QVBoxLayout, QPushButton, QLabel,
     QSizePolicy,QDialog
)
from PySide6.QtCore import QThreadPool, QThreadPool, QRunnable, Signal, Slot, QObject
from PySide6.QtGui import QIcon
from PySide6 import QtCore, QtWidgets
from src.service.devices import Devices

from src.service.exit import ExitTask
from src.service.test import Test
from src.ui.ui_test import Ui_Form
from src.util.filehelp import FileHelper

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # 初始化 UI
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 绑定控件事件
        self.bind_control_event()

        # 初始化线程池
        self.thread_pool = QThreadPool()

    def bind_control_event(self):
        # 获取UI文件中的小部件对象
        self.btn_search_devices = self.ui.btn_search_devices
        # self.btn_shup_up = self.ui.btn_shup_up
        # 连接信号和槽
        self.btn_search_devices.clicked.connect(self.bt_click)
        self.ui.btn_shup_up.clicked.connect(self.shutup)
    
    # 扫描设备
    def bt_click(self):
        print("click")

    # 定时关闭
    def shutup(self):
        # 创建并启动任务
        task = ExitTask()
        task.signals.progress_updated.connect(self.update_label)  # 连接信号到槽
        self.thread_pool.start(task)
        self.ui.btn_shup_up.setEnabled(False)
        self.ui.btn_shup_up.setText("正在关闭...")

    @Slot(str)
    def update_label(self, message):
        # 更新标签文本
        print(message)
        self.ui.btn_shup_up.setText("启用")
        self.ui.btn_shup_up.setEnabled(True)

    # 保存配置
    def save_config(self) -> None:
        FileHelper.Save()

    def add_project(self):
        devicesStr = Devices().get_all_devices()
        print(devicesStr)
        # 系统设置测试
        Test().post_test()
    def edit_items(self):
        print("789")
        dialog = CustomDialog(self)
        dialog.exec()

    def refresh_items(self):
        print("456")

class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("自定义对话框")
        self.setModal(True)
        self.layout = QVBoxLayout(self)
        self.label = QLabel("这是一个模态对话框", self)
        self.layout.addWidget(self.label)