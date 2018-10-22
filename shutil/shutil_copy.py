import shutil
import os

gloab_num = 50
gloab_char = "*"

if __name__ == '__main__':
	
	#change running dir
	os.chdir('E:/python/python_learn/shutil')
	
	#shutil.copy
	print('shutil.copy(src, des)'.center(gloab_num, gloab_char))
	str = shutil.copy('shutil_copy.py', 'tmp.tmp')
	print(str)
	
	print('shutil.copytree(src, des)'.center(gloab_num, gloab_char))
	str = shutil.copytree('../shutil', './tmp')
	print(str)
