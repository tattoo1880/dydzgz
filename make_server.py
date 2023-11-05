from os import wait
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from selenium import webdriver

from  abccd.get_job import wooo
from get_job2 import wooogz,wooogz2


def start_server():
    chrome_driver_path = '/usr/local/bin/chromedriver'  # 更新这个为你的 ChromeDriver 路径
    service = ChromeService(executable_path=chrome_driver_path,port=57366)
    service.start()

    print(f"ChromeDriver 现在正在端口 {service.port} 上运行")
    return service

if __name__ == '__main__':
    # service = start_server()
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(command_executor='http://127.0.0.1:57366', options=options)
    driver.get('https://www.douyin.com/')
    html = driver.page_source
    
    n = input("等待确认")
    if n == '1':
        print('开始')
    waittime = 15
    try:
        # 循环两次
        for _ in range(19):
        # while True:
            time.sleep(1)
            # wooo(driver,waittime)
            
            # wooogz2(driver,waittime)
            break
            
            
    except KeyboardInterrupt:
        print("正在停止 ChromeDriver...")
        # service.stop()
        print("ChromeDriver 已停止")