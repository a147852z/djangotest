# coding:utf-8
import numpy as np
import cv2

# input:
# 请把需要连接的图片放到同一个文件夹下面，图片名称最好具有相同的格式
N = 12		# 共有图片N张
M = 3	 	# 每M张合成一张纵向长图
# M = N       # 如果仅需要合成单张图片，请解除此句的注释，令 M=N

# 路径可以是绝对路径，也可以是相对路径，注意路径中不能出现中文，否则无法被imread读取
img_path = 'C:/Users/Gslab/Desktop/c109112107/django/django/123/'
save_path = 'C:/Users/Gslab/Desktop/c109112107/django\django/1234/'

G = np.ceil(N / M) 	# 共分为G组
G = G.astype(np.int32)
print(' image  :', N, '\n',
	   'length :', M, '\n',
	   'group  :', G)
imgs2 = []
for j in range(0, G):

	imgs = []

	# 把一组图像存到imgs里面
	for i in range(j*M + 1, min((j+1)*M, N) + 1):
		# 每个文件的路径
		path = img_path + str(i) + '.jpg'
		mat = cv2.imread(path)
		imgs.append(mat)
	# 把imgs里面的数据按垂直方向合并
	img = np.vstack(imgs)
	imgs2.append(img)
	# cv2.imshow('frame', img)
	# 保存合成图
	cv2.imwrite(save_path + 'out_' + str(j+1) + '.png', img)

a = np.hstack(imgs2)
cv2.imwrite(save_path + 'out_' + str(j+1) + '.png', a)
cv2.imshow("123",a)
cv2.waitKey(0)