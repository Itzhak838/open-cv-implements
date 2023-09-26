"""
The script is designed to compress an image (lose compression) by known ratio and spread it.
It can be used to evaluate the performance of neural networks or optical systems
"""
import cv2 as cv
import math
from skimage.transform import resize
import skimage

path = "path_to_image.jpg"
image_input = cv.imread(path)  # read the image by path
pixels_2_one_pixel = 4  # compression ratio 4:1
scale = 1 / math.sqrt(pixels_2_one_pixel)  # calculate the scale factor to resize the image by the compression ratio
resized_image = resize(image_input, (image_input.shape[0] * scale, image_input.shape[1] * scale), mode='constant',
                       anti_aliasing=False)  # resize the image by the scale factor
rescaled_image = resize(resized_image, (image_input.shape[0], image_input.shape[1]),
                        anti_aliasing=False)  # rescale the image to the original size (spread)
rescaled_image = skimage.img_as_ubyte(rescaled_image)  # convert the array to uint8
cv.imwrite("path_to_write", rescaled_image)  # save the image
