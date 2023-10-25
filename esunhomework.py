# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 21:07:13 2023

@author: user
"""

from bs4 import BeautifulSoup

import requests

url='https://www.esunbank.com/zh-tw/personal/deposit/rate/forex/foreign-exchange-rates'

header ={
    'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.57'}
 

    
data = requests.get(url,headers = header).text


soup = BeautifulSoup(data,'html.parser')

rate = soup.find(id='exchangeRate')


 
tbody = rate.find('tbody')

trs = tbody.find_all('tr')


for row in trs:
    tds = row.find_all('td',recursive = False)  #關閉遞迴搜尋,預設是True
    if len(tds) == 4:
        print(tds[0].text.strip().split()[0]) 
        print(tds[1].text.strip())
        print(tds[2].text.strip())
        print(tds[3].text.strip())
        print()
'''    
    print(currency)
    print(tds[1].text.strip())
    print(tds[2].text.strip())
    print(tds[3].text.strip())
    print()         

 
 
    print(tds[2].text)
    print(tds[3].text)  
    print()
'''
    