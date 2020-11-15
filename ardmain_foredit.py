import ardmove_foredit_streamlined
import ardimaging_foredit
from subprocess import call

'''
jalankan perintah pemanggilan import di terminal baru
'''

# menggunakan call dulu
global moving
global imaging

moving = call(['python', 'ardmove_foredit_streamlined.py'])
imaging = call(['python', 'ardimaging_foredit.py'])
