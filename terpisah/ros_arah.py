

'''
butuh cek parameter
'''
# fungsi untuk arah pergerakan ketika di udara


def fungsi_arah_bergerak(mode_state_terbang, lx, ly, lz, az):
    pub = rospy.Publisher(mode_state_terbang, Twist, queue_size=10)
    # rospy.init_node('bergerak', anonymous = True) # should be not necessary
    rate = rospy.Rate(10)
    global vel_msg
    vel_msg = Twist()

    vel_msg.linear.x = lx
    vel_msg.linear.y = ly
    vel_msg.linear.z = lz
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = az

    while not rospy.is_shutdown():
        pub.publish(vel_msg)
        rate.sleep()    # not sure
