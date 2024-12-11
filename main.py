# python -m pip install maafw
import sys
import json
from PySide6 import QtCore, QtWidgets

from src.ui.main_window import MainWindow

# ui转换测试
from src.ui.ui_test import Ui_Form
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTextBrowser, QPushButton
from src.util.filehelp import fileInfo,FileHelper

class MyMainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 初始化 UI
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 初始化配置文件
        FileHelper.init_config_file()

    # 连接信号和槽
    def bind_control_event(self):
        # 获取UI文件中的小部件对象
        self.bt_1 = self.ui.btn_search_devices
        # 连接信号和槽
        self.bt_1.clicked.connect(self.bt_click)

    def bt_click(self):
        print("click")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # 创建APP，将运行脚本时（可能的）的其他参数传给Qt以初始化
    widget = MainWindow()  # 实例化一个MyWidget类对象
    widget.show()  # 显示窗口
    sys.exit(app.exec())  # 正常退出APP：app.exec()关闭app，sys.exit()退出进


# def main():
#     print("main")
    