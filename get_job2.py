import re
import time
from unittest import result
import requests
from selenium.webdriver.common.by import By
from selenium import webdriver
from helium import *


def get_acessKye():
    url = 'http://120.79.250.90:8020'
    str1 = '/apikey?account=yagao321&pwd=yagao321'
    res = requests.get(url + str1)
    print(res.text)
    acesskey = res.json()['data']['accesskey']
    return acesskey
 
 
def get_job(ackey):
    url = 'http://120.79.250.90:8020'
    tt_type = 'gz'   
    str2 = f'/studio/api/task/get?key={ackey}&platform=dy&type={tt_type}&uid=22111433580634&sec_uid=MS4wLjABAAAAjSJ-n-ezIE8OtTDsiCiRP6h0qbQ-IGJA7wngmmvh9xw&filter=video&result=true'
    res = requests.get(url + str2)
    print(res.json())
    if res.json()['success'] == False:
        return 0,0,0,0
    task_id = res.json()['data']['studiotask_id']
    sec_uid = res.json()['data']['params']['sec_uid']
    video_id = res.json()['data']['params']['video_id']
    share_url = res.json()['data']['params']['share_url']
    return task_id, sec_uid, video_id,share_url

def work(driver,sec_uid,waittime):

    # options = webdriver.ChromeOptions()
    driver.get(f'https://www.douyin.com/user/{sec_uid}')
    time.sleep(waittime)
    # 窗口最大化
    driver.maximize_window()
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # 获取源代码
    # html = driver.page_source
    # with open('test.html', 'w') as f:
    #     f.write(html)
    # findelement
    item = driver.find_elements(By.XPATH, '//button[contains(@type,"button") and text()="关注"]')[-1]
    time.sleep(1)
    result = 0
    if item:
        try:
            item.click()
            result = 1
            return result
        except:
            result
        return result
    else:
        return result


    
    
    

    
def finish_job(ackey, task_id):
    url = 'http://120.79.250.90:8020'
    # task_id = '1719194630890717185'
    tt_type = 'gz'   
    str3 = f'/studio/api/task/submit?platform=dy&type={tt_type}&studiotask_id={task_id}&key={ackey}'
    
    res = requests.get(url + str3)
    print(res.text)
    
    
def wooogz(driver,waittime):
    # ackey = get_acessKye()
    # print(ackey)
    ackey = 'AKID7f6253e7538b8c77a47f008a8d39e61f'
    task_id,sec_id,video_id,share_url = get_job(ackey=ackey)
    if task_id != 0:
        print(task_id)
        result = work(driver,sec_id,waittime)
    # n = input("等待确认")
    
        if result == 1:
        # time.sleep(200)
            # finish_job(ackey, task_id)
            print('提交任务')
        else:
            print('任务失败')


def work1(driver,share_url,waittime):
    
    driver.get(share_url)
    time.sleep(waittime)
    driver.maximize_window()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # 滚动到顶部
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(2)
    # 获取源代码
    # html = driver.page_source
    # with open('test.html', 'w') as f:
    #     f.write(html)
    # findelement
    item = driver.find_elements(By.XPATH, '//button[contains(@type,"button") and text()="关注"]')[-1]
    time.sleep(1)
    result = 0
    if item:
        try:
            item.click()
            result = 1
            return result
        except:
            result
        return result
    else:
        return result



def wooogz2(driver,waittime):
    ackey = 'AKID7f6253e7538b8c77a47f008a8d39e61f'
    task_id,sec_id,video_id,share_url = get_job(ackey=ackey)
    if task_id != 0:
        print(task_id)
        result = work1(driver,share_url,waittime)
        
        if result == 1:
            print('提交任务')
            finish_job(ackey, task_id)
        else:
            print('任务失败')
    
    
def work3(brower,share_url,waittime):
    go_to(share_url)
    time.sleep(waittime)
    # 窗口最大化
    for i in range(10):
        time.sleep(1)
        scroll_down(5)
        
    for i in range(10):
        time.sleep(1)
        scroll_up(5)
        
    # 使用helium 找到关注
    # item = find_all('//button[text()="关注"]')
    item = find_all(S('//button[text()="关注"]'))[-1]
    if item:
        try:
            # item[-1].click()
            click(item)
            reslut = 1
        except:
            reslut = 0
    return reslut
    
def wooogz3(brower,waittime):
    ackey = 'AKID7f6253e7538b8c77a47f008a8d39e61f'
    task_id,sec_id,video_id,share_url = get_job(ackey=ackey)
    if task_id != 0:
        print(task_id)
        result = work3(brower,share_url,waittime)
        
        if result == 1:
            print('提交任务')
            # finish_job(ackey, task_id)
        else:
            print('任务失败')
    

    
if __name__ == '__main__':
    wooogz()