# -*- coding: utf-8 -*-

import urllib
import re
from BeautifulSoup import BeautifulSoup

product_names = ['Samsung UE','Samsung LE','Samsung PS', 'Sharp LC', 'Sharp LE', 'Panasonic TX',
                     'Philips 19','Philips 2','Philips 3','Philips 4','Philips 5','Philips 6','LG 2','LG 3','LG 4', 'LG M',
                     'LG 5','LG 6', 'Sony KDL','Toshiba 1','Toshiba 2','Toshiba 3','Toshiba 4','Toshiba 5']
product_categoty = ['9','9','9','14','14','13','11','11','11','11','11','11','12','12','12','12','12','12','10','37','37','37','37',
'37']

articles = {
	'UE':'Samsung',
	'LE':'Samsung',
	'LC':'Sharp',
	'LE':'Sharp',
	'TX':'Philips'
}

links = []
urls = open('product_urls.txt')
for line in urls:
	links.append(line)
print links
	
for item in links:
	f = open('products/'+item,'w')
	page = urllib.urlopen("/"+item)
	soup = BeautifulSoup(page.read(), fromEncoding="utf-8")
	body = soup.contents[2].contents[3]
	table = body.contents[1].contents[1].contents[1].contents[2].contents[1].contents
	b = table[3].findAll('b')
	i=0;
	for product in product_names:
		# print ((table[3].find('h1').string.encode('utf-8')).lower()).find(product.lower())
		if ((table[3].find('h1').string.encode('utf-8')).lower()).find(product.lower()) >= 0:
			f.write('1'+'\n')
			name_start = ((table[3].find('h1').string.encode('utf-8')).lower()).find(product.lower())
			f.write(table[3].find('h1').string.encode('utf-8')[name_start:] + '\n')
			f.write('74,'+product_categoty[i]+'\n')
			table = body.contents[1].contents[1].contents[1].contents[2]
			font = table.findAll('font')
			s = font[1]
			s = s.string.encode('utf-8').replace(',','.')
			price = re.findall(r"[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", s)
			f.write(price[2].replace('.',',')+'\n')
			descr_tags = table.contents[1].contents[5].contents[1].contents[1]
			descr_td = descr_tags.findAll('td')
			descr = str(descr_td[0]).replace('\n','')
			f.write(descr)
			i += 1
			break
		elif ((table[3].find('h1').string.encode('utf-8')).lower()).find(product.lower()) < 0:
			for art in articles:
				if ((table[3].find('h1').string.encode('utf-8')).lower()).find(art) >= 0:
					f.write('1'+'\n')
					name_start = ((table[3].find('h1').string.encode('utf-8')).lower()).find(art)
					f.write(articles.get(art)+" "+table[3].find('h1').string.encode('utf-8')[name_start:] + '\n')
					print articles.get(art)+" "+table[3].find('h1').string.encode('utf-8')[name_start:]
					f.write('74,'+product_categoty[i]+'\n')
					table = body.contents[1].contents[1].contents[1].contents[2]
					font = table.findAll('font')
					s = font[1]
					s = s.string.encode('utf-8').replace(',','.')
					price = re.findall(r"[+-]? *(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", s)
					f.write(price[2].replace('.',',')+'\n')
					descr_tags = table.contents[1].contents[5].contents[1].contents[1]
					descr_td = descr_tags.findAll('td')
					descr = str(descr_td[0]).replace('\n','')
					f.write(descr)
					i += 1
					break
		i += 1
	# f.write(table[3].find('h1').string.encode('utf-8') + '\n')
	# f.write('74,9'+'\n')
	# for el in b:
	# 	if el.string is None:
	# 		pass
	# 	else:
	# 		f.write(el.string.encode('utf-8') + '\n')
	f.close()
