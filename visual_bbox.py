import cv2
import numpy as np

# Class names for bounding boxes
# Define the paths and classes
SOURCE_IMAGE_PATH = "artifacts/helmet.jpeg"
TARGET_IMAGE_PATH = "artifacts/helmet3.jpeg"
NAMES = ["head", "helmet"]

# Global variables to store bounding box data
bbox_list = []
drawing = False  # Flag to indicate if the user is drawing a rectangle
start_x, start_y = -1, -1  # Starting points for the rectangle
current_class_idx = 0  # Default class index for bounding boxes

# Mouse callback function to draw rectangles
def draw_bbox(event, x, y, flags, param):
    global start_x, start_y, drawing, img_copy, bbox_list, current_class_idx

    if event == cv2.EVENT_LBUTTONDOWN:
        # Starting point of rectangle
        drawing = True
        start_x, start_y = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            img_copy = img.copy()  # Copy the original image to show the current rectangle
            cv2.rectangle(img_copy, (start_x, start_y), (x, y), (0, 255, 0), 2)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        # Save the bounding box
        bbox_list.append((start_x, start_y, x, y, NAMES[current_class_idx]))  # Add class info
        cv2.rectangle(img_copy, (start_x, start_y), (x, y), (0, 255, 0), 2)
        # Put the class name label
        cv2.putText(img_copy, f'Class: {NAMES[current_class_idx]}', (start_x, start_y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

# Load the image
img = cv2.imread(SOURCE_IMAGE_PATH)
img_copy = img.copy()

# Set up OpenCV window and mouse callback
cv2.namedWindow('Image')
cv2.setMouseCallback('Image', draw_bbox)

# Display the image and wait for user input
while True:
    cv2.imshow('Image', img_copy)

    # Wait for user input
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):  # Press 'q' to quit
        break
    elif key == ord('n'):  # Press 'n' to change class to the next one
        current_class_idx = (current_class_idx + 1) % len(NAMES)  # Cycle through the classes

# Clean up and close
cv2.destroyAllWindows()

# Print out bounding boxes and their respective classes
print("Bounding boxes:")
for bbox in bbox_list:
    print(f"Class: {bbox[4]}, Coordinates: {bbox[:4]}")

# Optionally, save the image with the bounding boxes drawn
cv2.imwrite(TARGET_IMAGE_PATH, img_copy)
print(f"Image with bounding boxes saved to {TARGET_IMAGE_PATH}")
