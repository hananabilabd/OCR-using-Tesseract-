# USAGE
# python ocr.py --image images/example_01.png 
# python ocr.py --image images/example_02.png  --preprocess blur

# import the necessary packages
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd =  'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'
import argparse
import cv2
import os

# load the example image and convert it to grayscale
image = cv2.imread("images/English1.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Image", gray)

# check to see if we should apply thresholding to preprocess the image

gray = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# make a check to see if median blurring should be done to remove noise
#gray = cv2.medianBlur(gray, 3)

# write the grayscale image to disk as a temporary file so we can
# apply OCR to it
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file
text = pytesseract.image_to_string(Image.open(filename))
# French text image to string

os.remove(filename)
print(text)
###########
print(pytesseract.image_to_string(Image.open('images/french2.jpg'), lang='fra'))
print(pytesseract.image_to_string(Image.open('images/arabic2.jpg'), lang='ara'))
print(pytesseract.image_to_string(Image.open('images/arabic5.jpg'), lang='ara'))

cv2.imshow("Output", gray)
cv2.waitKey(0)