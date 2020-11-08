#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist

def forward():
    pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10 )
    rospy.init_node('forward', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    vel_msg = Twist()
    # parameter
    kecepatan = input("Masukkan kecepatan: ")
    jarak = input("Masukkan jarak: ")

    vel_msg.linear.x = abs(kecepatan)
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0


    while not rospy.is_shutdown():
        # kalkulasi waktu dan jarak
        t0 = rospy.Time.now().to_sec()
        jarak_sekarang = 0

        # looping pergerakan dalam jarak
        while(jarak_sekarang < jarak):
            # publish kecepatan
            pub.publish(vel_msg)
            # ambil waktu sekarang 
            t1 = rospy.Time.now().to_sec()
            # kalkulasi jarak
            jarak_sekarang = kecepatan*(t1-t0)
        # kecepatan 0 
        vel_msg.linear.x = 0
        # paksa henti
        pub.publish(vel_msg)



if __name__ == '__main__':
    try:
        forward()
    except rospy.ROSInterruptException:
        pass