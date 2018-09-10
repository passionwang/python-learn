import requests
from bs4 import BeautifulSoup

# r = requests.get('https://api.github.com/events')

#print(r.json())
# print(r.encoding)
#print(r.text)

# r = requests.get('http://github.com', allow_redirects = False)
# print(r.url)
# print(r.history)

url = 'http://www.heibanke.com/lesson/crawler_ex01/'

number = 0

while True:
	params = {'username':'flysmoke', 'password':str(number)}
	r = requests.post(url, data = params)
	if r.text.find(u"密码错误") > 0:
		print(u"密码错误")
		number = number + 1
	else:
		print(r.text)
		break
