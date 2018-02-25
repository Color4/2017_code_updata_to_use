from urllib.request import urlopen
from bs4 import BeautifulSoup


# if has Chinese, apply decode()
html = urlopen(
    "https://www.ncbi.nlm.nih.gov/pubmed/?term=((fusion%5BTitle%2FAbstract%5D)+OR+rearrangement%5BTitle%2FAbstract%5D)+AND+FGFR%5BTitle%5D"
).read().decode('utf-8')

#html = 'https://www.ncbi.nlm.nih.gov/pubmed/?term=((fusion%5BTitle%2FAbstract%5D)+OR+rearrangement%5BTitle%2FAbstract%5D)+AND+FGFR%5BTitle%5D'

soup = BeautifulSoup(html)
soup_find = soup.body.div.div.form.div
#foup_find_one = soup_find.find_all('div',class='maincontent')
foup_find_one = soup_find.find_all('div',{"class":"rslt"})

print(foup_find_one)
#kk<-foup_find_one[0]
#foup_find_new_one = BeautifulSoup(kk,'lxml')

print(kk)

#soup_find_all = soup_find.find_all('rprt')

#for child in soup_find_all:
#    print('++++++++++++++++++++++++++')
#    print(child)

#print(foup_find_one)


#with open('lhq.txt','wb') as lin:
#    lin.write(html)
#print(html)
