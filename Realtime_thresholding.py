import imutils
import numpy as np
import cv2
import os
from numba import jit
@jit(nopython=True)
def thresholdIntegral1(inputMat,s,T = 0.1):
	outputMat=np.zeros(inputMat.shape)
	nRows = inputMat.shape[0]
	nCols = inputMat.shape[1]
	S = int(max(nRows, nCols) / 8)

	s2 = int(S / 4)

	for i in range(nRows):
		y1 = i - s2
		y2 = i + s2

		if (y1 < 0) :
			y1 = 0
		if (y2 >= nRows):
			y2 = nRows - 1

		for j in range(nCols):
			x1 = j - s2
			x2 = j + s2

			if (x1 < 0) :
				x1 = 0
			if (x2 >= nCols):
				x2 = nCols - 1
			count = (x2 - x1)*(y2 - y1)

			sum=s[y2][x2]-s[y2][x1]-s[y1][x2]+s[y1][x1]

			if ((int)(inputMat[i][j] * count) < (int)(sum*(1.0 - T))):
				outputMat[i][j] = 255
	return outputMat

#Test tren camera khong day qua IP dien thoai
camera = cv2.VideoCapture('http://192.168.0.103:4747/video')

print("Adaptive Threshold by Integral image loading, Please press Q to exit !!!!!!")
#Duyệt từng frame
while True:
	(grabbed, frame) = camera.read()
	#Resize frame về theo chiều rong 700px
	frame = imutils.resize(frame, width = 700)
	gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	blurred_gray = cv2.GaussianBlur(gray_image, (5,5), 0)
	roii = cv2.integral(blurred_gray)
	
	#Lấy ngưỡng 0 -> 255 sử dụng láy ngưỡng nhị phân và otsu
	for j in range(1):
		image_mask = thresholdIntegral1(blurred_gray, roii)
	# image_mask=cv2.subtract(255, image_mask)
	cv2.imshow("original", frame)
	cv2.imshow("Result",image_mask)

	# Bấm phím q để thoát chương trình
	
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break

camera.release()
cv2.destroyAllWindows()


