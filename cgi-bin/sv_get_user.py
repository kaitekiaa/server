#!/usr/bin/env python2
import cgi
import sys
sys.path.append("usr/lib/python2.7/dist-packages/")
import MySQLdb

class getUsrClass:

	def __init__(self):
		print("getUsrClass")

	def getPass(self,id):
		connector = MySQLdb.connect(host="localhost",db="aquaplants",user="root",passwd="aquaplants",charset="utf8")
		cursor = connector.cursor()
		sql = "select * from user"
		cursor.execute(sql)
		records  = cursor.fetchall()
	#	print (records)
		upass = "NULL"
		for record in records:
			if record[0] == id:
				cursor.close()
				connector.close()
				return (record[2])	
		cursor.close()
		connector.close()
		return (upass)

	def getUserName(self,id):
		connector = MySQLdb.connect(host="localhost",db="aquaplants",user="root",passwd="aquaplants",charset="utf8")
		cursor = connector.cursor()
		sql = "select * from user"
		cursor.execute(sql)
		records  = cursor.fetchall()
#		print (records)
		uname = "NULL"
		for record in records:
			if record[0] == id:
				cursor.close()
				connector.close()
				return (record[1])	
		cursor.close()
		connector.close()
		return (uname)


	def getGroupId(self,id): #multi
		connector = MySQLdb.connect(host="localhost",db="aquaplants",user="root",passwd="aquaplants",charset="utf8")
		cursor = connector.cursor()
		sql = "select * from user"
		cursor.execute(sql)
		records  = cursor.fetchall()
	#	print (records)
		ugroup = ['NULL']
		for record in records:
			if record[0] == id:
				if ugroup[0] == 'NULL' :
					ugroup.remove('NULL')
				ugroup.append(record[3])
		
				
		cursor.close()
		connector.close()
		return (ugroup)
