import shutil
import sys
import os


sys.path.append('E:/python/python_learn')
from pub import pub

if __name__ == '__main__':
	
	#change running dir
	try:
		os.makedirs('E:/python/python_learn/shutil/moveTest')
	except Exception as e:
		print(e)
	os.chdir('E:/python/python_learn/shutil/moveTest')
	
	#移动文件
	print("Test：移动文件".center(pub.gloab_num, pub.gloab_char))
	try:
		shutil.copy('../../os/os_path.py', '../../os/os_path1.py')
		shutil.move('../../os/os_path1.py', './')
		print('移动文件成功')
	except Exception as e:
		print(e)
		
	#改名
	print('Test: 改名'.center(pub.gloab_num, pub.gloab_char))
	try:
		shutil.move('os_path1.py', 'os_rename.py')
		print('改名成功')
	except Exception as e:
		print(e)
		
	#移动文件夹，文件夹不存在会创建
	print('Test:移动文件夹'.center(pub.gloab_num, pub.gloab_char))
	try:
		shutil.copytree('../../project', '../../project1')
		shutil.move('../../project1', './egg/egg/')
	except Exception as e:
		print(e)
		