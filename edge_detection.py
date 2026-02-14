import cv2
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# Step 1: Load the image
# -------------------------------
image = cv2.imread('low_contrast.jpg')  # Replace 'image.jpg' with your image path

if image is None:
    print("Error: Image not found!")
    exit()

# -------------------------------
# Step 2: Convert to Grayscale
# -------------------------------
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# -------------------------------
# Step 3: Histogram Equalization
# -------------------------------
hist_eq = cv2.equalizeHist(gray) 

# -------------------------------
# Step 4: CLAHE (Better Contrast Enhancement)
# -------------------------------
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
clahe_img = clahe.apply(gray)

# -------------------------------
# Step 5: Edge Detection
# -------------------------------

# Sobel Edge Detection
sobel_x = cv2.Sobel(clahe_img, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(clahe_img, cv2.CV_64F, 0, 1, ksize=3)
sobel_edge = cv2.magnitude(sobel_x, sobel_y)

# Canny Edge Detection
canny_edge = cv2.Canny(clahe_img, 50, 150)

# -------------------------------
# Step 6: Display Results
# -------------------------------
titles = [
    "Original Grayscale",
    "Histogram Equalized",
    "CLAHE Enhanced",
    "Sobel Edge Detection",
    "Canny Edge Detection"
]

images = [
    gray,
    hist_eq,
    clahe_img,
    sobel_edge,
    canny_edge
]

plt.figure(figsize=(12, 8))

for i in range(len(images)):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()
