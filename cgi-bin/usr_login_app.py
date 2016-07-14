#!/usr/bin/env python2

import cgi
import sys
sys.path.append("/usr/lib/python2.7/dist-packages/")
import MySQLdb
import sv_get_user
import sv_confirm_user

form = cgi.FieldStorage()
id = form["userId"].value
passwd = form["pass"].value

print ( id , passwd )

#id = 'test'
#passwd = 'test'

com = sv_confirm_user.confirmUsrClass()
result = com.confirmUser(id, passwd)

print (result)

if result :

	print("Content-type: text/html\n")
	html_body = """
	<!DOCTYPE html>
	<html>
	<meta http-equiv="refresh" content="0;URL=http://192.168.50.123:8080/">
	<body>
	</body></html>
	"""
	print(html_body.format())

else :
	print("Content-type: text/html\n")
	html_body = """
	<html><body>pass or userid is invalid </body></html>"""
	print(html_body.format())



