#!/usr/bin/env python3
 
#Importing needed modules of PyMySQL
from pymysql import connect, err, sys, cursors
from random import randint
 
#Doing our connection
conn = connect( host = 'localhost',
                        port = 3306,
                        user = 'root',
                        passwd = 'ballfilm@44',
                        db = 'niu_res' );
cursor = conn.cursor( cursors.DictCursor );
 
#Running a query easily
while True:
    cursor.execute( "INSERT INTO accel_data(x_val, y_val, z_val) VALUES (%s, %s , %s)"%(str(randint(0,9)), str(randint(0,9)), str(randint(0,9))))
    conn.commit()
#cursor.execute("select * from accel_data")
#data = cursor.fetchall()
#print(data)

