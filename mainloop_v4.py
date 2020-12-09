'''
note error :
menu utama                      - ok
menu awal   - takeoff           - ok
            - land              - ok
            - mode bergerak     - error

'''


def fungsi_arah_bergerak(mode_state_terbang, lx, ly, lz, az):
    # pub = rospy.Publisher(mode_state_terbang, Twist, queue_size=10)
    # # rospy.init_node('bergerak', anonymous = True) # should be not necessary
    # rate = rospy.Rate(10)
    # global vel_msg
    # vel_msg = Twist()

    # vel_msg.linear.x = lx
    # vel_msg.linear.y = ly
    # vel_msg.linear.z = lz
    # vel_msg.angular.x = 0
    # vel_msg.angular.y = 0
    # vel_msg.angular.z = az

    # while not rospy.is_shutdown():
    #     pub.publish(vel_msg)
    #     rate.sleep()    # not sure
    print('Pengganti fungsi ros arah')
    print('Mode state terbang: ' + mode_state_terbang)
    print('lx: ' + lx)
    print('ly: ' + ly)
    print('lz: ' + lz)
    print('az: ' + az)


def fungsi_state_terbang(mode_state_terbang):
    # # not sure what queue_size do
    # pub = rospy.Publisher(mode_state_terbang, Empty, queue_size=10)
    # rospy.init_node('terbang', anonymous=True)    # should be just once
    # rate = rospy.Rate(10)   # should be frequency of transfer rate at 10 hz ?
    # while not rospy.is_shutdown():
    #     pub.publish(Empty())
    #     rate.sleep()
    print('Pengganti fungsi ros state')
    print('Mode state terbang: ' + mode_state_terbang)


# fungsi untuk inisialisasi kecepatan default
def kecepatan_default():
    global kecepatan
    kecepatan = float(input('Masukkan kecepatan antara 0.1 - 1: '))
    return kecepatan


def fungsi_menu_arah(perintah_main, kecepatan):
    while perintah_main != 'q':
        kecepatan = kecepatan_default()
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
        perintah_main = input('Masukkan perintah: ')
        print('')
        print('Perintah: ' + perintah_main)
        if perintah_main in ['q', 'u', 'i', 'k', 'j', 'l', 'y', 't', 'p', 'o']:

            # drone diam di udara hover
            if perintah_main == 'u':
                print('Drone diam\n')
                lx = 0
                ly = 0
                lz = 0
                az = 0
                return lx, ly, lz, az

            # drone maju
            elif perintah_main == 'i':
                print('Drone maju\n')
                lx = abs(kecepatan)
                ly = 0
                lz = 0
                az = 0
                return lx, ly, lz, az

            # drone mundur
            elif perintah_main == 'k':
                print('Drone mundur\n')
                lx = -abs(kecepatan)
                ly = 0
                lz = 0
                az = 0
                return lx, ly, lz, az

            # drone ke kiri
            elif perintah_main == 'j':
                print('Drone ke kiri\n')
                lx = 0
                ly = abs(kecepatan)
                lz = 0
                az = 0
                return lx, ly, lz, az

            # drone ke kanan
            elif perintah_main == 'l':
                print('Drone ke kanan\n')
                lx = 0
                ly = -abs(kecepatan)
                lz = 0
                az = 0
                return lx, ly, lz, az

            # drone naik
            elif perintah_main == 'y':
                print('Drone naik\n')
                lx = 0
                ly = 0
                lz = abs(kecepatan)
                az = 0
                return lx, ly, lz, az

            # drone turun
            elif perintah_main == 't':
                print('Drone turun\n')
                lx = 0
                ly = 0
                lz = -abs(kecepatan)
                az = 0
                return lx, ly, lz, az

            # drone berputar searah jarum jam
            elif perintah_main == 'p':
                print('Drone searah jarum jam\n')
                lx = 0
                ly = 0
                lz = 0
                az = -abs(kecepatan)
                return lx, ly, lz, az

            # drone berputar berlawanan jarum jam
            elif perintah_main == 'o':
                print('Drone berlawanan jarum jam\n')
                lx = 0
                ly = 0
                lz = 0
                az = abs(kecepatan)
                return lx, ly, lz, az

            # kembali ke menu sebelumnya
            elif perintah_main == 'q':
                print('Keluar dari menu pergerakan')
                lx = 0
                ly = 0
                lz = 0
                az = 0
                return lx, ly, lz, az
                # break
        else:
            print('Masukkan sesuai perintah!')
            lx = 0
            ly = 0
            lz = 0
            az = 0
            return lx, ly, lz, az


def menu_state_terbang(perintah_main):
    while perintah_main != 'q':
        print('\nMenu Awal')
        print('q. Keluar')
        print('f. Takeoff')
        print('g. Landing')
        print('h. Mode bergerak')
        perintah_main = input('Masukkan perintah: ')
        print('')
        print('Perintah: ' + perintah_main)
        if perintah_main in ['q', 'f', 'g', 'h']:

            # menuju ke menu pergerakan
            if perintah_main == 'h':
                # cek dulu
                print('Menuju menu pergerakan')
                # ceck parameter
                fungsi_menu_arah(perintah_main, kecepatan)
                # mode_bergerak(perintah_standar)
                mode_state_terbang = '/cmd_vel'
                # mode_bergerak(perintah_bergerak, kecepatan)
                # fungsi_arah_bergerak(mode_state_terbang,
                #                      kecepatan, lx, ly, lz, az)
                fungsi_arah_bergerak(mode_state_terbang, lx, ly, lz, az)

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
                break
        else:
            print('Masukkan sesuai perintah!')


def main(perintah_main):
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
                menu_state_terbang(perintah_main)
            elif perintah_main == 'q':
                print('Keluar dari program')
                break
        else:
            print('Masukkan sesuai perintah!')


if __name__ == '__main__':
    try:
        global perintah_main
        perintah_main = ''
        main(perintah_main)
    except:
        print('Ada yg error....')
    # except rospy.ROSInterruptException:
    #     pass
