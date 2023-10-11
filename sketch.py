import cv2

image = cv2.imread("healthy_apple.jpg")
grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_image)
blur = cv2.GaussianBlur(invert, (99,99), 0)
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey_image, invertedblur, scale=250.0)

cv2.imwrite("Sketch.png",sketch)