# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 16:46:41 2018

@author: zhangp
"""

import requests
from bs4 import BeautifulSoup
import re

text ='FYN_HUMAN 410 G R'


session = requests.Session()
data = {'varspec': text, 'search':'Search'}
d = session.post('http://genetics.bwh.harvard.edu/cgi-bin/pph2/dbsearch.cgi',data = data).text
soup_ncbi = BeautifulSoup(d, features='lxml')
img_links = soup_ncbi.find_all("td")
img_links = img_links[0:15]
with open('1.txt', 'wb')as r:
    out_data_all = []
    for one in img_links:    
        if 'href' in str(one):
            aa = re.match(r'<td>(.*)</td>',str(one))
            aa = aa.group(1)
            aa = re.match(r'<a href=(.*)>(.*)</a>',str(aa))
            out_data = aa.group(2)
        else:
            aa = re.match(r'<td>(.*)</td>',str(one))
            out_data = aa.group(1)
        print(out_data)
        #out_data = str(out_data)
        out_data_all.append(out_data)
    print(out_data_all)
    r.write(out_data_all)
    
#print(img_links)