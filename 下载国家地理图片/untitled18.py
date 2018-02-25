# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 15:57:50 2018

@author: zhangp
"""


from bs4 import BeautifulSoup
import requests

#URL = "http://www.nationalgeographic.com.cn/animals/"

for number_one in range(5000):
    #URL = 'http://www.nationalgeographic.com.cn/animals/photo/4822.html'
    URL = 'http://www.nationalgeographic.com.cn/animals/photo/'+ str(number_one+100) +'.html'
    html = requests.get(URL).text
    soup = BeautifulSoup(html, 'lxml')
    #img_ul = soup.find_all('ul', {"class": "img_list"})
    img_ul = soup.find_all('ul', {"class": "cf"})
    for ul in img_ul:
        imgs = ul.find_all('img')
        for img in imgs:
            url = img['src']
            r = requests.get(url, stream=True)
            image_name = url.split('/')[-1]
            with open('./%s' % image_name, 'wb') as f:
                for chunk in r.iter_content(chunk_size=128):
                        f.write(chunk)
            print('Saved %s' % image_name)
