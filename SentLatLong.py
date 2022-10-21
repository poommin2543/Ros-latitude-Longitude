import pyrebase
import rospy
from std_msgs.msg import String
import ast
config = {
  "apiKey": "AIzaSyB9RkZFAwtJfZUXYvXZBb2S4GYVSzOkpjEv",
  "authDomain": "location-a26be.firebaseapp.com",
  "databaseURL": "https://location-a26be-default-rtdb.asia-southeast1.firebasedatabase.app",
  "storageBucket": "location-a26be.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    # print(data.data)
    res = ast.literal_eval(data.data)
    # print(res["latitude"])
    # print(res["longitude"])
    data = {
    "latitude": res["latitude"],
    "longitude": res["longitude"]
    }
    results = db.child("locationCar").update(data)
    print(results)


def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('LatLongUser', String, callback)
    rospy.spin()



if __name__ == '__main__':
    listener()