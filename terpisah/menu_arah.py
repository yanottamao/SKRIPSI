from terpisah import kecepatan_default

kecepatan = kecepatan_default.kecepatan_default()


def fungsi_menu_arah(perintah_arah, kecepatan):
    while perintah_arah != 'q':
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
        perintah_arah = input('Masukkan perintah: ')
        print('')
        print('Perintah: ' + perintah_arah)
        if perintah_arah in ['q', 'u', 'i', 'k', 'j', 'l', 'y', 't', 'p', 'o']:

            # drone diam di udara hover
            if perintah_bergerak == 'u':
                print('Drone diam\n')
                lx = 0
                ly = 0
                lz = 0
                az = 0
                return lx, ly, lz, az

            # drone maju
            elif perintah_arah == 'i':
                print('Drone maju\n')
                lx = abs(kecepatan)
                ly = 0
                lz = 0
                az = 0
                return lx, ly, lz, az

            # drone mundur
            elif perintah_arah == 'k':
                print('Drone mundur\n')
                lx = -abs(kecepatan)
                ly = 0
                lz = 0
                az = 0
                return lx, ly, lz, az

            # drone ke kiri
            elif perintah_arah == 'j':
                print('Drone ke kiri\n')
                lx = 0
                ly = abs(kecepatan)
                lz = 0
                az = 0
                return lx, ly, lz, az

            # drone ke kanan
            elif perintah_arah == 'l':
                print('Drone ke kanan\n')
                lx = 0
                ly = -abs(kecepatan)
                lz = 0
                az = 0
                return lx, ly, lz, az

            # drone naik
            elif perintah_arah == 'y':
                print('Drone naik\n')
                lx = 0
                ly = 0
                lz = abs(kecepatan)
                az = 0
                return lx, ly, lz, az

            # drone turun
            elif perintah_arah == 't':
                print('Drone turun\n')
                lx = 0
                ly = 0
                lz = -abs(kecepatan)
                az = 0
                return lx, ly, lz, az

            # drone berputar searah jarum jam
            elif perintah_arah == 'p':
                print('Drone searah jarum jam\n')
                lx = 0
                ly = 0
                lz = 0
                az = -abs(kecepatan)
                return lx, ly, lz, az

            # drone berputar berlawanan jarum jam
            elif perintah_arah == 'o':
                print('Drone berlawanan jarum jam\n')
                lx = 0
                ly = 0
                lz = 0
                az = abs(kecepatan)
                return lx, ly, lz, az

            # kembali ke menu sebelumnya
            elif perintah_arah == 'q':
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
