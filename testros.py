import rospy
from sensor_msgs.msg import NavSatFix
import threading
import pyrebase
# from __future__ import print_function
config = {
    "apiKey": "AIzaSyB9RkZFAwtJfZUXYvXZBb2S4GYVSzOkpjEv",
    "authDomain": "location-a26be.firebaseapp.com",
    "databaseURL": "https://location-a26be-default-rtdb.asia-southeast1.firebasedatabase.app",
    "storageBucket": "location-a26be.appspot.com"
    }

firebase = pyrebase.initialize_app(config)

db = firebase.database()

longitude = ""
latitude = ""

def talker():
    rospy.loginfo("Initialising GPS publishing")
    gps_pub=rospy.Publisher('/gps_new', NavSatFix, queue_size=1)
    rospy.init_node('talker', anonymous=True)
    rospy.sleep(3)
    rospy.loginfo("initialised")
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        gpsmsg=NavSatFix()
        gpsmsg.header.stamp = rospy.Time.now()
        gpsmsg.header.frame_id = "gps"
        rospy.loginfo("Hi!!!")
        gpsmsg.latitude=float(1.1111)
        gpsmsg.longitude=float(2.25555)
        # gpsmsg.latitude=float(latitude)
        # gpsmsg.longitude=float(longitude)
        gps_pub.publish(gpsmsg)
        rospy.loginfo(gpsmsg)
        rate.sleep()
        rospy.sleep(3)
def stream_handler(message):
		# global location_info 
    global latitude
    global longitude
    
    if message["path"] == '/location':
        location_info = str(message["data"])
    elif message["path"] == '/':
        # print((message["data"]["location"]))
        location_info = (str(message["data"]["location"]))

    location_sp = (location_info.split(","))
    latitude = float((location_sp[0].split(":"))[1])
    longitude = float(((location_sp[1].split(":"))[1]).split("}")[0])

    print(latitude,longitude) 

def run_pub():
    try:
        talker()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
    #  while True:
    #     print(1)
    #     time.sleep(3)


def run_firebase():
    db.stream(stream_handler)




# creating thread
t1 = threading.Thread(target=run_firebase)
t2 = threading.Thread(target=run_pub)

# starting thread 1
t1.start()
# starting thread 2
t2.start()

# wait until thread 1 is completely executed
t1.join()
# wait until thread 2 is completely executed
t2.join()

# both threads completely executed
print("Done!")

