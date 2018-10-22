import shutil
import os

gloab_num = 50
gloab_char = "*"

if __name__ == '__main__':
	
	#change running dir
	try:
		os.makedirs('E:/python/python_learn/shutil/copyTest')
	except Exception as e:
		print(e)
	os.chdir('E:/python/python_learn/shutil/copyTest')
	
	#shutil.copy
	print('shutil.copy(src, des)'.center(gloab_num, gloab_char))
	try:
		str = shutil.copy('../shutil_copy.py', 'tmp.tmp')
	except Exception as e:
		print(e)
	print(str)
	
	#shutil.copytree 可递归创建
	print('shutil.copytree(src, des)'.center(gloab_num, gloab_char))
	try:
		str = shutil.copytree('../../os', './tmp/')
	except Exception as e:
		print(e)
	print(str)
	
	
