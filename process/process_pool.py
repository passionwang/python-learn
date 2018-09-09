from multiprocessing import Pool
import os
import time
import random

def long_time_task(name):
	print('Run task %s (%s)...' % (name, os.getpid()))
	start = time.time()
	time.sleep(random.random() * 5)
	end = time.time()
	print('Task %s runs %0.2f seconds' % (name, (end - start)))
	
if __name__ == '__main__':
	print('Parent process %s.' % os.getpid())
	p = Pool(4)
	for i in range(5):
		p.apply_async(long_time_task, args = (i,))
	print('Waiting for all subprocess done ...')
	p.close()#调用后不能继续添加新的process
	p.join()#等待所有子进程执行完成，先调用close，close之后就不能继续添加新的进程了
	print('All subprocess done.')