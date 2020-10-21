
# coding: utf-8

# In[11]:


import requests
from bs4 import BeautifulSoup
google_url='https://www.taiwanlottery.com.tw/'
html=requests.get(google_url)
sp=BeautifulSoup(html.text,'html.parser')
#print(sp.prettify())
data1=sp.find_all('div',{'class':'contents_box02'})
data2=data1[2].find_all('div',{'class':'ball_tx ball_yellow'})
print("開出順序:",end="")
for n in range(0,6):
    print(data2[n].text,end="")
print("大小順序:",end="")
for n in range(6,12):
    print(data2[n].text,end="")
print("開出順序:",end="")
data3=data1[2].find_all('div',{'class':'ball_red'})
print(data3[0].text,end="")


# In[4]:




