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
	
	#os.path.relpath(path, start)将返回从start路径到path的相对路径的字符串
	print('os.path.relpath()'.center(gloab_num, gloab_char))
	os.chdir('E:/python\\python_learn')
	relpath = os.path.relpath('E:/python\\python_learn', 'E:/python')
	print(relpath)
	
	#分割一个完全的路径信息
	print('分割信息：'.center(gloab_num, gloab_char))
	str = 'E:\\python\\python_learn\\os\\os_path.py'
	print(str)
	dir = os.path.dirname(str)
	print(dir)
	name = os.path.basename(str)
	print(name)
	tuple_dir_name = os.path.split(str)
	print(tuple_dir_name)
	tuple_sep = str.split(os.path.sep)
	print(tuple_sep)
	
	#获得文件大小和列表
	print('os.path.getsize()'.center(gloab_num, gloab_char))
	size = os.path.getsize(str)
	print(size)
	print('os.listdir()'.center(gloab_num, gloab_char))
	str = 'E:\\python\\python_learn\\os'
	list_info = os.listdir(str)
	print(list_info)
	
	#判断是否存在
	print('os.path.exists()'.center(gloab_num, gloab_char))
	print(os.path.exists('C:/Windows'))
	print(os.path.isdir('C:/Windows'))
	print(os.path.isfile('E:\\python\\python_learn\\os\\os_path.py'))