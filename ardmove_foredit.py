#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist


def kecepatandefault():
    global kecepatan
    kecepatan = float(input('Masukkan kecepatan antara 0.1 - 1: '))
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


def arahterbang(kecepatan):
    print('Pilihan arah terbang:')
    print('0. Diam di udara')
    print('1. Naik')
    print('2. Turun')
    print('3. Maju')
    print('4. Mundur')
    print('5. Bergerak ke kanan')
    print('6. Bergerak ke kiri')
    print('7. Bergerak berlawanan jarum jam')
    print('8. Bergerak searah jarum jam')

    arahtujuan = int(input('Masukkan pilihan arah: '))
    global arahkecepatan

    global lx
    global ly
    global lz
    global az

    # diam di udara
    if arahtujuan == 0:
        lx = 0
        ly = 0
        lz = 0
        az = 0
        return lx, ly, lz, az

    # naik
    elif arahtujuan == 1:
        lx = 0
        ly = 0
        lz = abs(kecepatan)
        az = 0
        return lx, ly, lz, az

    # turun
    elif arahtujuan == 2:
        lx = 0
        ly = 0
        lz = -abs(kecepatan)
        az = 0
        return lx, ly, lz, az

    # maju
    elif arahtujuan == 3:
        lx = abs(kecepatan)
        ly = 0
        lz = 0
        az = 0
        return lx, ly, lz, az

    # mundur
    elif arahtujuan == 4:
        lx = -abs(kecepatan)
        ly = 0
        lz = 0
        az = 0
        return lx, ly, lz, az

    # bergerak ke kanan
    elif arahtujuan == 5:
        lx = 0
        ly = -abs(kecepatan)
        lz = 0
        az = 0
        return lx, ly, lz, az

    # bergerak ke kiri
    elif arahtujuan == 6:
        lx = 0
        ly = abs(kecepatan)
        lz = 0
        az = 0
        return lx, ly, lz, az

# bergerak berlawanan arah jarum jam
    elif arahtujuan == 7:
        lx = 0
        ly = 0
        lz = 0
        az = abs(kecepatan)
        return lx, ly, lz, az

# bergerak searah jarum jam
    elif arahtujuan == 8:
        lx = 0
        ly = 0
        lz = 0
        az = -abs(kecepatan)
        return lx, ly, lz, az


'''
    # diam di udara
    if arahtujuan == 0:
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0

    # naik
    elif arahtujuan == 1:
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = abs(kecepatan)
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0

    # turun
    elif arahtujuan == 2:
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = -abs(kecepatan)
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0

    # maju
    elif arahtujuan == 3:
        vel_msg.linear.x = abs(kecepatan)
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0

    # mundur
    elif arahtujuan == 4:
        vel_msg.linear.x = -abs(kecepatan)
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0

    # bergerak ke kanan
    elif arahtujuan == 5:
        vel_msg.linear.x = 0
        vel_msg.linear.y = -abs(kecepatan)
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0

    # bergerak ke kiri
    elif arahtujuan == 6:
        vel_msg.linear.x = 0
        vel_msg.linear.y = abs(kecepatan)
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0

# bergerak berlawanan arah jarum jam
    elif arahtujuan == 7:
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = abs(kecepatan)

# bergerak searah jarum jam
    elif arahtujuan == 8:
        vel_msg.linear.x = 0
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = -abs(kecepatan)
'''


def terbang(mode):
    # not sure what queue_size do
    pub = rospy.Publisher(mode, Empty, queue_size=10)
    rospy.init_node('terbang', anonymous=True)    # should be just once
    rate = rospy.Rate(10)   # should be frequency of transfer rate at 10 hz ?
    while not rospy.is_shutdown():
        pub.publish(Empty())
        rate.sleep()


def bergerak(mode, kecepatan, lx, ly, lz, az):
    pub = rospy.Publisher(mode, Twist, queue_size=10)
    # rospy.init_node('bergerak', anonymous = True) # should be not necessary
    rate = rospy.Rate(10)
    global vel_msg = Twist()

    vel_msg.linear.x = lx
    vel_msg.linear.y = ly
    vel_msg.linear.z = lz
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = az

    while not rospy.is_shutdown():
        pub.publish(vel_msg)
        rate.sleep()    # not sure


'''
def takeoff(mode):
    pub = rospy.Publisher(mode, Empty, queue_size=10)
    # rospy.init_node('takeoff', anonymous=True)    # not sure
    rate = rospy.Rate(10)  # 10hz
    while not rospy.is_shutdown():
        pub.publish(Empty())
        rate.sleep()


def land(mode):
    pub = rospy.Publisher(mode, Empty, queue_size=10)
    # rospy.init_node('land', anonymous=True)   # not sure
    rate = rospy.Rate(10)  # 10hz
    while not rospy.is_shutdown():
        pub.publish(Empty())
        rate.sleep()
'''

'''

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

'''

if __name__ == '__main__':
    try:
        forward()
    except rospy.ROSInterruptException:
        pass
