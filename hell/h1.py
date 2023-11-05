import json
import re
import time
from helium import *
from bs4 import BeautifulSoup
from urllib.parse import unquote 

def get_profile():
    # 打开一个浏览器
    start_chrome('https://www.douyin.com/')
    # 等待with 出现
    # wait_until(S('img', aria_label='二维码').exists)
    # wait_until(lambda: find_all(S('img[aria-label="二维码"]')) != [])
    wait_until(Text('扫描二维码登录').exists,timeout_secs=120)
    time.sleep(20)
    get_driver().save_screenshot('douyin.png')
    # 等待一个用户确认登陆
    n = input('请确认登陆后，输入1继续')
    if n == "1":
        # 等待5s读取当前页面的源码
        time.sleep(5)
        # 获取当前页面的源码
        html = get_driver().page_source
        
        # 用BeautifulSoup解析源码
        soup = BeautifulSoup(html, 'html.parser')
        # 找到id为RENDER_DATA的script标签
        scripts = soup.find_all(id='RENDER_DATA')
        for i in range(len(scripts)):
            print(i)
            str = scripts[i].text
            # 使用urllib.parse.unquote()解码
            str = unquote(str)
            # json.loads()将json字符串转换为字典
            data = json.loads(str)
            uid = data['app']['user']['info']['uid']
            secUid = data['app']['user']['info']['secUid']
            
            print(uid)
            print(secUid)
            
            return uid, secUid
            
            
            
            
        
        
    
    
if __name__ == '__main__':
    get_profile()
    