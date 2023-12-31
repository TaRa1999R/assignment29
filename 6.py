
import cv2

room = cv2.imread ("inputs\input_6_room.jpg")
floor = cv2.imread ("inputs\input_6_floor.jpg")
mask = cv2.imread ("inputs\input_6_mask.jpg")

mask = mask / 255.0
masked_floor = floor * mask

cv2.imshow ("Virtual Decoration" , masked_floor)
cv2.waitKey ()