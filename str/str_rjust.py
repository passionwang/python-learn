

if __name__ == '__main__':
	"""
	使用ljust、rjust、center来对齐字符串
	"""
	#ljust左对齐，第一个参数表示包括字符串在内的总长度，第二个参数表示填充的字符
	str = 'Test:'.rjust(10, '*')
	print(str)
	#rjust右对齐，第一个参数表示包括字符串在内的总长度，第二个参数表示填充的字符
	str1 = str
	str2 = str1.ljust(15, '*')
	print(str2)
	#center表示居中，第一个参数表示包括字符串在内的总长度，第二个参数表示填充的字符
	str = 'Test:'.center(50, '*')
	print(str)