'''
TO DO
1. ubah nama fungsi
2. ubah nama parameter
3. cari hubungan / sambungan antara pemanggilan fungsi
'''


#!/usr/bin/env python
# import ros
import rospy
from std_msgs.msg import String
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist


# import fungsi


'''
butuh cek variable
'''


def main():
    '''
    # print('Kendali Ar.Drone dengan Python')
    # modeterbang() ->  standar(perintah_standar)
    print('Kendali Ar.Drone dengan Python')
    modeterbang()
    '''
    while perintah_main != 'q':
        global perintah_menu_state_terbang
        perintah_menu_state_terbang = ''
        print('\nMenu utama')
        print('q. Keluar')
        print('1. Mulai')
        perintah_main = input('Masukkan perintah: ')
        print('')
        print('Perintah: ' + perintah_main)
        if perintah_main in ['1', 'q']:
            if perintah_main == '1':
                print('Menuju menu awal')
                menu_state_terbang(perintah_menu_state_terbang)
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
