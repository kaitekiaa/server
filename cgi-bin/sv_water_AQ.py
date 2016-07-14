#!/usr/bin/env python2
import cgi
import sys
sys.path.append("/usr/lib/python2.7/dist-packages/")
import MySQLdb
import sv_get_user
import sv_search_aquaplant
import datetime

form = cgi.FieldStorage()
uid=form["userId"].value
gid=form["groupId"].value

u = sv_get_user.getUsrClass()
group = u.getGroupId(uid)

flag = False

for i in group:
	if i == gid:
		flag = True

if flag :
	ip="NULL"
	ap = sv_search_aquaplant.searchAPIpClass()
	ip = ap.searchAPIp(gid)
#	print (ip)

	if ip == "NULL" :
		flag = False

if flag :

	print("Content-type: text/html\n")
	print("<html><meta http-equiv='refresh' content='10;URL=http://")
	print(ip)
	print("/cgi-bin/pi_light.html")
	print("'><body>")
	print("mizuagetayade")
	print(ip)
	print("</body></html>")

else :

	print("Content-type: text/html\n")
	print("<html><body>")
	print("miss")
	print("</body></html>")
