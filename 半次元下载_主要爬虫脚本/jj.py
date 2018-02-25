import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

session = requests.Session()
paper_dio = '>sp|Q6GZX4|001R_FRG3G Putative transcription factor 001R OS=Frog virus 3 (isolate Goorha) GN=FV3-001R PE=4 SV=1\n MAFSAEDVLKEYDRRRRMEALLLSLYYPNDRKLLDYKEWSPPRVQVECPKAPVEWNNPPSEKGLIVGHFSGIKYKGEKAQASEVDVNKMCCWVSKFKDAMRRYQGIQTCKIPGKVLSDLDAKIKAYNLTVEGVEGFVRYSRVTKQHVAAFLKELRHSKQYENVNLIHYILTDKRVDIQHLEKDLVKDFKALVESAHRMRQGHMINVKYILYQLLKKHGHGPDGPDILTVKTGSKGVLYDDSFRKIYTDLGWKFTPL'
paper_name = {'sequence':paper_dio, 'uid':'500fe2cd-98d3-4e4c-a290-79b4d56bf89b','jid':'784576'}
usd_path = 'https://rostlab.org/services/snap2web/'
head = paper_name

head['Accept']='application\/json, text\/javascript, \*\/\*; q=0.01'
head['Accept-Encoding']='gzip, deflate, br'
head['Accept-Language']=['zh-CN,zh;q=0.9']
head['Connection']='keep-alive'
head['Content-Length']='453'
head['Content-Type']='application/x-www-form-urlencoded; charset=UTF-8'
head['Cookie']='__utmc=103477251; __utmz=103477251.1517809472.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=103477251.378052180.1517809472.1517809472.1518071730.2; __utmt=1; __utmb=103477251.21.10.1518071730'
head['Host']='rostlab.org'
head['Origin']='https://rostlab.org'
head['Referer']='https://rostlab.org/services/snap2web/'
head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
head['X-Requested-With']='XMLHttpRequest'

r_data = session.post(usd_path, data=paper_name)

y_data = session.post('https://rostlab.org/~snap2web/qjobstat.php')
print(r_data)

soup = BeautifulSoup(r_data.content, 'lxml')

print(soup)

#email:

