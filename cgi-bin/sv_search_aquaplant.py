import sys
sys.path.append("/usr/lib/python2.7/dist-packages/")
import MySQLdb
import sv_get_group
import sv_get_plant
import sv_get_aquaplant

class searchAPIpClass:

	def __init__(self):
		print ("confirmuser")

	def searchAPIp(self, gid):
		pi = 'NULL'
		g = sv_get_group.getGroupClass()
		pid = g.getPlantId(gid)		
		p = sv_get_plant.getPlantClass()
		apid = p.getAPId(pid)
		ap = sv_get_aquaplant.getAquaplantClass()
		ip = ap.getIP(apid)

		print (ip)

		return (ip)
