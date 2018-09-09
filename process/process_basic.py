from multiprocessing import Process
import os

def run_proc(name):
	print('Run child process %s (%s)...' % (name, os.getpid()))
	
if __name__ == '__main__':
	
	print('Parent process %s.' % os.getpid())
	p = Process(target = run_proc, args = ('test',))
	print('Child process will start ...')
	p.start()#用于启动子进程
	p.join()#等待子进程执行完成后再继续向下执行，用于进程间同步
	print('Child process end.')
	
