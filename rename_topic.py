import rosbag

path = '/home/zinuok/Dataset/kaistviodataset/data/'
t = ['infinite','square','rotation']
seq = ['', '_fast','_head']

for type_ in t:
	for s in seq:
		with rosbag.Bag(path+type_+'/'+type_+s+'_res.bag', 'w') as outbag:
			for topic, msg, t in rosbag.Bag(path+type_+'/'+type_+s+'_out.bag').read_messages():
				# This also replaces tf timestamps under the assumption
				# that all transforms in the message share the same timestamp
				if topic == "/camera/color/image_raw/out":
					outbag.write("/camera/color/image_raw", msg, t)
				elif topic == "/camera/infra1/image_rect_raw/out":
					outbag.write("/camera/infra1/image_rect_raw", msg, t)
				elif topic == "/camera/infra2/image_rect_raw/out":
					outbag.write("/camera/infra2/image_rect_raw", msg, t)
				else:
					outbag.write(topic, msg, t)
