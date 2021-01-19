# testing
# import ardmove_foredit_streamlined
# import ardimaging_foredit
from subprocess import call

'''
jalankan perintah pemanggilan import di terminal baru
'''


def main():
    # menggunakan call dulu
    global moving
    global imaging

    # at least call test success
    moving = call(['python3', 'ardmove_foredit_streamlined.py'])
    imaging = call(['python3', 'ardimaging_foredit.py'])


if __name__ == "__main__":
    main()
