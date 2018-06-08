# -*- coding: UTF-8 -*-

__author__ = 'Mr.Bluyee'

def triangles(lines):
	l = [1]
	line = 1
	while line < lines:
		yield l
		l = [1] + [l[i-1] + l[i] for i in range(1,len(l))] + [1]
		line += 1
	return 'done'
	
def main():
	t = triangles(6)
	for i in t:
		print(i)
	
if __name__ == '__main__':
	main()