import asyncio
from re import S
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import base64
from bs4 import BeautifulSoup


async def test_login():

    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    driver = webdriver.Chrome(options=options)
    # 窗口最大化
    driver.maximize_window()
    # get 痘印
    driver.get("https://www.douyin.com/")
    # 等待页面加载完成
    try:
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.CLASS_NAME, "web-login-scan-code__content")))
        # 获得源码
        time.sleep(15)
        html = driver.page_source
        # 使用bs4解析
        soup = BeautifulSoup(html, 'html.parser')
        # 获取二维码
        img = soup.find('img', class_='web-login-scan-code__content__qrcode-wrapper__qrcode')
        if img:
            print(img['src'])
            src = img['src']
            img_data = src.split(',')[1]
            # 解码
            img_data = base64.b64decode(img_data)
            # 保存图片
            file = open('qrcode.png', 'wb')
            file.write(img_data)
            file.close()
            
            confirm = 0
            confirm = input('是否登录成功？(0/1)')
            if confirm == "1":
                print('登录成功')
                # 取得cookies
                cookies = driver.get_cookies()
                print(cookies)
                # 键值对处理cookies
                cookies = {i['name']:i['value'] for i in cookies}
                print(cookies)
                with open('cookies.txt','w')as f:
                    f.write(str(cookies))
            else:                
                driver.quit()
        else:
            print('二维码获取失败')
    except Exception as e:
        print(e)
    
if __name__ == '__main__':
    asyncio.run(test_login())

