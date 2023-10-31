import time
import requests
from http.cookies import SimpleCookie

from selenium import webdriver


def get_acessKye():
    url = 'http://120.79.250.90:8020'
    str1 = '/apikey?account=yagao321&pwd=yagao321'
    res = requests.get(url + str1)
    print(res.text)
    acesskey = res.json()['data']['accesskey']
    return acesskey
 
 
def get_job(ackey):
    url = 'http://120.79.250.90:8020'
    tt_type = 'dz'   
    str2 = f'/studio/api/task/get?key={ackey}&platform=dy&type={tt_type}&uid=22111433580634&sec_uid=MS4wLjABAAAAjSJ-n-ezIE8OtTDsiCiRP6h0qbQ-IGJA7wngmmvh9xw&filter=video&result=true'
    res = requests.get(url + str2)
    print(res.json())
    task_id = res.json()['data']['studiotask_id']
    sec_uid = res.json()['data']['params']['sec_uid']
    video_id = res.json()['data']['params']['video_id']
    share_url = res.json()['data']['params']['share_url']
    return task_id, sec_uid, video_id,share_url

def work(driver,share_url):

    options = webdriver.ChromeOptions()
    driver.get(share_url)


    
    
    

    
def finish_job(ackey, task_id):
    url = 'http://120.79.250.90:8020'
    # task_id = '1719194630890717185'
    tt_type = 'dz'   
    str3 = f'/studio/api/task/submit?platform=dy&type={tt_type}&studiotask_id={task_id}&key={ackey}'
    
    res = requests.get(url + str3)
    print(res.text)
    
    
def wooo(driver):
    # ackey = get_acessKye()
    # print(ackey)
    ackey = 'AKID7f6253e7538b8c77a47f008a8d39e61f'
    task_id,sec_id,share_url,share_url = get_job(ackey=ackey)
    print(task_id)
    work(driver,share_url)
    n = input("等待确认")
    if n == '1':
        # time.sleep(200)
        finish_job(ackey, task_id)
    