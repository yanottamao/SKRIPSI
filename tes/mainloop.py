'''
Referensi perintah untuk perulangan pemanggilan main
yang dikirim hanya satu perintah
untuk print lain tetap sama
'''


def mode_bergerak(perintah_bergerak):
    while perintah_bergerak != False:
        # while perintah_bergerak != 'q':
        print('q. Keluar')
        print('i. Maju')
        print('k. Mundur')
        print('j. Ke kiri')
        print('l. Ke kanan')
        print('y. Naik')
        print('t. Turun')
        print('p. Searah jarum jam')
        print('o. Berlawanan jarum jam')
        perintah_bergerak = input('Masukkan perintah: ')
        print('Perintah: ' + perintah_bergerak)
        if perintah_bergerak == 'i':
            print('Drone maju\n')
        elif perintah_bergerak == 'k':
            print('Drone mundur\n')
        elif perintah_bergerak == 'j':
            print('Drone ke kiri\n')
        elif perintah_bergerak == 'l':
            print('Drone ke kanan\n')
        elif perintah_bergerak == 'y':
            print('Drone naik\n')
        elif perintah_bergerak == 't':
            print('Drone turun\n')
        elif perintah_bergerak == 'p':
            print('Drone searah jarum jam\n')
        elif perintah_bergerak == 'o':
            print('Drone berlawanan jarum jam\n')
        elif perintah_bergerak == 'q':
            break
        else:
            print('Masukkan sesuai perintah!\n')
            mode_bergerak(perintah_bergerak)


def standar(perintah_standar):
    while perintah_standar != False:
        # while perintah_awal != 'q':
        print('q. Keluar')
        print('f. Takeoff')
        print('g. Landing')
        print('h. Mode bergerak')
        perintah_standar = input('Masukkan perintah: ')
        print('Perintah: ' + perintah_standar)
        if perintah_standar == 'h':
            mode_bergerak(perintah_standar)
        elif perintah_standar == 'f':
            print('Drone takeoff\n')
        elif perintah_standar == 'g':
            print('Drone landing\n')
        elif perintah_standar == 'q':
            break


def main(perintah_main):
    print('\nMenu utama')
    print('q. Keluar')
    print('1. Mulai')
    perintah_main = input('Masukkan perintah: ')
    while perintah_main != 'q':
        standar(perintah_standar)


if __name__ == "__main__":
    global perintah_main
    global perintah_bergerak
    global perintah_standar
    perintah_main = True
    perintah_bergerak = True
    # perintah_awal = ''
    # perintah_bergerak = ''
    perintah_standar = ''
    main(perintah_standar)
