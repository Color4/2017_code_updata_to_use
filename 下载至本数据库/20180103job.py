# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 09:21:51 2018

@author: zhangp
"""

import requests
import json

session = requests.Session()
data = {'username': 'zhangp', 'password': 'Edcrfv34'}
r = session.post('http://el.origimed.com/auth', data=data)
data_number = {'searchCategorySecondId':'256'}
#d = session.post('http://el.origimed.com/user/course/my/new', data=data_number)
#d = session.post('http://el.origimed.com/user/course/my')
d = session.post('http://el.origimed.com/log/menu/c')
#print(d.text)
html = session.post('http://el.origimed.com/user/course/my/new?pageSize=100&from=0').text
#print(html['rows'])
print(type(html))
mydata = json.loads(html)
mydata_one = mydata['rows']

for one in mydata_one:
    mydata_two = one
    path_one = 'http://el.origimed.com/resource/course/' + one['RESOURCE_URI']
    #print(path_one)
    out_path = 'C:/Users/zhangp/Documents/2017/' + one['RESOURCE_NAME']
    print(out_path)
    kk = session.get(path_one)
    with open(out_path,'wb') as f:
        f.write(kk.content)
    #urlretrieve(path_one, out_path)
#print(len(mydata_one))
#print(range(10))
#mydata_two = mydata_one[0]
#print(mydata_two['RESOURCE_URI'])

#for link in html:
    #print(link)
#soup = BeautifulSoup(html, 'lxml')
#data_output = soup.html.body.p

#img_p = soup.find_all('p', {"RESOURCE_URI": re.compile('.*?')})
#img_p = soup.find_all('RESOURCE_URI')

#for link in data_output:
    #print(BeautifulSoup(link,'lxml'))
    #for one_link in link:
        #print(one_link)
#print(img_p)
#pdfs = soup.find_all('pdf')

#print(pdfs)

