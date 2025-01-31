import cv2

def preprocess_image(image_path):
    # Example: Convert image to grayscale and resize
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (256, 256))
    return image