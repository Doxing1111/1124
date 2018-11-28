import requests
from bs4 import BeautifulSoup

html = requests.get('http://www.taiwanlottery.com.tw/result_all.aspx')
html.encoding = 'utf-8'
sp = BeautifulSoup(html.text, 'html.parser')

#抓取最外層
bs1 = sp.select('#right_full')

#威力彩
bs2 = sp.find('h1', class_=' font_red18')

#表格
bs3 = bs1[0].find('table',{'class':'tableWin'})
bs4 = bs3.find_all('span')

#打印出威力彩+開獎號碼,刪除後面空格
print(bs2.text+'開獎號碼:', end='')

#打印從第三個span到第九個span的文字內容,刪除後面空格
for n in range(3,10):
    print(bs4[n].text, end='')


