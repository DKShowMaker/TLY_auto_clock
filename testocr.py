# import cv2
# import ddddocr
#
# for i in range(1,30):
#     # image = cv2.imread('.\Captcha\\'+str(i)+'.png')
#     # blur = cv2.pyrMeanShiftFiltering(image, sp=8, sr=60)
#     # # 灰度图像
#     # gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
#     # # 二值化
#     # ret, binary = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY_INV)
#     # # 逻辑运算  让背景为白色  字体为黑  便于识别
#     # cv2.bitwise_not(binary, binary)
#     # cv2.imwrite('.\Captcha\\'+str(i)+'tmp.png',binary)
#     # cv2.imshow('binary-image', binary)
#     # cv2.waitKey(0)
#     # print(contours)
#     ocr = ddddocr.DdddOcr()
#     with open('.\Captcha\\'+str(i)+'.png', 'rb') as f:
#         img_bytes = f.read()
#     res = ocr.classification(img_bytes)
#     res=res.upper()
#     print(res)

import pytesseract
from PIL import Image

for i in range(1,30):
    img=Image.open('.\Captcha\\'+str(i)+'.png')
    config=r'-c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 6'
    print(pytesseract.image_to_string(img,config=config))