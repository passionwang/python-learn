import urllib.request
import re
from bs4 import BeautifulSoup

html = urllib.request.urlopen('http://baike.baidu.com/view/284853.html')
bs_obj = BeautifulSoup(html, 'html.parser')

#print(bs_obj)

print(bs_obj.html.head.title)

#a_list = bs_obj.findAll("a", href = re.compile("baike\.baidu\.com\w?"))
a_list = bs_obj.findAll('a',href=re.compile('baidu'))


for aa in a_list:
	# print(aa)
	if not aa.find('img'):
		if aa.attrs.get('href'):
			print(aa.text, aa.attrs['href'])