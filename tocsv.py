import csv

links = []
urls = open('product_urls.txt')
for line in urls:
	links.append(line)
print len(links)
c = csv.writer(open("MYFILE.csv", "wb"), delimiter=';',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
count = 0
for row in links:
	f = open('products/'+row)
	data = list()
	p = f.readlines()
	# while 1:
	# 	data.append(f.readline())
	# 	line = f.readline()
	# 	if not line: break
	# f.close()

	# print data
	count += 1
	c.writerow(p)
f.close()
print count