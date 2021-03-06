#importing necessary files
import numpy as np
import cv2

#get the cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('smile_cascade.xml')
smile_close_cascade = cv2.CascadeClassifier('smile_closed_cascade.xml')
frown_cascade = cv2.CascadeClassifier('sad.xml')

#To get the webcam video capture
cap = cv2.VideoCapture(0)

while 1:
	#reading camera capture
	ret, img = cap.read()
	#turning image captured gray
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	#detects objects of different sizes -> returned as a list of rectangles
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)

	#If my camera is detecting a face there should be a blue rectangle around
	#the face. Get the gray image array and regular image array.
	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]

		#Detect the objects of different sizes -> returned as a list of rectangles
		smiles = smile_cascade.detectMultiScale(roi_gray)
		smiles_closed = smile_close_cascade.detectMultiScale(roi_gray)
		frowns = frown_cascade.detectMultiScale(roi_gray)

		#If camera detects a face there should be a smile or a frown inside the face.
		#Put a red rectangle around the smile and a green rectangle around the frown.
		for (sx,sy,sw,sh) in smiles:
			cv2.rectangle(roi_color,(sx,sy),(sx + sw, sy + sh), (0, 0, 255), 2)

		for (sx,sy,sw,sh) in smiles_closed:
			cv2.rectangle(roi_color,(sx,sy),(sx + sw, sy + sh), (0, 0, 255), 2)

		for (sx,sy,sw,sh) in frowns:
			cv2.rectangle(roi_color,(sx,sy),(sx + sw, sy + sh), (0, 255, 0), 2)

	#shows the video stream
	cv2.imshow('img',img)
	#exit stuff
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break

#release capture destroy all windows
cap.release()
cv2.destroyAllWindows()
