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
	
	print("Test".center(pub.gloab_num, pub.gloab_char))
	