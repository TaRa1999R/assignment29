
import cv2

full_text = cv2.imread ("inputs\input_4_full.png")
code_breaker = cv2.imread ("inputs\input_4_check.png")

full_text = 
secret_text = cv2.subtract (full_text , code_breaker)

cv2.imshow ("Secret Text" , secret_text)
cv2.waitKey ()