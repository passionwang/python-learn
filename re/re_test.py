import re

if __name__ == '__main__':

	str1 = 'abcdfg>123<'

	print('-------TEST1: match & search------')
	'''
	re.match从第一个位置开始匹配
	re.search从任意位置开始匹配
	'''
	if re.match(r'>123<', str1):
		print('match:' + str(re.match(r'>123<', str1)))
	else:
		print('re.match can not match')
		
	if re.search(r'>123<', str1):
		print('search:' + str(re.search(r'>123<', str1)))
	else:
		print('re.search can not search')
	print('-------TEST2: match & search------')
	# if re.match(r'>123<', str1, 6):
		# print('match:' + str(re.match(r'>123<', str1)))
	# if re.search(r'>123<', str1):
		# print('search:' + str(re.search(r'>123<', str1)))

# scmd /k C:\Users\wb\AppData\Local\Programs\Python\Python36\python.exe "$(FULL_CURRENT_PATH)" & PAUSE & EXIT