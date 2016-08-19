import urllib
from BeautifulSoup import *
import re

webpage ='http://www.zillow.com/homedetails/57369570_zpid/'
html2nd = urllib.urlopen(webpage).read()
zsoup2nd = BeautifulSoup(html2nd)
	#zillowind=open('zillowind.txt','w')
	#zillowind.write(zsoup2nd.prettify()) 
hoafee= zsoup2nd.find(text=re.compile('HOA'))
zpid= '57369570'

if hoafee is None: 
	hoafee= 'NA';
delimiter=';'
record= [zpid,hoafee]
adsp=delimiter.join(record)+'\n'

print adsp	

# html2nd = urllib.urlopen('http://www.zillow.com/homes/comps/57381139_zpid/').read()
# zsoup2nd = BeautifulSoup(html2nd)
# nearbyapts2nd= zsoup2nd('article')
# for apt in nearbyapts2nd: 
# 	address=apt.find('dt', {"class":"listing-address"}).string.strip()


# 	size=apt.find('dt', {"class":"listing-details"}).string.split('\n')
# 	bd=size[1].strip()
# 	ba=size[2].strip()
# 	dimension=size[3].strip()
# 	price=apt.find('dt', {"class":"listing-price"}).string.split(':')
# 	pricenum=price[1].strip()
# 	datesold=apt.find('dt', {"class":"listing-date-sold"}).string.split('Sold')
# 	date=datesold[1].strip()
# 	zpid=apt.parent.get('data-zpid').strip()





# 	delimiter=';'
# 	record= [zpid,address,bd, ba,dimension,pricenum,date]
# 	adsp=delimiter.join(record)+'\n'
# 	zillowrcds.write(adsp)
# 	print adsp

