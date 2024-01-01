
import cv2
import numpy as np 

first_photo = cv2.imread ("inputs/input_face.jpg")
second_photo = cv2.imread ("inputs\input_mom.jpg")

result = (first_photo + second_photo)/2

cv2.imwrite ("outputs\output_1_face_morphing.jpg" , result)