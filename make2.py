from helium import start_chrome, kill_browser, click
import time

# 你的其他脚本
from abccd.get_job import wooo
from get_job2 import wooogz3
from hell.h1 import get_profile

def start_browser():
    # Helium 默认会启动一个新的 Chrome 浏览器实例，不需要指定driver路径
    browser = start_chrome('https://www.douyin.com/', headless=False)
    return browser

if __name__ == '__main__':
    # browser = start_browser()
    uid,secuid = get_profile()
    n = input("等待确认")
    if n == '1':
        print('开始')
    waittime = 15
    try:
        # 循环两次
        for _ in range(100):
            time.sleep(1)
            # 这里需要根据wooo和wooogz2的实现来修改，使其兼容Helium
            # 比如如果wooo是点击操作，使用Helium就是：
            # click("按钮的文本或选择器")
            
            # 如果wooogz2与页面交互，可以用Helium提供的函数，如：
            # write('text', into='search box')
            # press(ENTER)

            # 你的逻辑代码
            # wooo(browser, waittime)
            # wooogz2(browser, waittime)
            # ...
            wooogz3(waittime,uid,secuid)

    except KeyboardInterrupt:
        print("正在关闭浏览器...")
        kill_browser()
        print("浏览器已关闭")
