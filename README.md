# Edge_Detection_Project
# Edge-Detection-using-OpenCV
Edge Detection and Contrast Enhancement using OpenCV
Project Overview

This project demonstrates image contrast enhancement and edge detection techniques using Python and OpenCV. It improves low-contrast images and detects edges using advanced image processing methods.

The project applies:

Histogram Equalization

CLAHE (Contrast Limited Adaptive Histogram Equalization)

Sobel Edge Detection

Canny Edge Detection

This helps in improving image quality and extracting important structural information.

Features

Load and process low contrast images

Convert image to grayscale

Enhance contrast using Histogram Equalization

Improve contrast using CLAHE

Detect edges using:

Sobel Edge Detection

Canny Edge Detection

Display all processing results using Matplotlib

Technologies Used

Python

OpenCV (cv2)

NumPy

Matplotlib

Project Structure
Edge-Detection-Project/
│
├── edge_detection.py
├── low_contrast.jpg
└── README.md

Installation
Step 1: Install Python (if not installed)

Download from: https://www.python.org/

Step 2: Install required libraries

Run this command in terminal or VS Code:

pip install opencv-python numpy matplotlib

How to Run the Project

Step 1: Place your image file
Example: low_contrast.jpg

Step 2: Run the Python file

python edge_detection.py


Step 3: Output window will display:

Original Grayscale Image

Histogram Equalized Image

CLAHE Enhanced Image

Sobel Edge Detection

Canny Edge Detection
