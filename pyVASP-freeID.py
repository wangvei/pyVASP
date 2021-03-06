#!/usr/bin/env python
## Application: List free JobID from SQL server 
## Written by:  Asst.Prof.Dr. Kittiphong Amnuyswat
## Updated:	    01/04/2020

import os
import sys
import datetime
import time
import pandas as pd

import platform
if platform.system() == 'Darwin' or 'Linux' :
    sys.path.append('/Volumes/GoogleDrive/My Drive/Python')
    os.system('clear')
print("Current date and time: ", datetime.datetime.now().strftime("%d-%m-%Y %H-%M-%S"))
print("")


######################### Opening DB connection #########################
import pymysql.cursors
import sql
connection = pymysql.connect(host = sql.host,
                             user = sql.user,
                             password = sql.password,
                             db = sql.db,
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)

with connection.cursor() as cursor:
    sql = "select `JobID` from `INCAR`"
    cursor.execute(sql)
    result = cursor.fetchall()
connection.commit()
os.system('clear')
connection.close()


jobid = pd.DataFrame.from_dict(result)
total = jobid.shape[0]
maxid = int(jobid.iloc[total-1])

min = int(input("Minimum no."))
max = int(input("Maximum no."))

for i in range(min,max+1) :
    if i not in jobid.values :
        print(i)