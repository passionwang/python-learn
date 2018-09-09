from multiprocessing import Process
from multiprocessing import Queue
import os
import time
import random

#写数据进程执行的代码
def write(q):
	print('Process to write : %s' % os.getpid())
	for value in ['A', 'B', 'C']:
		print('Put %s to queue...' % value)
		q.put(value)
		time.sleep(random.random())
		
		
#读数据进程执行的代码
def read(q):
	print('Process to read ：%s' % os.getpid())
	while(True):
		value = q.get(True)
		print("Get %s from queeu." % value)
		
if __name__ == '__main__':
	
	#父进程创建queue，并开始各个进程：
	q = Queue()
	pw = Process(target = write, args = (q,))
	pr = Process(target = read, args = (q,))
	pw.start()
	pr.start()
	pw.join()
	pr.terminate()#强行停止
	