import shelve
import os

gloab_num = 50
gloab_char = '*'

if __name__ == '__main__':
	
	print('test shelve read'.center(gloab_num, gloab_char))
	#change runing dir
	os.chdir('E:python/python_learn/shelve')
	shelfile = shelve.open('mydata')
	print(shelfile.keys())
	for k,v in shelfile.items():
		# print('%s:%s' % (k, shelfile[k]))
		print('%s:%s' % (k, v))
		# pass
	print(shelfile['cats'])
	shelfile.close()
	print('read finished')