import sys
import json
import configparser

json_file_info = None
user_config_file_info = None

class FileHelper():

    json_file_name = "appsettings.json"
    user_config_file_name = "user.config"
    
    @staticmethod
    def init_config_file():
        FileHelper.read_json_config()
        FileHelper.read_user_config()
    
    # 读取用户配置文件
    @staticmethod
    def read_user_config() -> None:
        print("Reading user config file...")
        try:
            global user_config_file_info
            user_config_file_info = configparser.ConfigParser()
            user_config_file_info.read(FileHelper.user_config_file_name)
        except FileNotFoundError:
            print("User config file not found.")

    # 获取config配置文件属性
    @staticmethod
    def get_user_attribute(module ,key):
        if user_config_file_info is None:
            FileHelper.read_user_config()
        if user_config_file_info is None:
            return ""
        
        return user_config_file_info.get(module,key)

    # 读取json配置文件，获取里面的Code
    @staticmethod
    def read_json_config():
        print("Reading config file...")
        global json_file_info  # 声明使用全局变量
        try:
            with open(FileHelper.json_file_name, 'r') as file:
                config_data = json.load(file)
                json_file_info = config_data  # 将配置数据加载到全局变量中
                print(f"Config loaded: {config_data}")
            return json_file_info
        except FileNotFoundError:
            print("Config file not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON from config file.")
    
    # 获取json配置文件属性
    @staticmethod
    def get_json_attribute(key):
        if json_file_info is None:
            FileHelper.read_config()
        if json_file_info is None:
            return ""
        
        return json_file_info.get(key,'')
