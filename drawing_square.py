"""
The script is designed to draw a square in the center of the image and enlarge it by d_square list.
Target: system resolution test
"""
import cv2 as cv
img = cv.imread("C:\\Itzhak\\BSc\\4yr\\Final_Project\\pythonProject\\yolov8-silva\\inference\\images\\data_all\\d_g_3.jpg")

# img[up:down right:left]=B, G, R while img is a 3D matrix representing an image
print("image dimensions: ", img.shape)
# cv.imshow("bird", img)
# cv.waitKey(0)
d_square = [1, 2, 4, 8, 16, 32, 64, 96, 128, 192, 256, 320, 384, 448, 512, 576, 640, 704, 768, 832, 896, 960, 1024]
x_center = img.shape[0]//2
y_center = img.shape[1]//2
print("x_center: ", x_center, "y_center: ", y_center)
for i in d_square:
    for j in [i]:
        if (x_center - j//2 >= 0) and (y_center - j//2 >= 0) and (x_center + j//2 <= img.shape[0]) and (y_center + j//2 <= img.shape[1]):
            img[x_center-j//2:x_center + j//2, y_center - j//2:y_center + j//2] = 0, 0, 0
            print((x_center - j//2) - (x_center + j//2), " : ", (y_center - j//2) - (y_center + j//2))
            cv.imshow(str(j), img)  # j*j is the dimension of the square
            cv.waitKey(0)
