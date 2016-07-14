import sys
sys.path.append("/usr/lib/python2.7/dist-packages/")
import MySQLdb
import sv_get_user

class confirmUsrClass:

	def __init__(self):
		print ("confirmuser")

	def confirmUser(self, id, ps):
		usr = sv_get_user.getUsrClass()
		upass = usr.getPass(id)
		
		if ps == upass :
			return (True)
		else :
			return (False)
