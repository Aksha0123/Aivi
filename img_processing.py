# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg

# img = mpimg.imread('vein_img1.jpg')
# imgplot = plt.imshow(img)
# cmap = plt.get_cmap("Greens")
# plt.set_cmap(cmap)
# plt.show()

import cv2
import numpy as np

# Read the image
image = cv2.imread('vein_img1.jpg')

# Convert the image to HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Define the lower and upper bounds of the color you want to filter
lower_blue = np.array([0, 0, 0])
upper_blue = np.array([184,161,145])

# Create a mask for the specified color range
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Apply the mask to the original image
result = cv2.bitwise_and(image, image, mask=mask)

# Naming a window
cv2.namedWindow("original", cv2.WINDOW_NORMAL) 
cv2.namedWindow("mask", cv2.WINDOW_NORMAL)
cv2.namedWindow("filtered", cv2.WINDOW_NORMAL) 
  
# Using resizeWindow()
cv2.resizeWindow("original", 300, 700) 
cv2.resizeWindow("mask", 300, 700) 
cv2.resizeWindow("filtered", 300, 700) 

# Display the results
cv2.imshow('original', image)
cv2.imshow('mask', mask)
cv2.imshow('filtered', result)
cv2.waitKey(0)
cv2.destroyAllWindows()