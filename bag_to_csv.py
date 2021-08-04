import rosbag
from nav_msgs.msg import Odometry
import pandas as pd



# The bag file should be in the same directory as your terminal
bag = rosbag.Bag('traj8_weight.bag')
out_file = 'gt.csv'
topic = '/vicon/drone_ding/drone_ding'
column_names = ['time', 'x', 'y', 'z', 'qw', 'qx', 'qy', 'qz']


df = pd.DataFrame(columns=column_names)

for topic, msg, t in bag.read_messages(topics=topic):
    secs = msg.header.stamp.secs
    nsecs = msg.header.stamp.nsecs
    t = secs * (10**9) + nsecs

    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    z = msg.pose.pose.position.z

    qx = msg.pose.pose.orientation.x
    qy = msg.pose.pose.orientation.y
    qz = msg.pose.pose.orientation.z
    qw = msg.pose.pose.orientation.w

    df = df.append(
        {'time': t,
         'x': x,
         'y': y,
         'z': z,
         'qw': qw,
         'qx': qx,
         'qy': qy,
         'qz': qz},
        ignore_index=True)


df.to_csv(out_file, index=False)
