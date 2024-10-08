import cv2
face_cascade = cv2.CascadeClassifier("C:\\Users\\ravik\\OneDrive\\Desktop\\project\\haarcascade_frontalface_default.xml")
img = cv2.imread("C:\\Users\\ravik\\OneDrive\\Pictures\\Saved Pictures\\face.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow('Detected Faces', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
