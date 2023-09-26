"""
The script is designed to add a colored Gaussian noise to an image in three channels.
"""
import cv2 as cv
import numpy as np

# Load the image
path = "path_to_image"
# Read the image
image = cv.imread(path)

# Convert the image to float32
image = np.float32(image) / 255.0

# Set the mean and standard deviation for Gaussian noise
mean = 0
stddev = 0.1

# Generate Gaussian noise
noise = np.random.normal(mean, stddev, image.shape).astype(np.float32)

# Add noise to the image
noisy_image = cv.add(image, noise)

# Clip the pixel values to the range [0, 1]
noisy_image = np.clip(noisy_image, 0, 1)

# Convert the noisy image back to uint8 format
noisy_image = (noisy_image * 255).astype(np.uint8)

# Display the original and noisy images
cv.imshow('Original Image', image)
cv.imshow('Noisy Image', noisy_image)
cv.waitKey(0)
cv.destroyAllWindows()

# Save the noisy image
cv2.imwrite('path_to write', noisy_image)
