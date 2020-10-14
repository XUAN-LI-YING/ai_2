
# coding: utf-8

# In[16]:


import requests
from bs4 import BeautifulSoup
url = 'https://www.chinatimes.com/?chdtv'
r=requests.get(url)
if r.status_code==requests.codes.ok:
   soup = BeautifulSoup(r.text, 'html.parser') 

   title=soup.find_all("h4",class_="title")
   for tag in title:
       print(str(tag.string))
       print('_網址'+tag.find('a').get('href'))
  
     
       

