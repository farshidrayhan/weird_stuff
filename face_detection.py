import numpy as np
import cv2

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
import time

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
left_eye_cascade =  cv2.CascadeClassifier('haarcascade_lefteye_2splits.xml')

smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
calculator_cascade = cv2.CascadeClassifier('calculator_cascade.xml')

cap = cv2.VideoCapture(0)
i = 0
while True:

    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)


    calculator = calculator_cascade.detectMultiScale(gray)#, 2,7)

    for (x, y, w, h) in calculator:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255),2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,'farshid',(x-w,y-h),font,.5,(0,255,255) , 2 , cv2.LINE_AA)
    # roi_color = [1,2,4,5]
    # smile_image = np.array(roi_color)
    # print(faces)

    # cv2.imshow('',faces)

    for (x, y, w, h) in faces:
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,'face', (x - w, y - h), font, 0.5, (0, 255, 255), 2)

        # i += 1
        # img_name = 'img'+ str(i) + '.png'
        # print(img_name)

        # cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # resized_image = cv2.resize(img, (w, h))

        # cv2.imshow('face Detector',resized_image)
        # print("face detected ")
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

        # cv2.imshow('face Detector', roi_color)
        resized_image = cv2.resize(roi_gray, (100, 100))

        # cv2.imwrite('uglies/'+img_name, resized_image)

        eyes = eye_cascade.detectMultiScale(roi_gray)

        for (ex, ey, ew, eh) in eyes:
            # cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 1)

            eye_image = roi_color[ey:ey + eh, ex:ex + ew]
            #
            # cv2.imshow('eye Detector', eye_image)
            # print(eye_image)

        # smile = smile_cascade.detectMultiScale(roi_gray)
        # print(smile)
        # for (ex, ey, ew, eh) in smile:
        #     cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 1)
        #
        #     smile_color = roi_color[ey:ey + eh, ex:ex + ew]
            # cv2.imshow('smile detector', smile_color)

    cv2.imshow('Image Detector', img)
# cv2.imshow('Detector', smile_image)


# cv2.imshow('Image Detector gray', roi_color)

# time.sleep(2)


    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
