import cv2
import pytesseract

def ocr(img):
    text = pytesseract.image_to_string(img)
    return text

img = cv2.imread('img.jpg')

def gray(image):
    return cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

print(gray(img))