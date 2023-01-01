import time
import ddddocr
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from lxml import etree

def login():
    url='https://tly30.com/modules/index.php'
    tlycookie={}
    tlycookie['user_pwd']='c7f8cdcddece84d263ff8987a7eedfcaa144e6774f3d2'
    tlycookie['PHPSESSID'] = 'l8ucoleu68haat8u1vlg00eac7'
    tlycookie['uid'] = '1729598'
    tlycookie['_gid'] = 'GA1.2.214496544.1672488920'
    tlycookie['lang'] = 'zh'
    tlycookie['_ga'] = 'GA1.2.2058105441.1672488920'
    tlycookie['user_email'] = '1320839695%40qq.com'
    tlycookie['is_web'] = '1'

    browser = webdriver.Chrome('D:\Program Files (x86)\Python3.9\Scripts\chromedriver.exe')
    # 通过程序调用谷歌浏览器，chromedriver需要下载，然后下载路径填到里面。
    browser.get(url)
    for cookie in tlycookie:
        browser.add_cookie({
            "domain":"tly30.com",
            "name": cookie,
            "value": tlycookie[cookie],
            "path": '/',
            "expires": None
        })
    browser.get(url)
    time.sleep(1)
    button=browser.find_element(By.XPATH,'/html/body/div/div/section[2]/div[2]/div[3]/div/div[2]/p[2]/a')
    try:
        button.click()
    except:
        print('already signed')
    else:
        ocr = ddddocr.DdddOcr()
        with open('1.png', 'rb') as f:
            img_bytes = f.read()
        res = ocr.classification(img_bytes)
        # print(len(res))
        # print(res.upper())
        # res = res.upper()
        # input1 =browser.find_element(By.CSS_SELECTOR,'')
        # input1.send_keys(res)
login()
