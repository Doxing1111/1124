import requests
from bs4 import BeautifulSoup
html = requests.get('http://www.taiwanlottery.com.tw/result_all.aspx')
html.encoding = 'utf-8'
sp = BeautifulSoup(html.text, 'html.parser')

data1 = sp.find('h1', class_='font_red18')
data2 = sp.find('table', class_='tableWin')
data3 = data2.find_all('span')
print(data1.text.strip()+'開獎順序:')
for n in range(3,len(data3)):
    print(data3[n].text+'',end='')