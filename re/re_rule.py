import re

if __name__ == '__main__':
	
	print('-----------TEST:------------')
	print('-----------\d-数字----------')
	
	str1 = 'angaolaf12"34535235nvl<>aj,f.12/31[4v]lf"mlf'
	rule_d = re.compile(r'\d')
	result_d = rule_d.search(str1)
	if result_d:
		print('old:' + str1)
		print('new:' + result_d.group())
	
	print('-----------\w-字母&数字-----')	
	str2 = 'angaolaf12"34535235nvl<>aj,f.12/31[4v]lf"mlf'
	rule_d = re.compile(r'\w')
	result_d = rule_d.search(str2)
	if result_d:
		print('old:' + str2)
		print('new:' + result_d.group())
		
	print('-----------\w-----findall---')	
	str3 = 'angaolaf12"34535235nvl<>aj,f.12/31[4v]lf"mlf'
	rule_d = re.compile(r'\w')
	result_d = rule_d.findall(str3)
	if result_d:
		print('old:' + str3)
		print('new:' + str(result_d))
		
	print('-----------.-匹配任意数字---')	
	str4 = 'angaolaf12"34535235nvl<>aj,f.12/31[4v]lf"mlf'
	rule_d = re.compile(r'.')
	result_d = rule_d.search(str4)
	if result_d:
		print('old:' + str4)
		print('new:' + result_d.group())
		
	print('-----------.------findall---')	
	str5 = 'angaolaf12"34535235nvl<>aj,f.12/31[4v]lf"mlf'
	rule_d = re.compile(r'.')
	result_d = rule_d.findall(str5)
	if result_d:
		print('old:' + str5)
		print('new:' + str(result_d))
		
	print('-----------*-0或者更多-------')	
	str6 = 'angaolaf12"34535235nvl<>aj,f.12/31[4v]lf"mlf'
	rule_d = re.compile(r'\d*')
	result_d = rule_d.findall(str6)
	if result_d:
		print('old:' + str6)
		print('new:' + str(result_d))
		
	print('-----------+?-0或者更多(懒惰型)-------')	
	str6 = 'angaolaf12"34535235nvl<>aj,f.12/31[4v]lf"mlf'
	rule_d = re.compile(r'\d+?')
	result_d = rule_d.findall(str6)
	if result_d:
		print('old:' + str6)
		print('new:' + str(result_d))
		
	print('-----------+--1或者更多-------')	
	str7 = 'angaolaf12"34535235nvl<>aj,f.12/31[4v]lf"mlf'
	rule_d = re.compile(r'\d+')
	result_d = rule_d.findall(str7)
	if result_d:
		print('old:' + str7)
		print('new:' + str(result_d))
		
		
	print('-----------?---0个或1个--------')	
	str8 = 'angaolaf12"34535235nvl<>aj,f.12/31[4v]lf"mlf'
	rule_d = re.compile(r'\[?')
	result_d = rule_d.findall(str8)
	if result_d:
		print('old:' + str8)
		print('new:' + str(result_d))
		
	print('-----------{n}---n个------------')	
	str9 = 'angaolaf12"34535235nvl<>aj,f.12/31[4v]lf"mlf'
	rule_d = re.compile(r'\d{2}')
	result_d = rule_d.findall(str9)
	if result_d:
		print('old:' + str9)
		print('new:' + str(result_d))
		
	print('-----------{m,n}---m-n个------------')	
	str10 = 'angaolaf12"34535235nvl<>aj,f.12/31[4v]lf"mlf'
	rule_d = re.compile(r'\d{1,10}')
	result_d = rule_d.findall(str10)
	if result_d:
		print('old:' + str10)
		print('new:' + str(result_d))
		
	print('-----------[]---表示范围------------')	
	str11 = 'angaolaf12"34535235nvl<>aj,f.12/31[4v]lf"mlf'
	rule_d = re.compile(r'[ang]{1,3}')
	result_d = rule_d.findall(str11)
	if result_d:
		print('old:' + str11)
		print('new:' + str(result_d))
		
	print('-----------|---或-------------------')	
	str12 = 'angaolaf12"34535235nvl<>aj,f.12/31[4v]lf"mlf'
	rule_d = re.compile(r'(a|g)')
	result_d = rule_d.findall(str12)
	if result_d:
		print('old:' + str12)
		print('new:' + str(result_d))
		
	print('-----------^-开头--$-结尾------------')	
	str13 = 'angaolaf12"34535235nvl<>aj,f.12/31[4v]lf"mlf'
	rule_d = re.compile(r'^\w.*\w$')
	result_d = rule_d.findall(str13)
	if result_d:
		print('old:' + str13)
		print('new:' + str(result_d))
		
	print('-----------\s-空格-------------------')	
	str14 = 'anga o la   f12"34   53523 5nvl<>aj,f.12/31[4v]lf"mlf'
	rule_d = re.compile(r'\s+')
	result_d = rule_d.findall(str14)
	if result_d:
		print('old:' + str13)
		print('new:' + str(result_d))
		
	print('-----------"------------------------')	
	str15 = 'anga o la   f12"34   53523 5nvl<>aj,f.12/31[4v]lf"mlf'
	rule_d = re.compile(r'"')
	result_d = rule_d.findall(str15)
	if result_d:
		print('old:' + str15)
		print('new:' + str(result_d))
		
	print('-----------\b---匹配边界-------------')	
	str16 = 'i am a cat you are cattoo'
	rule_d = re.compile(r'\bcat\b')
	result_d = rule_d.findall(str16)
	if result_d:
		print('old:' + str16)
		print('new:' + str(result_d))
		
	
		
	
		
		
		