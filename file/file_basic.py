#import os

if __name__ == '__main__':
	
	print('-------------------file--TEST-----------------')
	
	print('-------------------basic-----------------------')
	
	#local_path = os.getcwd()
	#print(local_path)
	f = open('E:python_learn\\file\\file_text', 'r') 
	str = f.read()
	f.close()
	print(str)
	
	f = open('E:python_learn\\file\\file_text', 'a')
	f.write('\n11')
	f.close()
	
	f = open('E:python_learn\\file\\file_text', 'r')
	str = f.read()
	f.close()
	print(str)
	
	print('-------------------except----------------------')
	
	try:
		f = open('E:python_learn\\file\\file_text', 'r')
		print(f.read())
	finally:
		if f:
			print(f)
			f.close()
	
	print('-------------------with------------------------')
	
	with open('E:python_learn\\file\\file_text', 'r') as f:
		print(f.read())
		
	print('-------------------read(size)------------------')
	
	with open('E:python_learn\\file\\file_text', 'r') as f:
		print(f.read(15))
		
	print('-------------------readline()------------------')
	
	with open('E:python_learn\\file\\file_text', 'r') as f:
		str = f.readline()
		str1 = f.readline()
		str2 = f.readline()
		print(str)
		print(str1)
		print(str2)
		
	print('------------------readlines()-----------------')
	
	with open('E:python_learn\\file\\file_text', 'r') as f:
		new_str = ''
		str = f.readlines()
		print(str)
		for i in str:
			if 'hahahaha' in i:
				new_str += i.replace('hahahaha', 's')
			else:
				new_str += i
		print(new_str)
		
	with open('E:python_learn\\file\\file_text', 'w') as f:
		f.write(new_str)
	
	print('----------------encoding----------------------')
	
	with open('E:python_learn\\file\\file_text', 'r', encoding = 'utf8', errors = 'ignore') as f:
		print(f.readlines())
	