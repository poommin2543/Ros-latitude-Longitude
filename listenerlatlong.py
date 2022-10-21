import rospy
from std_msgs.msg import String


import pyrebase

config = {
  "apiKey": "AIzaSyB9RkZFAwtJfZUXYvXZBb2S4GYVSzOkpjEv",
  "authDomain": "location-a26be.firebaseapp.com",
  "databaseURL": "https://location-a26be-default-rtdb.asia-southeast1.firebasedatabase.app",
  "storageBucket": "location-a26be.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

pub = rospy.Publisher('LatLongUser', String, queue_size=10)
rospy.init_node('talker', anonymous=True)
rate = rospy.Rate(10) # 10hz


def talker(data):
    # hello_str = data + " %s" % rospy.get_time()
    # rospy.loginfo(hello_str)
    rospy.loginfo(type(dict(data)))

    pub.publish(data)
    rate.sleep()

def stream_handler(message):
    # print(message["event"]) # put
    # print(message["path"]) # /air
    # print(message["data"]) # ON or OFF
    # print(message)
    if message["path"] == '/location':
        # print((message["data"]))
        talker(str(message["data"]))
    elif message["path"] == '/':
        # print((message["data"]["location"]))
        talker(str(message["data"]["location"]))

if __name__ == '__main__':
    try:
        # talker("Start")
        my_stream = db.stream(stream_handler)
        # stream_handler() 
    except rospy.ROSInterruptException:
        pass
