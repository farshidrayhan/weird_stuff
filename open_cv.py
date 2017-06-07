import numpy as np
from PIL import ImageGrab
import cv2
import time

def precess_img(original_img):
    precessed_img = cv2.cvtColor(original_img,cv2.COLOR_BGR2GRAY)
    precessed_img = cv2.Canny(precessed_img,threshold1 = 200, threshold2 = 300)

    return precessed_img



if __name__ == '__main__':

    last_time = time.time()
    frame_counter = 0
    while(True):
        frame_counter += 1
        screen = np.array(  ImageGrab.grab(bbox=(50,50,640,480)) )
        new_screen = precess_img(screen)
        # printscreen_numpy =   np.array(printscreen_pil.getdata(),dtype='uint8')\
        # .reshape((printscreen_pil.size[1],printscreen_pil.size[0],3))
        cv2.imshow('streaming 2 gray',new_screen )
        cv2.imshow('streaming',cv2.cvtColor( screen,cv2.COLOR_BGR2RGB ) )
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
        if float( format(time.time()-last_time) ) >= 1:
            print('FPS : ',frame_counter)
            last_time = time.time()
            frame_counter = 0
