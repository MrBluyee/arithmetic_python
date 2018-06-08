# -*- coding: UTF-8 -*-

__author__ = 'Mr.Bluyee'

from itertools import islice

class Fib:
	def __init__(self):
		self.prev = 0
		self.cur = 1
		
	def __iter__(self):
		return self
		
	def __next__(self):
		value = self.cur
		self.cur += self.prev
		self.prev = value
		return self.prev
		
		
def fib(max):
	return list(islice(Fib(),0,max))
	
def main():
	print(fib(10))
	
if __name__ == '__main__':
	main()