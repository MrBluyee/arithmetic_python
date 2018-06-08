# -*- coding: UTF-8 -*-

__author__ = 'Mr.Bluyee'

from itertools import islice

def fib1(max):
	prev,cur,n = 0,1,0
	while n < max:
		yield cur
		prev,cur = cur,prev + cur
		n += 1
	return 'done'

def fib2():
	prev,cur = 0,1
	while True:
		yield cur
		prev,cur = cur,prev + cur
		
def main():
	for i in fib1(6):
		print(i)
		
	print(list(islice(fib2(),0,6)))
	
if __name__ == '__main__':
	main()