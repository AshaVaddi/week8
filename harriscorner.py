import cv2
import numpy as np
image_path = "C:\\Users\\ravik\\OneDrive\\Pictures\\Saved Pictures\\building.jpeg"
img = cv2.imread(image_path)
if img is None:
    print(f"Error: Could not load image from {image_path}. Please check the file path and permissions.")
    exit()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
corners = cv2.cornerHarris(gray, 2, 3, 0.04)
corners = cv2.dilate(corners, None)
threshold = 0.01 * corners.max()
img[corners > threshold] = [0, 0, 255]
cv2.imshow("Corners Detected", img)
cv2.imwrite("corners_detected.jpeg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
