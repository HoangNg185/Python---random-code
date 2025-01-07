import cv2

img = cv2.imread('Rabbit.jpg')

blurred = cv2.GaussianBlur(img, (5, 5), 0)  # Gaussian Blur
median = cv2.medianBlur(img, 5)  # Median Blur
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)  # Binary threshold
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
dilated = cv2.dilate(binary, kernel, iterations=1)
eroded = cv2.erode(binary, kernel, iterations=1)

edges = cv2.Canny(img, 100, 200)
cv2.imshow('Original Image', img)
cv2.imshow('Blurred Image', blurred)
cv2.imshow('Median Blurred Image', median)
cv2.imshow('Binary Threshold Image', binary)
cv2.imshow('Dilated Image', dilated)
cv2.imshow('Eroded Image', eroded)
cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
