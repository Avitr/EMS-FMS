#!/usr/bin/python
import MySQLdb
import MySQLdb.cursors

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="john",         # your username
                     passwd="megajonhy",  # your password
                     db="jonhydb"       # name of the data base
                     cursorclass=MySQLdb.cursors.DictCursor)

# you must create a Cursor object. It will let
#  you execute all the queries you need

cur = db.cursor()

tab1=cur.execute("SELECT loc_id, curr_status FROM Table1 WHERE curr_status<0")
tab1 = cur.fetchall()



tab2=cur.execute("SELECT drive_id, driv_status FROM Table2 WHERE driv_status<0")
tab2 = cur.fetchall()


for i in tab1:
	bool p=true
    for j in tab2:
        if i[1]<0 and j[1]<0:
        	i[1]=j[0]
        	j[1]=i[0] 
        	p=false
        	#We have to send signal here 
    if p===true:
    	#for Extra grid and we could not find driver
    	#make them point towards nearest driver by location


#if the driver got any call from patient we will get driver id by  driver itself
temp=cur.execute("SELECT drive_id, driv_status FROM Table2 WHERE driv_id==x")
temp = cur.fetchone()

for i in temp:
    temp2=cur.execute("SELECT loc_id, curr_status FROM Table1 WHERE curr_status=drive_id")
    temp2 = cur.fetchall()
    for j in temp2
        i[1]=-100
        j[1]=-100


temp1=cur.execute("SELECT loc_id, curr_status FROM Table1 WHERE cur")
temp1 = cur.fetchall()













db.close()