
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 20:21:51 2018

@author: zhangp
"""
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

my_input_path = 'C:/Users/zhangp/Documents/2017/'
test_all =  ['10.1158/0008-5472.CAN-17-0448','10.1016/j.ejmech.2017.12.062','29293164']
test_all = ['10.1038/nature25187']

def SciHubFunction(paper_dio):
    ncbi_path = 'https://www.ncbi.nlm.nih.gov/pubmed/?term=' + paper_dio
    d_data = urlopen(ncbi_path).read().decode('utf-8')
    soup_ncbi = BeautifulSoup(d_data, features='lxml')
    img_links = soup_ncbi.find_all("h1")
    bb = re.match(r'<h1>(.*)</h1>',str(img_links[1]))
    paper_name_path = bb.group(1)
    paper_name_path = paper_name_path + 'pdf'
    paper_name_path = ''.join(paper_name_path.split(':'))
    ##test sci-hub
    houzui = ['tw','cc','ac','bz','au','mn','la','io']
    for onezhui in houzui:
        path_one = 'http://www.sci-hub.' + onezhui + '/'
        r_stat = requests.get(path_one)
        print(r_stat.status_code)
        if r_stat.status_code == 200:
            usd_path = path_one
            break
        ##test download
    if usd_path != '':
        session = requests.Session()
        paper_name = {'request':paper_dio}
        #r_data = session.post('http://www.sci-hub.tw/', data=paper_name)
        r_data = session.post(usd_path, data=paper_name)
        soup = BeautifulSoup(r_data.content, 'lxml')
        sub_urls =soup.find_all("iframe", {"src": re.compile(r'.*\.pdf')})
        try:
            aa = re.match(r'<iframe id="pdf" src="(.*)"></iframe>',str(sub_urls[0]))
            pdf_name = aa.group(1)
            if 'http:' not in pdf_name:
                pdf_name = 'http:' + pdf_name
            out_path = my_input_path + paper_name_path
            kk = session.get(pdf_name)
            with open(out_path,'wb') as f:
                f.write(kk.content)
        except (IndexError, FileNotFoundError):
            print('Not find %s'%paper_name_path)
            
    else:
        print('All Sic-Hub break')
            

for test_one in test_all:
    SciHubFunction(paper_dio = test_one)
        
