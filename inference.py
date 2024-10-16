import os
import cv2
import random
from ultralytics import YOLO

model = YOLO('runs/detect/train22/weights/best.pt')

path = 'datasets/multicontainer/test'
imgp = path+'/images/'
num_images = 3
images = random.sample(os.listdir(imgp), num_images)
# # Show the results
for image in images:
     imgpath = imgp+image
     results = model(imgpath)
     r = results[0]
     im_array = r.plot()  # plot a BGR numpy array of predictions
     # cv2.imwrite('predicted.png',im_array)
     cv2.namedWindow("asd", cv2.WINDOW_NORMAL)  
     cv2.imshow('asd',im_array)
     cv2.waitKey(0)
     cv2.destroyAllWindows()

