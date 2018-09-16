import requests

with requests.Session() as s:
	r = s.get('http://www.baidu.com')
	with open('E:header.html', 'a', encoding = 'utf-8') as f:
		print('-------------------begin----------------')
		print('-------------------headers')
		f.write(str(r.headers))
		print(r.headers)
		'''
		{'Cache-Control': 'private, no-cache, no-store, proxy-revalidate, no-transform', 'Connection': 'Keep-Alive', 'Content-Encoding': 'gzip', 'Content-Type': 'text/html', 'Date': 'Sun, 16 Sep 2018 13:40:03 GMT', 'Last-Modified': 'Mon, 23 Jan 2017 13:27:32 GMT', 'Pragma': 'no-cache', 'Server': 'bfe/1.0.8.18', 'Set-Cookie': 'BDORZ=27315; max-age=86400; domain=.baidu.com; path=/', 'Transfer-Encoding': 'chunked'}
		'''
		print('-------------------requests-headers')
		f.write(str(r.request.headers))
		print(r.request.headers)
		'''
		{'User-Agent': 'python-requests/2.19.1', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
		'''
		print('-------------------text')
	# print(r.text)
	# with open('E:1.html', 'w', encoding = 'utf-8') as f:
		# f.write(r.text)
	