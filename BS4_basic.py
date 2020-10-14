
# coding: utf-8

# In[5]:


from bs4 import BeautifulSoup
html_doc = """<html><head><title>李映璇</title></head>
<body><h2>adt107101</h2>
<p>This is a test.</p>
<a id="link1" href="/my_link1">Link 1</a>
<a id="link2" href="/my_link2">Link 2</a>
<p>Hello, <b class="boldtext">Bold Text</b></p>
</body></html>"""

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())


# In[6]:


title_tag=soup.title
print(title_tag)


# In[11]:


a_tags=soup.find_all('a')
for tag in a_tags:
    print(tag.string)


# In[14]:



for tag in a_tags:
    print(tag.get('href'))

