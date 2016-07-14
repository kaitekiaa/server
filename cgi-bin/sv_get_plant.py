#!/usr/bin/env python2
import cgi
import sys
sys.path.append("usr/lib/python2.7/dist-packages/")
import MySQLdb

class getPlantClass:

	def __init__(self):
		print("getUsrClass")

	def getPlantName(self,id):
		connector = MySQLdb.connect(host="localhost",db="aquaplants",user="root",passwd="aquaplants",charset="utf8")
		cursor = connector.cursor()
		sql = "select * from plant"
		cursor.execute(sql)
		records  = cursor.fetchall()
#		print (records)
		apname = "NULL"
		for record in records:
			if record[0] == id:
				cursor.close()
				connector.close()
				return (record[1])	
		cursor.close()
		connector.close()
		return (apname)


	def getAPId(self,id): 
		connector = MySQLdb.connect(host="localhost",db="aquaplants",user="root",passwd="aquaplants",charset="utf8")
		cursor = connector.cursor()
		sql = "select * from plant"
		cursor.execute(sql)
		records  = cursor.fetchall()
	#	print (records)
		apid = "NULL"
		for record in records:
			if record[0] == id:
				cursor.close()
				connector.close()
				return (record[2])
		cursor.close()
		connector.close()
		return (apid)

	def getDate(self,id): 
		connector = MySQLdb.connect(host="localhost",db="aquaplants",user="root",passwd="aquaplants",charset="utf8")
		cursor = connector.cursor()
		sql = "select * from plant"
		cursor.execute(sql)
		records  = cursor.fetchall()
	#	print (records)
		date = "NULL"
		for record in records:
			if record[0] == id:
				cursor.close()
				connector.close()
				return (record[3])
		cursor.close()
		connector.close()
		return (date)
