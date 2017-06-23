import cv2
import numpy as np
import os

def find_uglies():
    match = False

    counter = 0

    for file_type in ['neg']:
        # print(file_type)
        for img in os.listdir(file_type):

            for ugly in os.listdir('uglies'):
                try:
                    # print(str(file_type)+'/'+str(img))
                    current_image_path = str(file_type)+'/'+str(img)
                    ugly = cv2.imread('uglies/'+str(ugly))
                    question = cv2.imread(current_image_path)
                    if ugly.shape == question.shape and not(np.bitwise_xor(ugly,question).any()):
                        # print('That is one ugly pic! Deleting!')
                        # print(current_image_path)
                        os.remove(current_image_path)
                        counter += 1
                except Exception as e:
                    print(str(e))
                    os.remove(current_image_path)
                    counter = counter+1

    print('deleted ' , counter , ' images')

find_uglies()