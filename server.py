import time
from selenium.webdriver.chrome.service import Service as ChromeService

def start_server():
    chrome_driver_path = '/usr/local/bin/chromedriver'  # 更新这个为你的 ChromeDriver 路径
    service = ChromeService(executable_path=chrome_driver_path,port=57366)
    service.start()

    print(f"ChromeDriver 现在正在端口 {service.port} 上运行")
    return service



if __name__ == '__main__':
    service = start_server()
    try:
        while True:
            time.sleep(1)
            print('服务器正在运行')
    except KeyboardInterrupt:
            print("正在停止 ChromeDriver...")
            service.stop()
            print("ChromeDriver 已停止")