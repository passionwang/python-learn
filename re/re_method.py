import re

if __name__ == '__main__':

	
	'''
	re.match从第一个位置开始匹配
	re.search从任意位置开始匹配
	'''
	str1 = 'abcdfg>123<'
	print('-------TEST1: match & search------')
	if re.match(r'>123<', str1):
		print('match:' + str(re.match(r'>123<', str1)))
	else:
		print('re.match can not match')
		
	if re.search(r'>123<', str1):
		print('search:' + str(re.search(r'>123<', str1)))
	else:
		print('re.search can not search')

	'''
	使用compile可以实现正则表达式的复用
	rule.match(arg1, arg2),其中arg2可以指定从第几个字符开始匹配，从0开始
	'''
	str2 = 'abcdfg>123<'
	print('-------TEST2: re.compile: match & search------')
	rule = re.compile(r'>123<')
	if rule.match(str2, 6):
		print('match:' + str(rule.match(str2, 6)))
	if rule.search(str2):
		print('search:' + str(rule.search(str2)))

	'''
	匹配完成使用.group可以输出匹配到的字符串
	'''
	str3 = 'abcdfg>123<'
	print('-------TEST3: \d：匹配数字------')
	rule = re.compile(r'>\d+<')
	result = rule.match(str3, 6)
	print(result.group())#匹配不到字符串是没有group这个属性的
	print(rule.match(str3, 6).group())
	print(rule.search(str3).group())

	'''
	re.split,按照正则表达式将字符串分离成list
	'''
	str4 = 'abcdfg>1a2b3<'
	print('-------TEST4: re.split------')
	rule1 = re.compile(r'\d')
	rule2 = re.compile(r'\w')
	rule3 = re.compile(r'z')
	result1 = rule1.split(str4)
	result2 = rule2.split(str4)
	result3 = rule3.split(str4)
	print(result1)
	print(result2)
	print(result3)
	
	'''
	re.findall,按照正则表达式找到所有子串
	从左到有有序返回，返回list
	'''
	str5 = 'abcdfg>1a2b3<'
	print('-------TEST5: re.findall------')
	rule1 = re.compile(r'\d')
	rule2 = re.compile(r'\w')
	rule3 = re.compile(r'z')
	result1 = rule1.findall(str5)
	result2 = rule2.findall(str5)
	result3 = rule3.findall(str5)
	print(result1)
	print(result2)
	print(result3)
	
	'''
	re.finditer,按照正则表达式找到所有子串
	从左到右有序返回，返回迭代器，无匹配返回空列表
	'''
	str6 = 'abcdfg>1a2b3<'
	print('-------TEST6: re.finditer------')
	rule = re.compile(r'\d')
	iter = rule.findall(str6)
	for iter in iter:
		print(iter)
		
	'''
	re.sub,找到re匹配的所有子串，并将其用一个不同的字符串替换
	'''
	str7 = 'abcdfg>1a2b33<'
	print('-------TEST7: re.sub------')
	rule = re.compile(r'\d+')
	result = rule.sub('zz', str7)
	print(result)
	
	'''
	group() 匹配的字符串
	strat()匹配的开始位置
	end()匹配的结束位置
	span()包含开始结束位置
	'''
	str8 = 'abcdfg>1a2b33<'
	print('-------TEST8: 配置的信息------')
	rule = re.compile(r'\d+')
	result = rule.search(str8)
	print(result)
	print(result.group())
	print(result.start())
	print(result.end())
	print(result.span())
		
	
	
	
	
