import subprocess

if __name__ == '__main__':
	'''
	子进程用于控制子进程的输入和输出
	'''
	print('$ nslookup www.python.org')
	r = subprocess.call(['nslookup', 'www.python.org'])
	print('Exit code:', r)
	
	
	print('$ nslookup')
	p = subprocess.Popen(['nslookup'], stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	output, err = p.communicate(b'set q=mx\npython.ort\nexit\n')
	print(output)
	print('Exit code:', p.returncode)
	