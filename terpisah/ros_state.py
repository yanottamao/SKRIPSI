
'''
harusnya sudah benar, tinggal cek pemanggilan
'''
# fungsi untuk pilihan takeoff atau landing


def fungsi_state_terbang(mode_state_terbang):
    # not sure what queue_size do
    pub = rospy.Publisher(mode_state_terbang, Empty, queue_size=10)
    rospy.init_node('terbang', anonymous=True)    # should be just once
    rate = rospy.Rate(10)   # should be frequency of transfer rate at 10 hz ?
    while not rospy.is_shutdown():
        pub.publish(Empty())
        rate.sleep()


'''
