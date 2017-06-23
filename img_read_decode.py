import urllib.request
import cv2
import numpy as np
import os


def store_raw_images():
    # neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n09618957'
    # neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00007846'
    neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n00523513'
    neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
    pic_num = 5000

    if not os.path.exists('neg'):
        os.makedirs('neg')

    for i in neg_image_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, "neg/" + str(pic_num) + ".jpg")
            img = cv2.imread("neg/" + str(pic_num) + ".jpg", cv2.IMREAD_GRAYSCALE)
            # should be larger than samples / pos pic (so we can place our image on it)
            resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite("neg/" + str(pic_num) + ".jpg", resized_image)
            pic_num += 1

        except Exception as e:
            print(str(e))
def change():
    # neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n09618957'
    # neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
    pic_num = 200

    # if not os.path.exists('neg'):
    #     os.makedirs('neg')

    for file_type in ['negs']:
        # print(file_type)
        for img in os.listdir(file_type):
            try:
                print(str(file_type)+'/'+str(img))
                current_image_path = str(file_type)+'/'+str(img)
                # urllib.request.urlretrieve(i, "neg/" + str(pic_num) + ".jpg")
                img = cv2.imread(current_image_path + ".jpg", cv2.IMREAD_GRAYSCALE)

                # should be larger than samples / pos pic (so we can place our image on it)
                resized_image = cv2.resize(img, (10, 10))
                cv2.imwrite("negs/new/" + str(pic_num) + ".jpg", img)
                pic_num += 1

            except Exception as e:
                print(str(e))
store_raw_images()
# change()