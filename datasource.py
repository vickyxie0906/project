import requests

from bs4 import BeautifulSoup
lottery_name = {"賓果賓果": "Bingobingo", "雙贏彩": "Winwin", "威力彩": "Lottery", "_38樂合彩": "Lottery38", "大樂透": "Biglottery", "_49樂合彩": "Lottery49", "今彩539": "Lottery539",
                "_39樂合彩": "Lottery39", "_3星彩": "Threestar", "_4星彩": "Fourstar"}

response = requests.get('https://www.taiwanlottery.com.tw/index_new.aspx')

bsObj = BeautifulSoup(response.content, "lxml")

ball = bsObj.find('div', {'id': 'rightdown'}).findAll(
    'div', class_='ball_tx ball_yellow')

print('賓果賓果 : -------------')
賓果賓果 = ""
賓果賓果 += f"開獎日期 : {bsObj.find('div', {'id': 'rightdown'}).findAll('span', class_='font_black15')[0].text}\n"


賓果賓果 += "開出獎號 : "

for index in range(0, 20):

    賓果賓果 += f"{ball[index].text}"


賓果賓果 += f"\n超級號 :{bsObj.find('div',{'id':'rightdown'}).findAll('div',class_='ball_red')[0].text}\n"
賓果賓果 += f"猜大小 :{bsObj.find('div',{'id':'rightdown'}).findAll('div',class_='ball_blue_BB1')[0].text}\n"
賓果賓果 += f"猜單雙 :{bsObj.find('div',{'id':'rightdown'}).findAll('div',class_='ball_blue_BB2')[0].text}"

print('雙贏彩開獎 : -------------')
雙贏彩 = ""
雙贏彩 += f"開獎日期:{bsObj.find('div', {'id': 'rightdown'}).findAll('span', class_='font_black15')[1].text}\n"

雙贏彩 += "開出順序 :"

for index in range(0, 12):

    雙贏彩 += f"{ball[index].text}"

雙贏彩 += "\n大小順序 :"

for index in range(12, 24):

    雙贏彩 += f"{ball[index].text}"

print('威力彩開獎 : -------------')
威力彩 = ""
威力彩 += f"開獎日期 :{bsObj.find('div', {'id': 'rightdown'}).findAll('span', class_='font_black15')[2].text}\n"

威力彩 += "開出順序 :"

for index in range(0, 6):

    威力彩 += f"{ball[index].text}"


威力彩 += "\n大小順序:"

for index in range(6, 12):

    威力彩 += f"{ball[index].text}"

威力彩 += f"\n特別號: {bsObj.find('div', {'id': 'rightdown'}).findAll('div', class_='ball_red')[1].text}"

print('_38樂合彩開獎 : -------------')
_38樂合彩 = ""
_38樂合彩 += f"開獎日期: {bsObj.find('div', {'id': 'rightdown'}).findAll('span', class_='font_black15')[3].text}\n"

_38樂合彩 += "開出順序:"

for index in range(12, 18):

    _38樂合彩 += f"{ball[index].text}"


_38樂合彩 += "\n大小順序:"
for index in range(18, 24):

    print(ball[index].text, end=' ')


print('大樂透開獎 : -------------')
大樂透 = ""
大樂透 += f"開獎日期 :{ bsObj.find('div', {'id': 'rightdown'}).findAll('span', class_='font_black15')[4].text}\n"

大樂透 += "開出順序:"
for index in range(20, 26):

    大樂透 += f"{ball[index].text}"

大樂透 += "\n大小順序: "
for index in range(26, 32):

    大樂透 += f"{ball[index].text}"

大樂透 += f"特別號 :{bsObj.find('div',{'id':'rightdown'}).findAll('div',class_='ball_red')[2].text}"

print('_49樂合彩開獎 : -------------')
_49樂合彩=""
_49樂合彩+=f"開獎日期: { bsObj.find('div', {'id': 'rightdown'}).findAll('span', class_='font_black15')[5].text}\n"

_49樂合彩 += "開出順序: "
for index in range(32, 38):

  _49樂合彩 += f"{ball[index].text}"


_49樂合彩 += "\n大小順序:"
for index in range(38, 44):

   _49樂合彩 += f"{ball[index].text}"

print('今彩539開獎 : -------------')
今彩539=""
今彩539+=f"開獎日期: {bsObj.find('div', {'id': 'rightdown'}).findAll('span', class_='font_black15')[6].text}\n"

今彩539 += "開出順序: "
for index in range(0, 5):

    今彩539 += f"{ball[index].text}"

今彩539 += "\n大小順序: "
for index in range(5, 10):

    今彩539 += f"{ball[index].text}"

print('_39樂合彩開獎 : -------------')
_39樂合彩=""
_39樂合彩 += f"開獎日期:{bsObj.find('div', {'id': 'rightdown'}).findAll('span', class_='font_black15')[7].text}\n"

_39樂合彩 += "開出順序 :"

for index in range(10, 15):

    _39樂合彩 += f"{ball[index].text}"

_39樂合彩 += "\n大小順序: "
for index in range(15, 20):

    _39樂合彩 += f"{ball[index].text}"

print('_3星彩開獎 : -------------')
_3星彩=""
_3星彩+=f"開獎日期 :{ bsObj.find('div', {'id': 'rightdown'}).findAll('span', class_='font_black15')[8].text}\n"

_3星彩 += "中獎號碼:"
for index in range(0, 3):

   _3星彩 += f"{ball[index].text}"

print('_4星彩開獎 : -------------')
_4星彩 = ""
_4星彩 += f"開獎日期 :{ bsObj.find('div', {'id': 'rightdown'}).findAll('span', class_='font_black15')[9].text}\n"

_4星彩 += "中獎號碼:"
for index in range(3, 7):

   _4星彩 += f"{ball[index].text}"








