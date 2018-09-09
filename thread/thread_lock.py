import time
import threading

balance = 0

def change_it(n):
	global balance
	balance = balance + n
	balance = balance - n

#不加锁
'''	
def run_thread(n):
	for i in range(100000):
		change_it(n)
'''
#加锁
lock = threading.Lock()
def run_thread(n):
	for i in range(1000000):
		lock.acquire()#这里只有一个线程可以拿到锁，其他线程进行等待到拿到锁
		try:
			change_it(n)
		finally:#使用捕获异常的方式确保锁一定会被释放
			lock.release()
		
if __name__ == '__main__':
	
	#global balance#if并不会改变作用于，所有默认就是全局的作用域
	
	t1 = threading.Thread(target = run_thread, args = (5,))
	t2 = threading.Thread(target = run_thread, args = (6,))
	
	t1.start()
	t2.start()
	
	t1.join()
	t2.join()
	
	print(balance)