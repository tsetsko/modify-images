import os
import cv2

folder_path = '/Users/tdonov/Desktop/Python/modify images/images/sample_images'
filepath = [os.path.join(folder_path, name) for name in os.listdir(folder_path)]

print(filepath)

def modify_image(list):
    for i in list:
        name = i.split('/')[-1]
        img = cv2.imread(i, 0)
        resized_image = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
        cv2.imwrite(('resized' + name), resized_image)
        print(name)
        print(img.shape)

modify_image(filepath)
