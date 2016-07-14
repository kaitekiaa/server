#!/usr/bin/env python2
import cgi
import sys
sys.path.append("usr/lib/python2.7/dist-packages/")
import MySQLdb

class getAquaplantClass:

	def __init__(self):
		print("getGroupClass")

	def getMode(self,id):
		connector = MySQLdb.connect(host="localhost",db="aquaplants",user="root",passwd="aquaplants",charset="utf8")
		cursor = connector.cursor()
		sql = "select * from aquaplants.aquaplant"
		cursor.execute(sql)
		records  = cursor.fetchall()
#		print (records)
		mode = "NULL"
		for record in records:
			if record[0] == id:
				cursor.close()
				connector.close()
				return (record[2])	
		cursor.close()
		connector.close()
		return (mode)


	def getIP(self,id): 
		connector = MySQLdb.connect(host="localhost",db="aquaplants",user="root",passwd="aquaplants",charset="utf8")
		cursor = connector.cursor()
		sql = "select apId, INET_NTOA(Ip) from aquaplant"
		cursor.execute(sql)
		records  = cursor.fetchall()
	#	print (records)
		ip = "NULL"
		for record in records:
			if record[0] == id:
				cursor.close()
				connector.close()
				return (record[1])
		cursor.close()
		connector.close()
		return (ip)
