# here the negetive files are in the bg.txt as path to the images and 
# info.lst contains the image of the positive image with starting location of the object then width and hight respectively 

##  creating positive samples via open cv2
opencv_createsamples -img img0.png -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 8000
opencv_createsamples -info info/info.lst -num 8000 -w 20 -h 20 -vec positives.vec

## training the cascade with twice the number of the subject with respect to negetive samples 
opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 2000 -numNeg 1000 -numStages 50 -w 20 -h 20
