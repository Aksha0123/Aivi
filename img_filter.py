import cv2
import numpy as np

# Read the image
image = cv2.imread('img22.jpg')
# Convert the image to HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#change contrast
alpha = 1.6 # Contrast control
beta = -100 # Brightness control
# 0.78, -100 for xray type
# 1.6, -100 for orangey saturated

# call convertScaleAbs function
contrast_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

# Naming a window
cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL) 
cv2.namedWindow("Contrast Adjusted", cv2.WINDOW_NORMAL)
  
# Using resizeWindow()
cv2.resizeWindow("Original Image", 300, 700) 
cv2.resizeWindow("Contrast Adjusted", 300, 700) 

cv2.imshow("Original Image", image)
cv2.imshow("Contrast Adjusted", contrast_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
