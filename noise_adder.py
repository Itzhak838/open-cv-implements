"""
The script is designed to add a Gaussian noise to the image channels

"""
import cv2 as cv
import numpy as np

path = "cat.jpeg"  # path to image
image_input = cv.imread(path, cv.IMREAD_UNCHANGED)  # read the image as is

# display the input image
cv.imshow("input image", image_input)
cv.waitKey(1000)  # show for a few seconds

# create a matrix with random gaussian values
# mean, std_division (mu), image dimension typed to uint8 (image format)
noise_mat = np.random.normal(0, 50, (image_input.shape[0], image_input.shape[1])).astype(np.uint8)
# convert to 3 dimensions - without it, the noise_mat is suitable gray images
noise_mask = np.zeros((image_input.shape[0], image_input.shape[1], 3), dtype=np.uint8)
# convert to one noisy channel: choose the color by the numbers bellow
blue = 0
green = 1
red = 2
noise_mask[:, :, red] = noise_mat

cv.imshow("red noise", noise_mask)
cv.waitKey(10000)
noisy_image = cv.add(image_input, noise_mask)
cv.imshow("noisy image", noisy_image)
cv.waitKey(10000)
# save the image by the path bellow
save_path = "noisy_image.jpeg"
cv.imwrite(save_path, noisy_image)
