from datetime import datetime, time
from PySide6.QtCore import QRunnable, Signal, QObject
import time

from src.util.filehelp import FileHelper

# 定义一个任务类，继承自 QRunnable
class ExitTask(QRunnable):
    """
    后台任务类，用于执行后台任务，并使用信号通知主线程任务状态。
    """
    class Signals(QObject):
        progress_updated = Signal(str)

    def __init__(self):
        super().__init__()
        self.signals = self.Signals()
        self._running = True  # 添加一个标志位来控制任务的运行状态

    def run(self):
        print("开始执行: 退出任务")
        while self._running:
            try:
                # 获取配置文件中的时间
                stoptime = FileHelper.get_user_attribute("stop", "stoptime")

                # 使用 strptime 解析配置文件中的时间字符串为 time 对象
                target_time = datetime.strptime(stoptime, "%H:%M").time()

                # 获取当前时间的 time 对象，并只保留小时和分钟
                current_time = datetime.now().time()

                # 判断当前时间是否等于配置文件中的时间
                if current_time.hour == target_time.hour and current_time.minute == target_time.minute:
                    message = "当前时间等于配置文件中的时间，开始执行退出任务"
                    print(message)
                    self.signals.progress_updated.emit(message)  # 发送信号
                    self.stop()  # 停止任务
                else:
                    # 等待 58 秒后再次检查时间
                    time.sleep(58)
            except ValueError as e:
                print(f"时间格式不正确: {e}")
                self.stop()  # 如果时间格式不正确，停止任务
            except Exception as e:
                print(f"发生错误: {e}")
                time.sleep(58)  # 发生其他错误时，等待 58 秒后重试

        print("退出任务执行完毕")
        self.signals.progress_updated.emit("后台任务执行完毕")

    def stop(self):
        """
        停止后台任务
        """
        # TODO: 添加停止任务的逻辑

        self._running = False  # 设置标志位为 False，优雅地停止任务
        print("任务已停止")