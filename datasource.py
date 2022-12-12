import requests

from bs4 import BeautifulSoup
lottery_name = {"賓果賓果": "Bingobingo", "雙贏彩": "Winwin", "威力彩": "Lottery", "38樂合彩": "Lottery38", "大樂透": "Biglottery", "49樂合彩": "Lottery49", "今彩539": "Lottery539",
                "39樂合彩": "Lottery39", "3星彩": "Threestar", "4星彩": "Fourstar"}

response = requests.get('https://www.taiwanlottery.com.tw/index_new.aspx')

bsObj = BeautifulSoup(response.content, "lxml")

ball = bsObj.find('div', {'id': 'rightdown'}).findAll(
    'div', class_='ball_tx ball_yellow')

print('賓果賓果 : -------------')

a='開獎日期 :', bsObj.find('div', {'id': 'rightdown'}).findAll(
    'span', class_='font_black15')[0].text
print(a)

print('開出獎號 :', end=' ')

for index in range(0, 20):

    print(ball[index].text, end=' ')

print()

print('超級號 :', bsObj.find('div', {'id': 'rightdown'}).findAll(
    'div', class_='ball_red')[0].text)
print('猜大小 :', bsObj.find('div', {'id': 'rightdown'}).findAll(
    'div', class_='ball_blue_BB1')[0].text)
print('猜單雙 :', bsObj.find('div', {'id': 'rightdown'}).findAll(
    'div', class_='ball_blue_BB2')[0].text)
