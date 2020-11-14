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

call(['rosrun', 'lsd_slam_core', 'live_slam',
      'image:/ardrone/front/image_raw', '_calib:/file'])
