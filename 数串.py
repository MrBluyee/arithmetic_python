# -*- coding: UTF-8 -*-

__author__ = 'Mr.Bluyee'

import itertools

def main():
	n = input()
	n_l = input().split()
	n_l = [int(''.join(i)) for i in itertools.permutations(n_l,int(n))]
	n_l.sort(reverse = True)
	print(n_l[0])
	
	
if __name__ == '__main__':
	main()