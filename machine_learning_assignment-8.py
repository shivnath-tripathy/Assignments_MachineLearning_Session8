
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
from collections import Counter
import urllib.request
import nltk
response = urllib.request.urlopen('http://php.net/')
html = response.read()
soup = BeautifulSoup(html,"html5lib")


# In[2]:


#SEE THE HTML TYPE DATA
print(soup.prettify())


# In[3]:


soup.title


# In[4]:


# This gets all the Hyperlink from the webpage which comes under tag 'a' in HTML
for link in soup.find_all('a'):
    print(link.get('href'))


# In[5]:


# GET ALL TEXT
print(soup.get_text())


# In[6]:


from string import punctuation
text = (''.join(s.findAll(text=True))for s in soup.findAll('p'))
c = Counter((x.rstrip(punctuation).lower() for y in text for x in y.split()))
print (c.most_common()) # prints most common words staring at most common.


# In[7]:


import nltk
txts = soup.get_text()  # from soup get the text

#Tokenzie all words after handling Punctuation
words = nltk.wordpunct_tokenize(txts.translate(dict.fromkeys(punctuation)).lower())
words.sort(reverse=True) # Sort the words
print(words) # Print the words
fdist = nltk.FreqDist(words) # GET THE FREQUENCY OF WORDS USING FREQUENCY DISTRIBUTION
print(nltk.FreqDist(words)) # PRINT ALL WORDS


# In[8]:


# PRINT ALL WORDS AND ITS FRQUENCY
for word, freq in fdist.most_common():
     print(u'{}=:{}'.format(word, freq))

