#!/usr/bin/python
# -*- coding: utf-8 -*-

import mysql.connector

mydb = mysql.connector.connect(
  host="mysqldbinst1.cou0izjnusjt.us-east-1.rds.amazonaws.com",
  user="root",
  passwd="Test1234#"
)

print(mydb)

cursor = mydb.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT * FROM sakila.actor")

if 5 > 2:
	print("Five is greater than two!")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
while data is not None:
   print(data)
   data = cursor.fetchone()

# disconnect from server
mydb.close()
print("done")