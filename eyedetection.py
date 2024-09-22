import cv2
eye_cascade = cv2.CascadeClassifier('C:\\Users\\ravik\\Downloads\\haarcascade_eye.xml')
image_path = "C:\\Users\\ravik\\OneDrive\\Pictures\\Saved Pictures\\cutegirl.jpeg"
img = cv2.imread(image_path)
if img is None:
    print("Error: Could not load image. Please check the file path.")
    exit()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
for (x, y, w, h) in eyes:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)  
cv2.imshow('Detected Eyes', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
