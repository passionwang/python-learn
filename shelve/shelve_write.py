import shelve
import os

gloab_num = 50
gloab_char = '*'

if __name__ == '__main__':

	print('Test shelve write'.center(gloab_num, gloab_char))
	#change runing dir
	os.chdir('E:python/python_learn/shelve')
	shelfile = shelve.open('mydata')
	cats = ['cat', 'dog', 'tiger']
	shelfile['cats'] = cats
	shelfile.close()
	print('write finished')