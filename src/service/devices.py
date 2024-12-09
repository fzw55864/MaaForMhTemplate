import random
import sys
import json
from typing import Dict, Any
from datetime import datetime

from maa.tasker import Tasker
from maa.toolkit import Toolkit

class Devices():
    def get_all_devices(self) -> str:
        devices_list = Toolkit.find_adb_devices()
        # Convert each device to a dictionary and convert WindowsPath to string
        devices = [
            {
                "name": device.name,
                "adb_path": str(device.adb_path),  # Convert WindowsPath to string
                "address": device.address,
                "screencap_methods": device.screencap_methods,
                "input_methods": device.input_methods,
                "config": device.config
            }
            for device in devices_list
        ]
        return json.dumps(devices, indent=4)
