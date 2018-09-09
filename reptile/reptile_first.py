import urllib.request
import re
from bs4 import BeautifulSoup

html = urllib.request.urlopen('http://www.heibanke.com/lesson/crawler_ex00')
bs_obj = BeautifulSoup(html, 'html.parser')
print(bs_obj)

for i in range(100):
	a_list = bs_obj.findAll('h3')
	print('times:%d h3:' % i + str(a_list))
	rule = re.compile('\d{2,}')
	result = rule.search(str(a_list[0]))
	if result:
		print('code:' + result.group())
		url = 'http://www.heibanke.com/lesson/crawler_ex00' + '/' + result.group()
		print('url:' + url)
		html = urllib.request.urlopen(url)
		bs_obj = BeautifulSoup(html, 'html.parser')		
	else:
		print(bs_obj.html)
		break
