#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist


def mode_bergerak(perintah_bergerak):
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


def standar(perintah_standar):
    while perintah_standar != 'q':
        print('\nMenu Awal')
        print('q. Keluar')
        print('f. Takeoff')
        print('g. Landing')
        print('h. Mode bergerak')
        perintah_standar = input('Masukkan perintah: ')
        print('')
        print('Perintah: ' + perintah_standar)
        if perintah_standar in ['q', 'f', 'g', 'h']:
            if perintah_standar == 'h':
                print('Menuju menu pergerakan')
                mode_bergerak(perintah_standar)
            elif perintah_standar == 'f':
                print('Drone takeoff\n')
            elif perintah_standar == 'g':
                print('Drone landing\n')
            elif perintah_standar == 'q':
                print('Keluar dari menu awal')
                break
        else:
            print('Masukkan sesuai perintah!')


def kecepatandefault():
    global kecepatan
    kecepatan = float(input('Masukkan kecepatan antara 0.1 - 1: '))
    return kecepatan


def modeterbang():
    kecepatandefault()
    print('\nPilihan mode terbang:')
    print('1. Take off / terbang')
    print('2. Land / mendarat')
    print('3. Mode masukan arah')
    global mode
    modeinput = int(input('Masukkan mode terbang: '))
    if modeinput == 1:
        mode = 'ardrone/takeoff'
        terbang(mode)
    elif modeinput == 2:
        mode = 'ardrone/land'
        terbang(mode)
    elif modeinput == 3:
        mode = '/cmd_vel'
        arahterbang(kecepatan)
        bergerak(mode, kecepatan, lx, ly, lz, az)
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
