
import pandas as pd
import sklearn
from bs4 import BeautifulSoup
import urllib3
import requests
import warnings
warnings.filterwarnings('ignore')
import numpy as np


page = requests.get('https://news.ycombinator.com/')

soup = BeautifulSoup(page.content)

print(soup)


body = soup.find('table',class_='itemlist')

lines = body.findAll('tr')

lines[0].findAll('td',{'class':'title'})

lines[0].findAll('td',{'class':'title'})

heading = []
link = []

for i in range(30):
    c=lines[3*i].findAll('td',{'class':'title'})
    heading.append(c[1].a.text)
    link.append(c[1].a.get('href'))

df = pd.DataFrame(data= heading,columns=['Heading'],index=np.arange(1,len(heading)+1,1))

df['link']= link
