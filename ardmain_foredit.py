# testing
# import ardmove_foredit_streamlined
# import ardimaging_foredit
from subprocess import call

'''
jalankan perintah pemanggilan import di terminal baru
'''

# menggunakan call dulu
global moving
global imaging

# initial test success
moving = call(['python3', 'ardmove_foredit_streamlined.py'])
imaging = call(['python3', 'ardimaging_foredit.py'])
