# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 05:27:09 2020

@author: user
"""

##############PROGRAM 1###################
#Write a program to read realestate.csv and insert all the records
#( all columns) to the database
#( first create table structure with all the columns in the 
 #realestate.csv file )
#########################################
import pymysql
import csv
try:
    db=pymysql.connect(host='localhost',port=3306,user='root',password='sireesha',database='jntuk')
    print(db)
    cursor=db.cursor()
    with open('D:/dept/webinars/JNTUK aug 2020/Day-6(try _exception)/Material/17082020/realestate (12).csv','r') as fobj:
       reader=csv.reader(fobj)
       for line in reader:
           query="insert into realestate values('{}','{}').format(line[0],line[1])"
           cursor.execute(query)
           db.commit()
    db.close()
except pymysql.DatabaseError as err:
    print("Database error:",err)
except pymysql.OperationalError as err:
    print(err,": related to Database operations")
except pymysql.IntegrityError as err:
    print(err,":related to keys")
except Exception as err:
    print(err)
    
#################PROGRAM 2##################
#Write a Python program to display all the files and folders 
#separately and its count also.
############################################
import os
print("files_count:",len(os.listdir('D:/')))
print(os.listdir('D:/'))

#################PROGRAM 3##################
#Write a Python program to display the below information.

#display the current user name
#display current working directory
#display Operating system name
#display process id of your running program
#display the current timestamp
#display yesterday’s date
#display tomorrow’s date
#display all the environment variables that are existing
#display the python executable path ( just like ‘which python3’ in Linux )

############################################


import os
import time
import getpass
print(getpass.getuser())  #get userid
print(os.getcwd()) #current working directory (absolute path)
print(os.name)     #name of the operating system
print(os.getpid()) #process id
print(time.time())  #current time stamp
import datetime
print(datetime.datetime.now().timestamp())  #anotherway to print timestamp
print("yesterday was:",datetime.date.today()-datetime.timedelta(days=1))
print("tomorrow will be:",datetime.date.today()+datetime.timedelta(days=1))

#user's environment variables
import os
print(os.environ)

#python executable path
import sys
print(sys.executable)