import sys
import json

fileInfo = None

class FileHelper():

    fileName = "appsettings.json"
    
    @staticmethod
    def init_config_file():
        FileHelper.read_config()
    
    # 读取配置文件，获取里面的Code
    @staticmethod
    def read_config():
        global fileInfo  # 声明使用全局变量
        try:
            with open(FileHelper.fileName, 'r') as file:
                config_data = json.load(file)
                fileInfo = config_data  # 将配置数据加载到全局变量中
                print(f"Config loaded: {config_data}")
            return fileInfo
        except FileNotFoundError:
            print("Config file not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON from config file.")
    
    # 获取配置文件属性
    @staticmethod
    def get_attribute(self, key):
        if fileInfo is None:
            FileHelper.read_config()
        if fileInfo is None:
            return ""
        
        return fileInfo.get(key,'')
