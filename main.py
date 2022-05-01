import cv2
import matplotlib.pyplot as plt
# Write the code to perform histogram equalization of the image.
gray_image = cv2.imread('husk.jpg',0)
equ=cv2.equalizeHist(gray_image)
cv2.imshow('Gray image',gray_image)
cv2.imshow('Equalized Image',equ)
cv2.waitKey(0)
cv2.destroyAllWindows()

