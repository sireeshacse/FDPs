# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 21:55:57 2020

@author: Sireesha Rodda
"""

######Program 1: Character frequency in a string#######
str="sireesha"
for char in str:
    print(char,str.count(char))
    
######Program 2: Is a list empty or not#########
alist=[1,2,3]
blist=[]
isListEmpty=lambda x:len(x)==0
print(isListEmpty(alist))
print(isListEmpty(blist))

######Program 3:Find biggest among three numbers######
a=10
b=20
c=30
if(a>=b):
    if(a>=c):
        print("a is largest")
    else:
        print("c is largest")
else:
    if(b>=c):
        print("b is largest")
    else:
        print("c is largest")
        
######Program 4: Display Unique elements in a list#########
alist=[10,10,20,20,20,30]
print(alist)
aset=set(alist)
print("The unique elements are",aset)


######Program 5:Number of even and odd numbers in provided list#########
alist = [ 56,34,23,56,4,43,6,7,5,34,5,7645,573,23,6,7,5,4,6,7,5634,3454,345,67,32,45]
evens=[]
odds=[]
for n in alist:
    if n%2==0:
        evens.append(n)
    else:
        odds.append(n)
print("Even numbers are",evens)
print("odd numbers are",odds)

#####Program 6:display numbers from 50 to 1####
for i in range(50,0,-1):
    print(i,end=" ")
    
#####Program 7: odd numbers from 20 to 10#####
print("\nodd numbers from 20 down to 10")
for i in range(20,10,-1):
    if(i%2==1):print(i,end=" ")