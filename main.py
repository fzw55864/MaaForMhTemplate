# python -m pip install maafw
import sys
import json
from PySide6 import QtCore, QtWidgets

from src.ui.main_window import MainWindow

# ui转换测试
from src.util.filehelp import FileHelper

def TaskRun() -> None:
    app = QtWidgets.QApplication(sys.argv)  # 创建APP，将运行脚本时（可能的）的其他参数传给Qt以初始化
    widget = MainWindow()  # 实例化一个MyWidget类对象
    widget.show()  # 显示窗口
    sys.exit(app.exec())  # 正常退出APP：app.exec()关闭app，sys.exit()退出进

def InitFileInfo()->None:
    # 初始化配置文件
    FileHelper.init_config_file()

if __name__ == "__main__":
    InitFileInfo()
    TaskRun()
