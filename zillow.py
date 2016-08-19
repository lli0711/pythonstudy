import urllib
from BeautifulSoup import *

#url = raw_input('Enter - ')
html = urllib.urlopen('http://www.zillow.com/homes/comps/57365315_zpid/').read()
zsoup = BeautifulSoup(html)

# Retrieve all of the anchor tags
# tags = soup('a')
# fileout=open('urlliboutput.txt','w')
# for tag in tags:
#     fileout.write(tag.get('href', None))
zillowop=open('zillowop.txt','w')
zillowop.write(zsoup.prettify()) 

zillowrcds=open('zillowrcds.txt','w')
nearbyapts= zsoup('article')
for apt in nearbyapts: 
	address=apt.find('dt', {"class":"listing-address"}).string.strip()


	size=apt.find('dt', {"class":"listing-details"}).string.split('\n')
	bd=size[1].strip()
	ba=size[2].strip()
	dimension=size[3].strip()
	price=apt.find('dt', {"class":"listing-price"}).string.split(':')
	pricenum=price[1].strip()
	datesold=apt.find('dt', {"class":"listing-date-sold"}).string.split('Sold')
	date=datesold[1].strip()
	zpid=apt.parent.get('data-zpid').strip()

	delimiter=';'
	record= [address,bd, ba,dimension,pricenum,date,zpid]
	adsp=delimiter.join(record)+'\n'
	zillowrcds.write(adsp)
	print adsp

