from requests import Request
from requests import Session

url = r'http://www.baidu.com'
ua_headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
}
ua_data = {
	'username':'wangbiao',
	'password':'wangbiao'
}

s = Session()
req = Request('GET', url, headers = ua_headers, data = ua_data)
prepped = req.prepare()

print('---------------all-request-information---------')
print('\n'.join('%s:%s' % item for item in prepped.__dict__.items()))

response = s.send(prepped#,
	# stream = stream,
	# verify = verity,
	# proxies = proxies,
	# cert = cert,
	# timeout = timeout
)
print('----------------response-----------------------')
print(response.status_code)
print('----------------response-all-------------------')
print('\n'.join('%s:%s' % item for item in response.__dict__.items()))