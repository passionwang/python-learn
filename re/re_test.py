import re

if __name__ == '__main__':

	str1 = 'abcdfg>123<'

	print('-------TEST1: match & search------')
	if re.match(r'>123<', str1):
		print('match:' + str(re.match(r'>123<', str1)))
	if re.search(r'>123<', str1):
		print('search:' + str(re.search(r'>123<', str1)))
	print('-------TEST2: match & search------')
	# if re.match(r'>123<', str1, 6):
		# print('match:' + str(re.match(r'>123<', str1)))
	# if re.search(r'>123<', str1):
		# print('search:' + str(re.search(r'>123<', str1)))

