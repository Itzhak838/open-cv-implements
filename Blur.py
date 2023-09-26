"""
The script is designed to blur an image using Gaussian blur.
Target: system resolution test
"""
import cv2 as cv
# Load an image from file
image = cv.imread('input_image.jpg')

# Define the kernel size for Gaussian blur
kernel_size = (5, 5)  # Adjust the kernel size as needed (e.g., (3, 3), (7, 7), etc.)

# Apply Gaussian blur to the image
blurred_image = cv.GaussianBlur(image, kernel_size, 0)

# Save the blurred image to a file (optional)
cv.imwrite('blurred_image.jpg', blurred_image)

# Display the original and blurred images (optional)
cv.imshow('Original Image', image)
cv.imshow('Blurred Image', blurred_image)
cv.waitKey(0)
cv.destroyAllWindows()
