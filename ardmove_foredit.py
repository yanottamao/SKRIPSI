#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist


def kecepatandefault():
    global kecepatan = input('Masukkan kecepatan antara 0.1 - 1: ')
    return kecepatan


def modeterbang():
    print('Pilihan mode terbang:')
    print('1. Take off / terbang')
    print('2. Land / mendarat')
    print('3. Mode masukan arah')
    global mode
    modeinput = int(input('Masukkan mode terbang: '))
    if modeinput == 1:
        mode = 'ardrone/takeoff'
    elif modeinput == 2:
        mode = 'ardrone/land'
    elif modeinput == 3:
        mode = '/cmd_vel'
    else:
        print('Pilih antara pilian diatas!')
        modeterbang()


def takeoff():
    pub = rospy.Publisher('ardrone/takeoff', Empty, queue_size=10)
    rospy.init_node('takeoff', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    while not rospy.is_shutdown():
        pub.publish(Empty())
        rate.sleep()


def land():
    pub = rospy.Publisher('ardrone/land', Empty, queue_size=10)
    rospy.init_node('land', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    while not rospy.is_shutdown():
        pub.publish(Empty())
        rate.sleep()


def forward():
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.init_node('forward', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    vel_msg = Twist()
    # parameter
    kecepatan = input('Masukkan kecepatan: ')
    jarak = input('Masukkan jarak')

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


def backward():
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.init_node('backward', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    vel_msg = Twist()
    # parameter
    kecepatan = input('Masukkan kecepatan: ')
    jarak = input('Masukkan jarak')

    vel_msg.linear.x = -abs(kecepatan)
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


def toleft():
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.init_node('toleft', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    vel_msg = Twist()
    # parameter
    kecepatan = input('Masukkan kecepatan: ')
    jarak = input('Masukkan jarak')

    vel_msg.linear.x = 0
    vel_msg.linear.y = abs(kecepatan)
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


def toright():
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.init_node('toright', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    vel_msg = Twist()
    # parameter
    kecepatan = input('Masukkan kecepatan: ')
    jarak = input('Masukkan jarak')

    vel_msg.linear.x = 0
    vel_msg.linear.y = -abs(kecepatan)
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


def upward():
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.init_node('upward', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    vel_msg = Twist()
    # parameter
    kecepatan = input('Masukkan kecepatan: ')
    jarak = input('Masukkan jarak')

    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = abs(kecepatan)
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


def downward():
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.init_node('downward', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    vel_msg = Twist()
    # parameter
    kecepatan = input('Masukkan kecepatan: ')
    jarak = input('Masukkan jarak')

    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = -abs(kecepatan)
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


def counterclock():
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.init_node('counterclock', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    vel_msg = Twist()
    # parameter
    kecepatan = input('Masukkan kecepatan: ')
    jarak = input('Masukkan jarak')

    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = abs(kecepatan)

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


def clockwise():
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.init_node('clockwise', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    vel_msg = Twist()
    # parameter
    kecepatan = input('Masukkan kecepatan: ')
    jarak = input('Masukkan jarak')

    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = -abs(kecepatan)

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


def hover():
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.init_node('clockwise', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    vel_msg = Twist()
    # parameter
    kecepatan = input('Masukkan kecepatan: ')
    jarak = input('Masukkan jarak')

    vel_msg.linear.x = 0
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
