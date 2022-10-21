#!/usr/bin/env python

import threading

import rospy
from std_msgs.msg import String

def callback(msg):
    print("Msg from %s on thread %s" % (msg.data, threading.current_thread()))

def main():
    rospy.init_node('foooo')
    rospy.Subscriber('foo', String, callback, queue_size=1)
    rospy.spin()

if __name__ == '__main__':
    main()