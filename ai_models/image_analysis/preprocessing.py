import cv2
import numpy as np

def preprocess_image(image_path):
    """
    Preprocess a medical image for CNN input.
    """
    # Load image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Resize image to 256x256
    image = cv2.resize(image, (256, 256))
    
    # Normalize pixel values to [0, 1]
    image = image / 255.0
    
    # Add batch dimension
    image = np.expand_dims(image, axis=0)
    image = np.expand_dims(image, axis=0)
    
    return image