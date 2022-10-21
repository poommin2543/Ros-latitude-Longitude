#!/usr/bin/env python

from colorsys import yiq_to_rgb
import threading
import sys

import rospy
from std_msgs.msg import String



def publisher():
    msg = String("proc_id")
    r = rospy.Rate(1)
    pub = rospy.Publisher('foo', String, queue_size=1)
    while not rospy.is_shutdown():
        print("publishing")
        pub.publish(msg)
        r.sleep()
def x():
    for i in range (0,1000000000):
        print(i)
def y():
    for i in range (0,1000000000):
        print(f"{i}+++++")
def main():
   
    rospy.init_node("proc_id")
    thread = threading.Thread(target=publisher)
    thread1 = threading.Thread(target=y)
    thread.start()
    thread1.start()
    thread.join()
    thread1.join()
    rospy.spin()
    

if __name__ == '__main__':
    main()