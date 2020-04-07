# Name:       Phan Ben 
# email:      phanben110@gmail.com
# links face: https://www.facebook.com/ben.phan.5011

import cv2
import numpy as np
#face_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
#face_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')
#eye_cascade = cv2. cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')

#face_cascade = cv2. cv2.CascadeClassifier('mouth.xml')

#face_cascade = cv2.CascadeClassifier('mouth.xml')
#face_cascade = cv2.CascaderClassifier('haarcascades_frontalcatface.xml')

#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
#haarcascade_frontalface_alt.xml
body_cascade = cv2.CascadeClassifier('haarcascade_mcs_upperbody.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
mouth_cascade = cv2.cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')
cap = cv2.VideoCapture(0)
while True:
	ret, img = cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	#faces = face_cascade.detectMultiScale(gray, 1.3,5)
	body = body_cascade.detectMultiScale(gray, 1.3, 5)
	for(bx,by,bw,bh) in body:
		cv2.rectangle(img,(bx,by), (bx+bw , by+bh), (255,0,0) ,2)
		roi_gray1 = gray[by:by+bh, bx:bx+bw]
		roi_color1= img[by:by+bh, bx:bx+bw]
		face = face_cascade.detectMultiScale(roi_gray1)
		i = 0
		for (fx,fy,fw,fh) in face:
			areaFace = fw*fh
			areaUperBody = bw*bh
			i=i+1
			if areaUperBody<=98000  :
				#cv2.rectangle(roi_color1, (fx, fy), (fx + fw, fy + fh), (0, 255, 0), 2)
				cv2.putText(img, "Warning: deo khau trang di Ben deptrai", (bx, by - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
							(0, 0, 255), 3)
				roi_gray2 = gray[fx:fx + fh, fy:fy + fw * 2]
				roi_color2 = img[fx:fx + fh, fy:fy + fw * 2]
				mouth = mouth_cascade.detectMultiScale(roi_color2)
			else:
				if areaUperBody > 98000:
					if (areaUperBody/areaFace <= 4) :
						#cv2.rectangle(roi_color1, (fx, fy), (fx + fw, fy + fh), (0, 255, 0), 2)
						cv2.putText(img, "Warning: deo khau trang di Ben deptrai", (bx, by - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
									(0, 0, 255), 3)
						roi_gray2 = gray[fx:fx + fh, fy:fy + fw * 2]
						roi_color2 = img[fx:fx + fh, fy:fy + fw * 2]
						mouth = mouth_cascade.detectMultiScale(roi_color2)
				#print ( "'''''")
				#print( fx )
				#print ( fy )
			#for (mx,my,mw,mh) in mouth:
			#	i = mx+ 1
			#	cv2.rectangle(roi_color2, (mx, my),(mx+mw, my+mh),(0,0,255),2)


	cv2.imshow('img', img)
	k = cv2.waitKey(10) & 0xff
	if k == 27:
		break
cap.release()
cv2.destroyAllWindows()
