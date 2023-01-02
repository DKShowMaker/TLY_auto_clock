import time
import ddddocr
import requests
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from lxml import etree
import cv2

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

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chromedriver = "/usr/bin/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    browser = webdriver.Chrome(options=chrome_options, executable_path=chromedriver)
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
    time.sleep(5)

    try:
        button = browser.find_element(By.XPATH, '/html/body/div/div/section[2]/div[2]/div[3]/div/div[2]/p[2]/button')
        button.click()
        print('success')
    except:
        print('error')
    else:
        time.sleep(5)
        browser.find_element(By.XPATH,'/html/body/div/div/section[2]/div[2]/div[3]/div/div[2]/div/div[2]/div/div[2]/form/div[1]').screenshot('1.png')
        
        image = cv2.imread('1.png')
        blur = cv2.pyrMeanShiftFiltering(image, sp=8, sr=60)
        # 灰度图像
        gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
        # 二值化
        ret, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
        # 逻辑运算  让背景为白色  字体为黑  便于识别
        cv2.bitwise_not(binary, binary)
        cv2.imwrite('1.png', binary)
        ocr = ddddocr.DdddOcr()
        with open('1.png', 'rb') as f:
            img_bytes = f.read()
        res = ocr.classification(img_bytes)
        # print(len(res))
        # print(res.upper())
        res = res.upper()
        
        input1 =browser.find_element(By.XPATH,'/html/body/div/div/section[2]/div[2]/div[3]/div/div[2]/div/div[2]/div/div[2]/form/div[2]/div/input')
        input1.send_keys(res)
        time.sleep(5)
        button2=browser.find_element(By.XPATH,'/html/body/div/div/section[2]/div[2]/div[3]/div/div[2]/div/div[2]/div/div[2]/form/div[3]/div/input')
        print('success2')
        button2.click()
        time.sleep(5)
        browser.quit()
login()
