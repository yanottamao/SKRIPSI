#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist


# fungsi untuk inisialisasi kecepatan default
def kecepatan_default():
    global kecepatan
    kecepatan = float(input('Masukkan kecepatan antara 0.1 - 1: '))
    return kecepatan


def mode_bergerak(perintah_bergerak, kecepatan):
    while perintah_bergerak != 'q':
        global lx
        global ly
        global lz
        global az

        print('\nMenu pergerakan')
        print('q. Keluar')
        print('u. Diam di udara')
        print('i. Maju')
        print('k. Mundur')
        print('j. Ke kiri')
        print('l. Ke kanan')
        print('y. Naik')
        print('t. Turun')
        print('p. Searah jarum jam')
        print('o. Berlawanan jarum jam')
        perintah_bergerak = input('Masukkan perintah: ')
        print('')
        print('Perintah: ' + perintah_bergerak)
        if perintah_bergerak in ['q', 'u', 'i', 'k', 'j', 'l', 'y', 't', 'p', 'o']:
            # drone diam di udara hover
            if perintah_bergerak == 'u':
                print('Drone diam\n')
                lx = 0
                ly = 0
                lz = 0
                az = 0
                return lx, ly, lz, az

            # drone maju
            elif perintah_bergerak == 'i':
                print('Drone maju\n')
                lx = abs(kecepatan)
                ly = 0
                lz = 0
                az = 0
                return lx, ly, lz, az

            # drone mundur
            elif perintah_bergerak == 'k':
                print('Drone mundur\n')
                lx = -abs(kecepatan)
                ly = 0
                lz = 0
                az = 0
                return lx, ly, lz, az

            # drone ke kiri
            elif perintah_bergerak == 'j':
                print('Drone ke kiri\n')
                lx = 0
                ly = abs(kecepatan)
                lz = 0
                az = 0
                return lx, ly, lz, az

            # drone ke kanan
            elif perintah_bergerak == 'l':
                print('Drone ke kanan\n')
                lx = 0
                ly = -abs(kecepatan)
                lz = 0
                az = 0
                return lx, ly, lz, az

            # drone naik
            elif perintah_bergerak == 'y':
                print('Drone naik\n')
                lx = 0
                ly = 0
                lz = abs(kecepatan)
                az = 0
                return lx, ly, lz, az

            # drone turun
            elif perintah_bergerak == 't':
                print('Drone turun\n')
                lx = 0
                ly = 0
                lz = -abs(kecepatan)
                az = 0
                return lx, ly, lz, az

            # drone berputar searah jarum jam
            elif perintah_bergerak == 'p':
                print('Drone searah jarum jam\n')
                lx = 0
                ly = 0
                lz = 0
                az = -abs(kecepatan)
                return lx, ly, lz, az

            # drone berputar berlawanan jarum jam
            elif perintah_bergerak == 'o':
                print('Drone berlawanan jarum jam\n')
                lx = 0
                ly = 0
                lz = 0
                az = abs(kecepatan)
                return lx, ly, lz, az

            # kembali ke menu sebelumnya
            elif perintah_bergerak == 'q':
                print('Keluar dari menu pergerakan')
                lx = 0
                ly = 0
                lz = 0
                az = 0
                return lx, ly, lz, az
                break
        else:
            print('Masukkan sesuai perintah!')
            lx = 0
            ly = 0
            lz = 0
            az = 0
            return lx, ly, lz, az


# fungsi untuk pilihan takeoff atau landing
def state_terbang(mode_state_terbang):
    # not sure what queue_size do
    pub = rospy.Publisher(mode_state_terbang, Empty, queue_size=10)
    rospy.init_node('terbang', anonymous=True)    # should be just once
    rate = rospy.Rate(10)   # should be frequency of transfer rate at 10 hz ?
    while not rospy.is_shutdown():
        pub.publish(Empty())
        rate.sleep()


# fungsi untuk arah pergerakan ketika di udara
def arah_bergerak(mode_state_terbang, kecepatan, lx, ly, lz, az):
    pub = rospy.Publisher(mode_state_terbang, Twist, queue_size=10)
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


# def standar(perintah_standar):
def menu_state_terbang(perintah_menu_state_terbang):
    while perintah_menu_state_terbang != 'q':
        global mode_state_terbang
        print('\nMenu Awal')
        print('q. Keluar')
        print('f. Takeoff')
        print('g. Landing')
        print('h. Mode bergerak')
        perintah_menu_state_terbang = input('Masukkan perintah: ')
        print('')
        print('Perintah: ' + perintah_menu_state_terbang)
        if perintah_menu_state_terbang in ['q', 'f', 'g', 'h']:

            # menuju ke menu pergerakan
            if perintah_menu_state_terbang == 'h':
                # cek dulu
                print('Menuju menu pergerakan')
                mode_bergerak(perintah_standar)
                mode_state_terbang = '/cmd_vel'
                mode_bergerak(perintah_bergerak, kecepatan)
                arah_bergerak(mode_state_terbang, kecepatan, lx, ly, lz, az)

            # drone takeoff
            elif perintah_menu_state_terbang == 'f':
                print('Drone takeoff\n')
                mode_state_terbang = 'ardrone/takeoff'
                state_terbang(mode_state_terbang)

            # drone landing
            elif perintah_menu_state_terbang == 'g':
                print('Drone landing\n')
                mode_state_terbang = 'ardrone/land'
                state_terbang(mode_state_terbang)

            # kembali ke menu sebelumnya
            elif perintah_menu_state_terbang == 'q':
                print('Keluar dari menu awal')
                break
        else:
            print('Masukkan sesuai perintah!')


def main():
    '''
    # print('Kendali Ar.Drone dengan Python')
    # modeterbang() ->  standar(perintah_standar)
    print('Kendali Ar.Drone dengan Python')
    modeterbang()
    '''
    while perintah_main != 'q':
        print('\nMenu utama')
        print('q. Keluar')
        print('1. Mulai')
        perintah_main = input('Masukkan perintah: ')
        print('')
        print('Perintah: ' + perintah_main)
        if perintah_main in ['1', 'q']:
            if perintah_main == '1':
                print('Menuju menu awal')
                standar(perintah_standar)
            elif perintah_main == 'q':
                print('Keluar dari program')
                break
        else:
            print('Masukkan sesuai perintah!')


if __name__ == '__main__':
    try:
        global perintah_main
        global perintah_bergerak
        global perintah_standar
        perintah_main = ''
        perintah_bergerak = ''
        perintah_standar = ''
        main(perintah_main)
    except rospy.ROSInterruptException:
        pass
