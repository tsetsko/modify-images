import cv2

face_cascade = cv2.CascadeClassifier('/Users/tdonov/Desktop/Python/modify images/images/sample_images/face_detection.xml')

img = cv2.imread('news.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.005, minNeighbors=4)

for x, y, w, h in faces:
    img=cv2.rectangle(img, (x,y), (x + w, y + h), (0, 255, 0), 3)

cv2.imshow('test', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(faces)