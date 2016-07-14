#!/usr/bin/env python2
import cgi
import sys
sys.path.append("usr/lib/python2.7/dist-packages/")
import MySQLdb

class getGroupClass:

	def __init__(self):
		print("getGroupClass")

	def getGroupName(self,id):
		connector = MySQLdb.connect(host="localhost",db="aquaplants",user="root",passwd="aquaplants",charset="utf8")
		cursor = connector.cursor()
		sql = "select * from aquaplants.group;"
		cursor.execute(sql)
		records  = cursor.fetchall()
#		print (records)
		gname = "NULL"
		for record in records:
			if record[0] == id:
				cursor.close()
				connector.close()
				return (record[1])	
		cursor.close()
		connector.close()
		return (gname)


	def getPlantId(self,id): #multi
		connector = MySQLdb.connect(host="localhost",db="aquaplants",user="root",passwd="aquaplants",charset="utf8")
		cursor = connector.cursor()
		sql = "select * from aquaplants.group"
		cursor.execute(sql)
		records  = cursor.fetchall()
	#	print (records)
		plant = "NULL"
		for record in records:
			if record[0] == id:
				cursor.close()
				connector.close()
				return (record[2])
		cursor.close()
		connector.close()
		return (plant)
