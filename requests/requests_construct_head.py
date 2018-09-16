import urllib.request as urllib2
url = r'http://www.baidu.com'

'''
# 用于模拟http头的User-agent
ua_list = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
        "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
]
'''


ua_headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
}

req = urllib2.Request(url, headers = ua_headers)
print('----------------begin----------------')
print('----------------requests-header')
print(req.headers)
print('----------------requests-type')
print(req.type)
print('----------------requests-data')
print(req.data)
print('----------------requests-three')
print(req.headers, req.type, req.data)

print('----------------requests-all')
print('\n'.join(['%s:%s' % item for item in req.__dict__.items()]))

print('----------------requests-response')
response = urllib2.urlopen(req)
html = response.read()
# print(html.decode('utf-8'))
print('\n'.join(['%s:%s' % item for item in response.__dict__.items()]))
