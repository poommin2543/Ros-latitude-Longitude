#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import NavSatFix
import pyrebase

config = {
  "apiKey": "AIzaSyB9RkZFAwtJfZUXYvXZBb2S4GYVSzOkpjEv",
  "authDomain": "location-a26be.firebaseapp.com",
  "databaseURL": "https://location-a26be-default-rtdb.asia-southeast1.firebasedatabase.app",
  "storageBucket": "location-a26be.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
location_info = ""


class publishGPS(object):
	def __init__(self):
		rospy.loginfo("Initialising GPS publishing")
		# self.gps_sub=rospy.Subscriber('/GPS_talker_1',String, self.callback, queue_size=1)
		self.lastMsg=None
		self.gps_pub=rospy.Publisher('/gps_new', NavSatFix, queue_size=1)
		rospy.sleep(3)
		rospy.loginfo("initialised")

	# def callback(self, data):
	# 	self.lastMsg=data

	def stream_handler(self,message):
		global location_info 
		if message["path"] == '/location':
			location_info = str(message["data"])
		elif message["path"] == '/':
			# print((message["data"]["location"]))
			location_info = (str(message["data"]["location"]))
		# print(location_info)
	# print(location_info)

	def do_work(self):
		
		# self.splitStrings= str(self.lastMsg).split(",")
		db.stream(self.stream_handler)
		# print(f'location_info : {type(location_info)}')

		# print(location_info['latitude'])
		if location_info == "":
			pass
		else:
			location_sp = (location_info.split(","))
			latitude = float((location_sp[0].split(":"))[1])
			longitude = float(((location_sp[1].split(":"))[1]).split("}")[0])
			print(latitude,longitude)
			
			gpsmsg=NavSatFix()
			gpsmsg.header.stamp = rospy.Time.now()
			gpsmsg.header.frame_id = "gps"
			rospy.loginfo("Hi!!!")
			# gpsmsg.latitude=float(1.1111)
			# gpsmsg.longitude=float(2.25555)
			gpsmsg.latitude=float(latitude)
			gpsmsg.longitude=float(longitude)
			self.gps_pub.publish(gpsmsg)

	def run(self):
		r=rospy.Rate(1)
		while not rospy.is_shutdown():
			self.do_work()
			r.sleep()

if __name__=='__main__':
	rospy.init_node('pubgps')
	obj=publishGPS()
	obj.run()
    
    