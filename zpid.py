
import urllib
from BeautifulSoup import *

#url = raw_input('Enter - ')
html = urllib.urlopen('http://www.zillow.com/homes/57365315_zpid/').read()
zpidsp = BeautifulSoup(html)

zpiddt=open('zpiddt.txt','w')
zpiddt.write(zpidsp.prettify()) 