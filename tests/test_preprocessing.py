import numpy as np
from modules.image_preprocessing import ImagePreprocessor

def test_resize_and_grayscale():
    image = np.zeros((50, 80, 3), dtype=np.uint8)
    p = ImagePreprocessor()
    resized = p.resize(image)
    gray = p.grayscale(resized)
    assert resized.shape == (128, 128, 3)
    assert gray.shape == (128, 128)
