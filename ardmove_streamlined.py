#!/usr/bin/env python

# import ros - ros library untuk python, http://wiki.ros.org/rospy
from geometry_msgs.msg import Twist
import rospy
'''
import std_msgs dari library msg untuk mengirim pesan / perintah
ke drone - Empty untuk takeoff atau land, http://wiki.ros.org/msg,
http://wiki.ros.org/std_msgs
'''
from std_msgs.msg import String
from std_msgs.msg import Empty
'''
import geometry_msgs dari library msg untuk perintah pose / pergerakan
Twist berisi perintah linear dan angular, http://wiki.ros.org/geometry_msgs
'''

'''
fungsi untuk memasukkan kecepatan default yang akan digunakan
untuk mengontrol drone
'''


def kecepatandefault():
    global kecepatan
    kecepatan = float(input('Masukkan kecepatan antara 0.1 - 1: '))
    return kecepatan

# fungsi untuk memilih mode terbang dari drone


def modeterbang():
    print('Pilihan mode terbang:')
    print('1. Take off / terbang')
    print('2. Land / mendarat')
    print('3. Mode masukan arah')
    global mode
    modeinput = int(input('Masukkan mode terbang: '))
    if modeinput == 1:
        mode = 'ardrone/takeoff'
        return mode
    elif modeinput == 2:
        mode = 'ardrone/land'
        return mode
    elif modeinput == 3:
        mode = '/cmd_vel'
        return mode
    else:
        print('Pilih antara pilian diatas!')
        modeterbang()

# fungsi untuk memilih arah terbang drone


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

    global lx   # lx = linear x
    global ly   # ly = linear y
    global lz   # lz = linear z
    global az   # az = angular z

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

    #  bergerak searah jarum jam
    elif arahtujuan == 8:
        lx = 0
        ly = 0
        lz = 0
        az = -abs(kecepatan)
        return lx, ly, lz, az


'''
fungsi untuk terbang / takeoff dan mendarat / land
mengirim pesan / perintah Empty ke publisher (?) / node (?)
/ardrone/takeoff atau /ardrone/land - perintah diambil dari
return mode di fungsi modeterbang()
'''


def terbang(mode):
    # not sure what queue_size do
    pub = rospy.Publisher(mode, Empty, queue_size=10)
    rospy.init_node('terbang', anonymous=True)    # should be just once
    rate = rospy.Rate(10)   # should be frequency of transfer rate at 10 hz ?
    while not rospy.is_shutdown():
        pub.publish(Empty())
        rate.sleep()

# fungsi untuk arah bergerak drone ketika terbang
# mengirim pesan / perintah Twist yang berisi linear dan angular
# ke /cmd_vel yang diambil dari return lx, ly, lz, az di
# fungsi arah terbang()


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

# fungsi main


def main():
    print('Kendali Ar.Drone dengan Python')
    modeterbang()


# fungsi utama untuk memanggil main
if __name__ == '__main__':
    try:
        forward()
    except rospy.ROSInterruptException:
        pass
