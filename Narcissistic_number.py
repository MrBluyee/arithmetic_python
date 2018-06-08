# -*- coding: UTF-8 -*-

__author__ = 'Mr.Bluyee'

def split_num(num):
	return [int(i) for i in str(num)]

def is_narcissistic_number(num):
	l = split_num(num)
	sum = 0
	for i in l:
		sum += i**len(l)
	if sum == num:
		return num
	else:
		return -1
		
def find_narcissistic_numbers(m,n):
	return [i for i in range(m,n+1) if is_narcissistic_number(i) != -1]
	
def main():
	s = input('please input two numbers:')
	l = s.split()
	print(find_narcissistic_numbers(int(l[0]),int(l[1])))
	
if __name__ == '__main__':
	main()