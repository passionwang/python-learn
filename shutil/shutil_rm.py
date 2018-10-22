import os
import sys
import shutil

sys.path.append('E:/python/python_learn')
from pub import pub

if __name__ == '__main__':
	
	try:
		os.makedirs("E:/python/python_learn/shutil/rmTest")
	except Exception as e:
		print(e)
	os.chdir('E:/python/python_learn/shutil/rmTest')
	print("Test:删除指定路径下的文件".center(pub.gloab_num, pub.gloab_char))
	try:
		shutil.copy('../shutil_rm.py', './')
		shutil.copytree('../../project', './tmp')
	except Exception as e:
		print(e)
	try:	
		shutil.rmtree('E:/python/python_learn/shutil/rmTest/tmp')
	except Exception as e:
		print(e)