import cv2
import numpy as np

img = cv2.imread('Examen1.jpg')

# Method 1: copy image and set other channels to black
# r = img.copy()
# r[:,:,0] = r[:,:,1] = 0

# g = img.copy()
# g[:,:,0] = g[:,:,2] = 0

# b = img.copy()
# b[:,:,1] = b[:,:,2] = 0

# cv2.imshow("red",r)
# cv2.imshow("green",g)
# cv2.imshow("blue",b)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Method 2: split channels and merge with black channels
b,g,r = cv2.split(img)
k = np.zeros_like(b)
b = cv2.merge([b,k,k])
g = cv2.merge([k,g,k])
r = cv2.merge([k,k,r])

cv2.imshow("red",r)
cv2.imshow("green",g)
cv2.imshow("blue",b)
cv2.waitKey(0)
cv2.destroyAllWindows()

# save results
cv2.imwrite("mandril3_red.jpg", r)
cv2.imwrite("mandril3_green.jpg", g)
cv2.imwrite("mandril3_blue.jpg", b)
