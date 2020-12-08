
'''
butuh cek variabel + parameter
'''
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
                fungsi_menu_arah()      # ceck parameter
                # mode_bergerak(perintah_standar)
                mode_state_terbang = '/cmd_vel'
                mode_bergerak(perintah_bergerak, kecepatan)
                fungsi_arah_bergerak(mode_state_terbang,
                                     kecepatan, lx, ly, lz, az)

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
