import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('a')
fileout=open('urlliboutput.txt','w')
for tag in tags:
    fileout.write(tag.get('href', None))
  