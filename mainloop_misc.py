import os

def main():
    perintah_main = ''
    while perintah_main != 'q':
        print('\nMenu utama')
        print('q. Keluar')
        print('1. Mulai viewer slam')
        print('2. Mulai kamera slam')
        print('3. Mulai kamera ros')
        perintah_main = str(raw_input('Masukkan perintah: '))
        print('')
        print('Perintah: ' + str(perintah_main))
        if perintah_main in ['1', '2', '3', 'q']:
            if perintah_main == '1':
                os.system('rosrun lsd_slam_viewer viewer')
            elif perintah_main == '2':
                os.system('rosrun lsd_slam_core live_slam image:=/ardrone/front/image_raw _calib:=/home/lab/cameraconfig/ardrone_front_79.cfg')
            elif perintah_main == '3':
                os.system('rosrun image_view image_view image:=/ardrone/front/image_raw')

if __name__ == "__main__":
    try:
        main()
    except:
        print('Ada yang error...')