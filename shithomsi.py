import cv2
import numpy as np
import matplotlib.pyplot as plt
image_path = "C:\\Users\\ravik\\OneDrive\\Pictures\\Saved Pictures\\building.jpeg"
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
max_corners = 100
quality_level = 0.01
min_distance = 10
corners = cv2.goodFeaturesToTrack(img, max_corners, quality_level, min_distance)
corners = np.int32(corners) 
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 3, 255, -1)
plt.imshow(img, cmap='gray')
plt.title('Detected Corners')
plt.axis('off')
plt.show()
