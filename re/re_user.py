import re


if __name__ == '__main__':
	
	print('----------TEST------------')
	
	print('----------ip address------')
	ip1 = '192.168.1.1'
	ip2 = '255.255.255.255'
	ip3 = '3.3.3.3'
	ip4 = '266.1.1.1'
	rule = re.compile(r'(((\d{1,2})|(1\d{2})|(2[0-4]\d)|(25[0-5]))\.){3}((\d{1,2})|(1\d{2})|(2[0-4]\d)|(25[0-5]))')
	result = []
	result.append(rule.match(ip1))
	result.append(rule.match(ip2))
	result.append(rule.match(ip3))
	result.append(rule.match(ip4))
	for res in result:
		#print(res)
		if res:
			print(res.group())
			
	print('----------email address------')
	email1 = 'ajlagj@fjlafj.com'
	email2 = 'dfsff@jfldfj.fdlf.com'
	email3 = 'flsfj.fjslf@dfjldf.fdf.com'
	rule = re.compile(r'\w+[\w\.]*@[\w\.]+\.\w')
	result = []
	result.append(rule.match(email1))
	result.append(rule.match(email2))
	result.append(rule.match(email3))
	for res in result:
		#print(res)
		if res:
			print(res.group())
			


			
