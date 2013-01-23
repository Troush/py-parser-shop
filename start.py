from HTMLParser import HTMLParser
import urllib2

f = open('product_urls.txt','w')

class save_me():
	data = []
	def save(self,data):
		self.data.append(data)
		f.write(data)
		f.write('\n')
	def return_me(self):
		return self.data
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        pass# print "Encountered a start tag:", tag
        if tag == 'form':
        	if attrs[0][1].find('product') >= 0:
        		array.save(attrs[0][1])
	def handle_endtag(self, tag):
		pass# print "Encountered an end tag :", tag
    def handle_data(self, data):
        pass# print "Encountered some data  :", data
    def return_tags(self,data):
    	return data


i=0
while (i<=200):
	url = SITE_URL+str(i)
	i += 10

	array = save_me()
	parser = MyHTMLParser()
	usock = urllib2.urlopen(url)
	data = usock.read()
	parser.feed(data)

	usock.close()
