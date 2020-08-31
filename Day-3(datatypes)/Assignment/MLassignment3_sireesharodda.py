# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 22:38:08 2020

@author: sireesha

Day 3 Assignment
"""

#######Program1:count numbr of chars in a string############
astring="sireesha"
query="Number of characters in the string: {0} is {1}"
print(query.format(astring,len(astring)))

#####Program 2:String methods#############
alist="sireesha"
print(alist.lower())
print(alist.upper())
print(alist.isupper())
print(alist.islower())
print(alist.split("r"))
print(alist.capitalize())
print(alist.center(50))
print(alist.center(50,'*'))
#######Program 3: list methods###########
alist=[1,2,3,0,-1,-10]
alist.append(20)
print(alist)
alist.extend([5,6,7,8])
print(alist)
alist.insert(0,200)
print(alist)
alist.pop()
print(alist)
alist.pop(1)
print(alist)
alist.remove(0)
print(alist)
alist.sort()
print(alist)
alist.reverse()
print(alist)
alist.sort(reverse=True)

##########Program 4: dictionary methods#######
fdp={"day1":"intro","day2":"pandas","day3":"datatypes"}
print(fdp.keys())
print(fdp.values())
print(fdp.items())
print(fdp.get("day2"))
dict1={"day4":"functions"}
fdp.update(dict1)
print(fdp)

#######Program 5: Set methods##########
s={"apple","banana"}
print(s)
s.add("orange")
print(s)
s.update(["grapes","cherries"])
print(s)
print(len(s))
s.add("apple")
print(s)
s.remove("apple")
print(s)
s.discard("kiwi")
s.pop()
print(s)
s.clear()
print(s)
del s
