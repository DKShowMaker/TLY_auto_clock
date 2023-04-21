import time
import ddddocr
# import subprocess
import requests
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from lxml import etree
# import undetected_chromedriver as uc
import cv2

flag = 0


def login():
    global flag
    # COOKIE添加
    url = 'https://tly31.com/modules/index.php'
    tlycookie = {'user_pwd': 'c7f8cdcddece84d263ff8987a7eedfcaa144e6774f3d2', 'PHPSESSID': 'l8ucoleu68haat8u1vlg00eac7',
                 'uid': '1729598', '_gid': 'GA1.2.214496544.1672488920', 'lang': 'zh',
                 '_ga': 'GA1.2.2058105441.1672488920', 'user_email': '1320839695%40qq.com', 'is_web': '1'}
    # 浏览器
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--start-maximized')
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--enable-javascript')
    # chrome_options.add_argument('--disable-gpu')
    # user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'
    # chrome_options.add_argument('--user-agent={0}'.format(user_agent))
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:12306")
    # chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # chrome_options.add_experimental_option('useAutomationExtension', True)
    chromedriver = "D:\Program Files (x86)\Python3.9\Scripts\chromedriver"
    browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=chrome_options)
    print('open chrome')
    # 通过程序调用谷歌浏览器，chromedriver需要下载，然后下载路径填到里面。
    browser.get(url)
    for cookie in tlycookie:
        browser.add_cookie({
            "domain": "tly31.com",
            "name": cookie,
            "value": tlycookie[cookie],
            "path": '/',
            "expires": None
        })
    browser.get(url)
    time.sleep(10)
    try:
        browser.find_element(By.CLASS_NAME, 'box-header')  # if webpage is opened successfully
        print('successfully open the page')
    except:
        print('can not open the web page')
        exit(1)
    else:
        try:
            button = browser.find_element(By.XPATH,
                                          '/html/body/div/div/section[2]/div[2]/div[3]/div/div[2]/p[2]/button')
        except:
            print('have signed')
            exit(0)
        else:
            button.click()
            print('NOT SIGN')
            time.sleep(5)
            browser.find_element(By.XPATH,
                                 '/html/body/div/div/section[2]/div[2]/div[3]/div/div[2]/div/div[2]/div/div[2]/form/div[1]').screenshot(
                '1.png')
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
            print(res.upper())
            res = res.upper()

            input1 = browser.find_element(By.XPATH,
                                          '/html/body/div/div/section[2]/div[2]/div[3]/div/div[2]/div/div[2]/div/div[2]/form/div[2]/div/input')
            input1.send_keys(res)
            time.sleep(5)
            button2 = browser.find_element(By.XPATH,
                                           '/html/body/div/div/section[2]/div[2]/div[3]/div/div[2]/div/div[2]/div/div[2]/form/div[3]/div/input')
            button2.click()
            time.sleep(5)
            browser.quit()


while flag == 0:
    login()
    time.sleep(60)
