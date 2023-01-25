# -- coding: utf-8 --
file = open('C:\\Users\\devarl\\Documents\\GitHub\\--22\\test.txt',  'r') 
i=file.read() 
from random import random as r
n,k=map(int,(i).split())
k-=1; b=range(n)
a=[[r() for j in b] for i in b]; print(a)
for j in b: a[k][j]/=a[k][k]
file = open('C:\\Users\\devarl\\Documents\\GitHub\\--22\\test2.txt',  'w')
file.write(str(a))
file.close()
