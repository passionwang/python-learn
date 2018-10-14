import os

gloab_num = 50
gloab_char = '*'

if __name__ == '__main__':
	
	"""
	一些关于os模块的操作，主要path相关
	os.path:
	https://docs.python.org/3/library/os.path.html
	"""
	#os.system()在本机执行命令行，返回结果成功0或失败1
	print('os.system()'.center(gloab_num, gloab_char))
	output = os.system('dir')
	print(output)
	
	#os.getcwd()获得当前目录
	print('os.getcwd()'.center(gloab_num, gloab_char))
	path = os.getcwd()
	print(path)
	
	#os.chdir()切换当前目录
	print('os.chdir()'.center(gloab_num, gloab_char))
	path = os.getcwd()
	print('原来的目录：' + path)
	try:
		os.chdir('E:/python\\python_learn')
	except Exception as e:
		print(e)
	# os.system('dir')
	path = os.getcwd()
	print('切换后的目录：' + path)
	
	#os.path.join()将目录合并
	print('os.path.join()'.center(gloab_num, gloab_char))
	path = os.path.join('C:\\usr', 'wang', 'biao')
	print(path)
	
	#os.makedirs()创建新的目录
	print('os.makedirs()'.center(gloab_num, gloab_char))
	#创建一个目录
	dir = 'E:/python/testdir'
	try:
		os.makedirs(dir)
	except Exception as e:
		print(e)
	#创建相同的目录
	try:
		os.makedirs(dir)
	except Exception as e:
		print(e)
	
	#os.path.abspath()获得输入路径的绝对路径
	print('os.path.abspath()'.center(gloab_num, gloab_char))
	abs_path = os.path.abspath('.')
	print(abs_path)
	
	#os.path.isabs()判断输入路径是否是绝对路径
	print('os.path.isabs()'.center(gloab_num, gloab_char))
	b_result = os.path.isabs('.')
	print(b_result)
	b_result = os.path.isabs(os.path.abspath('.'))
	print(b_result)
	
	