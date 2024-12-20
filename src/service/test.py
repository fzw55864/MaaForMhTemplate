import sys
import os

from maa.resource import Resource
from maa.controller import AdbController
from maa.tasker import Tasker
from maa.toolkit import Toolkit

from src.util.filehelp import json_file_info,FileHelper

class Test():
    
    def post_test(self) -> None:
        user_path = os.getenv("USER_PATH", "./")
        Toolkit.init_option(user_path)

        resource = Resource()
        res_job = resource.post_path("assets/resource")
        res_job.wait()

        adb_devices = Toolkit.find_adb_devices()
        if not adb_devices:
            print("No ADB device found.")
            exit()

        # for demo, we just use the first device
        device = adb_devices[0]
        controller = AdbController(
            adb_path=device.adb_path,
            address=device.address,
            screencap_methods=device.screencap_methods,
            input_methods=device.input_methods,
            config=device.config,
        )

        try:
            controller.post_connection().wait()
        except Exception as e:
            print(f"Failed to connect to ADB device: {e}")

        tasker = Tasker()
        # tasker = Tasker(notification_handler=MyNotificationHandler())
        tasker.bind(resource, controller)

        if not tasker.inited:
            print("Failed to init MAA.")
            exit()

        # 初始化
        max_attempts = 5
        attempts = 0
        while attempts < max_attempts:
            task_detail = tasker.post_pipeline("识别返回图标").wait().get()
            if task_detail.status.succeeded():
                task_detail = tasker.post_pipeline("点击返回图标").wait().get()
                if not task_detail.status.succeeded():
                    print("Failed to click return icon.")
                    break
            else:
                print("Failed to recognize return icon.")
                break
            attempts += 1

        # 点击“声音和振动”按钮
        task_detail = tasker.post_pipeline("声音和振动").wait().get()

        if task_detail.status.succeeded():
            print("Success!")
        else:
            print("Failed!")
    
    def file_test(self) -> None:
        # 初始化配置文件
        FileHelper.init_config_file()

        print(f"Using config: {FileHelper.get_json_attribute("Code")}")

        # 使用 fileInfo
        if json_file_info:
            print(f"Using config: {FileHelper.get_json_attribute("Code")}")
        else:
            print("No config available.")
