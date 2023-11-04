from helium import *
import time


def heli_dz():
    start_chrome('https://www.douyin.com')
    # 等待加载完毕
    # wait_until(Button('登录').exists)
    time.sleep(5)
    # 找到登陆按钮
    click('登录')
    time.sleep(1)
    # 找到img   其中有aria-lable=“二维码”的img读取他的src
    qr_codes= find_all(S('img', {'aria-label': '二维码'}))
    if qr_codes:
        src = qr_codes[0].web_element.get_attribute('src')
        print(src)
    
    
    
    
if __name__ == '__main__':
    heli_dz()