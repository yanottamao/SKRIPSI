'''
note error :
menu utama                                                          - ok
menu awal   - takeoff                                               - ok
            - land                                                  - ok
            - mode bergerak                                         - error     - ok sepertinya tambahan 1012
            - fungsi arah bergerak                                  - error     - ok sepertinya tambahan 1012
            - fungsi arah bergerak, kembali ke menu sebelumnya      - error

'''
# tambahan 1012 lab
#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist
import os

def fungsi_arah_bergerak(mode_state_terbang, lx, ly, lz, az):
    pub = rospy.Publisher(mode_state_terbang, Twist, queue_size=2)
    # rospy.init_node('bergerak', anonymous = True) # should be not necessary
    rate = rospy.Rate(10)
    global vel_msg
    vel_msg = Twist()

    vel_msg.linear.x = lx
    vel_msg.linear.y = ly
    vel_msg.linear.z = lz
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = az

    while not rospy.is_shutdown():
        pub.publish(vel_msg)
        rate.sleep()    # not sure
        # rospy.signal_shutdown('Break')
        break

    # tambahan 1012 lab
    # print('Fungsi fungsi_arah_bergerak')
    # print('Pengganti fungsi ros arah')
    # print('Mode state terbang: ' + mode_state_terbang)
    # print('\nSebelum print lx fungsi_arah_bergerak')
    # print('lx: ' + str(lx))     # tambahan 1012
    # print('ly: ' + str(ly))
    # print('lz: ' + str(lz))
    # print('az: ' + str(az))
    # # print('lx: ' + lx)
    # # print('ly: ' + ly)
    # # print('lz: ' + lz)
    # # print('az: ' + az)
    # fungsi_menu_arah(perintah_main, kecepatan)      # tambahan 1012
    fungsi_menu_arah(kecepatan)


def fungsi_state_terbang(mode_state_terbang):
    # not sure what queue_size do
    pub = rospy.Publisher(mode_state_terbang, Empty, queue_size=2)
    rospy.init_node('terbang', anonymous=True)    # should be just once
    rate = rospy.Rate(10)   # should be frequency of transfer rate at 10 hz ?
    while not rospy.is_shutdown():
        pub.publish(Empty())
        rate.sleep()
        # rospy.signal_shutdown('Break')
        break

    # tambahan 1012 lab
    # print('Pengganti fungsi ros state')
    # print('Mode state terbang: ' + mode_state_terbang)


# fungsi untuk inisialisasi kecepatan default
def kecepatan_default():
    global kecepatan
    kecepatan = 0       # default
    kecepatan = float(raw_input('Masukkan kecepatan antara 0.1 - 1: '))
    return kecepatan


# def fungsi_menu_arah(perintah_main, kecepatan):
def fungsi_menu_arah(kecepatan):
    perintah_main = ''
    while perintah_main != 'q':
        # kecepatan = kecepatan_default()       # kayaknya belum perlu
        global lx
        global ly
        global lz
        global az     # tambahan 1012

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
        perintah_main = raw_input('Masukkan perintah: ')
        print('')
        print('Perintah: ' + perintah_main)
        if perintah_main in ['q', 'u', 'i', 'k', 'j', 'l', 'y', 't', 'p', 'o']:

           # drone diam di udara hover
            if perintah_main == 'u':
                print('Drone diam\n')
                mode_state_terbang = '/cmd_vel'
                # tambahan 1012
                print('Fungsi fungsi_menu_arah')
                print('Mode state terbang: ' + mode_state_terbang)
                print('')
                lx = float(0)
                ly = float(0)
                lz = float(0)
                az = float(0)
                # print('Sebelum print lx')
                # print('lx: ' + str(lx))     # tambahan 1012
                # print('ly: ' + str(ly))
                # print('lz: ' + str(lz))
                # print('az: ' + str(az))
                fungsi_arah_bergerak(mode_state_terbang,
                                     lx, ly, lz, az)    # tambahan 1012
                # return lx, ly, lz, az

            # drone maju
            elif perintah_main == 'i':
                print('Drone maju\n')
                mode_state_terbang = '/cmd_vel'
                # tambahan 1012
                lx = abs(kecepatan)
                ly = 0
                lz = 0
                az = 0
                fungsi_arah_bergerak(mode_state_terbang,
                                     lx, ly, lz, az)    # tambahan 1012
                # return lx, ly, lz, az

            # drone mundur
            elif perintah_main == 'k':
                print('Drone mundur\n')
                mode_state_terbang = '/cmd_vel'
                # tambahan 1012
                lx = -abs(kecepatan)
                ly = 0
                lz = 0
                az = 0
                fungsi_arah_bergerak(mode_state_terbang,
                                     lx, ly, lz, az)    # tambahan 1012
                # return lx, ly, lz, az

            # drone ke kiri
            elif perintah_main == 'j':
                print('Drone ke kiri\n')
                mode_state_terbang = '/cmd_vel'
                # tambahan 1012
                lx = 0
                ly = abs(kecepatan)
                lz = 0
                az = 0
                fungsi_arah_bergerak(mode_state_terbang,
                                     lx, ly, lz, az)    # tambahan 1012
                # return lx, ly, lz, az

            # drone ke kanan
            elif perintah_main == 'l':
                print('Drone ke kanan\n')
                mode_state_terbang = '/cmd_vel'
                # tambahan 1012
                lx = 0
                ly = -abs(kecepatan)
                lz = 0
                az = 0
                fungsi_arah_bergerak(mode_state_terbang,
                                     lx, ly, lz, az)    # tambahan 1012
                # return lx, ly, lz, az

            # drone naik
            elif perintah_main == 'y':
                print('Drone naik\n')
                mode_state_terbang = '/cmd_vel'
                # tambahan 1012
                lx = 0
                ly = 0
                lz = abs(kecepatan)
                az = 0
                fungsi_arah_bergerak(mode_state_terbang,
                                     lx, ly, lz, az)    # tambahan 1012
                # return lx, ly, lz, az

            # drone turun
            elif perintah_main == 't':
                print('Drone turun\n')
                mode_state_terbang = '/cmd_vel'
                # tambahan 1012
                lx = 0
                ly = 0
                lz = -abs(kecepatan)
                az = 0
                fungsi_arah_bergerak(mode_state_terbang,
                                     lx, ly, lz, az)    # tambahan 1012
                # return lx, ly, lz, az

            # drone berputar searah jarum jam
            elif perintah_main == 'p':
                print('Drone searah jarum jam\n')
                mode_state_terbang = '/cmd_vel'
                # tambahan 1012
                lx = 0
                ly = 0
                lz = 0
                az = -abs(kecepatan)
                fungsi_arah_bergerak(mode_state_terbang,
                                     lx, ly, lz, az)    # tambahan 1012
                # return lx, ly, lz, az

            # drone berputar berlawanan jarum jam
            elif perintah_main == 'o':
                print('Drone berlawanan jarum jam\n')
                mode_state_terbang = '/cmd_vel'
                # tambahan 1012
                lx = 0
                ly = 0
                lz = 0
                az = abs(kecepatan)
                fungsi_arah_bergerak(mode_state_terbang,
                                     lx, ly, lz, az)    # tambahan 1012
                # return lx, ly, lz, az

            # kembali ke menu sebelumnya
            elif perintah_main == 'q':
                print('Keluar dari menu pergerakan')
                # lx = 0
                # ly = 0
                # lz = 0
                # az = 0
                # return lx, ly, lz, az     # tambahan 1012
                break
                # perintah_main = ''
                # menu_state_terbang(perintah_main)
        else:
            print('Masukkan sesuai perintah!')
            print('Fungsi fungsi_menu_arah')
            # lx = 0
            # ly = 0
            # lz = 0
            # az = 0
            # return lx, ly, lz, az


# def menu_state_terbang(perintah_main):
def menu_state_terbang():
    perintah_main = ''
    while perintah_main != 'q':
        print('\nMenu Awal')
        print('q. Keluar')
        print('d. Diam')
        print('f. Takeoff')
        print('g. Landing')
        print('h. Mode bergerak')
        perintah_main = str(raw_input('Masukkan perintah: '))
        print('')
        print('Perintah: ' + perintah_main)
        if perintah_main in ['q', 'd', 'f', 'g', 'h']:

            # menuju ke menu pergerakan
            if perintah_main == 'h':
                print('Perintah: ' + perintah_main)
                kecepatan = kecepatan_default()     # tambahan 1012
                # cek dulu
                print('Menuju menu pergerakan')
                # ceck parameter
                # fungsi_menu_arah(perintah_main, kecepatan)
                fungsi_menu_arah(kecepatan)
                # mode_bergerak(perintah_standar)
                mode_state_terbang = '/cmd_vel'
                return mode_state_terbang       # tambahan 1012
                # mode_bergerak(perintah_bergerak, kecepatan)
                # fungsi_arah_bergerak(mode_state_terbang,
                #                      kecepatan, lx, ly, lz, az)
                # fungsi_arah_bergerak(mode_state_terbang, lx, ly, lz, az)      - tambahan 1012

            elif perintah_main == 'd':
                print('Drone diam\n')
                mode_state_terbang = '/cmd_vel'
                lx = 0
                ly = 0
                lz = 0
                az = 0
                kecepatan = 0
                fungsi_arah_bergerak(mode_state_terbang,
                                     lx, ly, lz, az)
            
            # drone takeoff
            elif perintah_main == 'f':
                print('Drone takeoff\n')
                mode_state_terbang = 'ardrone/takeoff'
                fungsi_state_terbang(mode_state_terbang)

            # drone landing
            elif perintah_main == 'g':
                print('Drone landing\n')
                mode_state_terbang = 'ardrone/land'
                fungsi_state_terbang(mode_state_terbang)

            # kembali ke menu sebelumnya
            elif perintah_main == 'q':
                print('Keluar dari menu awal')
                # tambahan 1012
                break
                # perintah_main = ''
                # main(perintah_main)
        else:
            print('Masukkan sesuai perintah!')
            print('Fungsi menu_state_terbang')


# def main(perintah_main):
def main():
    perintah_main = ''
    while perintah_main != 'q':
        print('\nMenu utama')
        print('q. Keluar')
        print('1. Mulai')
        print('2. Mulai kamera')
        perintah_main = str(raw_input('Masukkan perintah: '))
        print('')
        print('Perintah: ' + str(perintah_main))
        if perintah_main in ['1', '2', 'q']:
            if perintah_main == '1':
                print('Menuju menu awal')
                # menu_state_terbang(perintah_main)
                menu_state_terbang()
            elif perintah_main == '2':
                os.system('rosrun image_view image_view image:=/ardrone/front/image_raw')
                return
            elif perintah_main == 'q':
                print('Keluar dari program')
                break
                # quit()
        else:
            print('Masukkan sesuai perintah!')
            print('Fungsi main')


if __name__ == '__main__':
    try:
        # global perintah_main
        # perintah_main = 'f'
        # main(perintah_main)
        main()
    # except:
    #     print('Ada yg error....')
    except rospy.ROSInterruptException:
        pass
