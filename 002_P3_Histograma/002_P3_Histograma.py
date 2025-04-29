import cv2
import numpy

img1 = cv2.imread('3D-Matplotlib.png')
img_to_yuv = cv2.cvtColor(img1,cv2.COLOR_BGR2YUV)
img_to_yuv[:,:,0] = cv2.equalizeHist(img_to_yuv[:,:,0])
hist_equalization_result1 = cv2.cvtColor(img_to_yuv, cv2.COLOR_YUV2BGR)
cv2.imwrite('result.jpg',hist_equalization_result1)

img2 = cv2.imread('mainlogo.png')
img_to_yuv = cv2.cvtColor(img2,cv2.COLOR_BGR2YUV)
img_to_yuv[:,:,0] = cv2.equalizeHist(img_to_yuv[:,:,0])
hist_equalization_result2 = cv2.cvtColor(img_to_yuv, cv2.COLOR_YUV2BGR)
cv2.imwrite('result1.jpg',hist_equalization_result2)

img3 = cv2.imread('mainsvmimage.png')
img_to_yuv = cv2.cvtColor(img3,cv2.COLOR_BGR2YUV)
img_to_yuv[:,:,0] = cv2.equalizeHist(img_to_yuv[:,:,0])
hist_equalization_result3 = cv2.cvtColor(img_to_yuv, cv2.COLOR_YUV2BGR)
cv2.imwrite('result2.jpg',hist_equalization_result3)

cv2.imshow('result.jpg',hist_equalization_result1)
cv2.imshow('result1.jpg',hist_equalization_result2)
cv2.imshow('result2.jpg',hist_equalization_result3)
