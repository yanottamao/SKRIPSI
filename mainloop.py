'''
Referensi perintah untuk perulangan pemanggilan main
yang dikirim hanya satu perintah
untuk print lain tetap sama
'''


def main(perintah):
    while perintah != 'q':
        print('Maju')
        print('Maju')
        perintah = input('Masukkan perintah: ')
        print('Perintah: ' + perintah)


if __name__ == "__main__":
    global perintah
    perintah = ''
    main(perintah)
