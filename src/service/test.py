import sys

from maa.resource import Resource
from maa.controller import AdbController
from maa.tasker import Tasker
from maa.toolkit import Toolkit

class Test():
    
    def post_test(self) -> None:
        user_path = "./"
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
        controller.post_connection().wait()

        tasker = Tasker()
        # tasker = Tasker(notification_handler=MyNotificationHandler())
        tasker.bind(resource, controller)

        if not tasker.inited:
            print("Failed to init MAA.")
            exit()

        # 初始化
        task_detail = tasker.post_pipeline("识别返回图标").wait().get()
        while task_detail.status.succeeded():
            task_detail = tasker.post_pipeline("点击返回图标").wait().get()
            task_detail = tasker.post_pipeline("识别返回图标").wait().get()

        # 点击“声音和振动”按钮
        task_detail = tasker.post_pipeline("声音和振动").wait().get()

        if task_detail.status.succeeded():
            print("Success!")
        else:
            print("Failed!")