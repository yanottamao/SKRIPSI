import rospy
from std_msgs.msg import String
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist


def fungsi_arah_bergerak(mode_state_terbang, lx, ly, lz, az):
    pub = rospy.Publisher(mode_state_terbang, Twist, queue_size=10)
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

# def kecepatan_default():
global kecepatan
kecepatan = float(input('Masukkan kecepatan antara 0.1 - 1: '))
# return kecepatan
fungsi_menu_arah(kecepatan)
