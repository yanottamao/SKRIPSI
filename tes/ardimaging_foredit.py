# actually not recommended
# need to fix formatting
import os
from subprocess import call
os.system(
    "rosrun lsd_slam_core live_slam image:/ardrone/front/image_raw _calib:/file")

# another way to call command to terminal
# reference https://stackoverflow.com/questions/3730964/python-script-execute-commands-in-terminal
# from subprocess import call
# call(['ls', '-l'])


def viewslam():
    # pemanggilan viewer
    viewslam_run = call(['rosrun', 'lsd_slam_viewer', 'viewer'])


def filecalib():
    global calibr
    calibr = input('Masukkan path file kalibrasi: ')
    print('Lokasi file: ' + calibr)
    return calibr


def slam(calibr):
    global slam_run
    # testing
    # slam_run = 'Jalankan slam'
    # print(slam_run)
    print('Path: ' + calibr)    # test pemanggilan return calibr
    slam_run = call(['rosrun', 'lsd_slam_core', 'live_slam',
                     'image:/ardrone/front/image_raw', '_calib:' + calibr])


def main():
    # slam()
    filecalib()
    slam(calibr)


if __name__ == "__main__":
    main()
