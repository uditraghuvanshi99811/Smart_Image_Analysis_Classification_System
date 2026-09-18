import cv2
import numpy as np

class ImagePreprocessor:
    def load(self, path):
        image = cv2.imread(str(path))
        if image is None:
            raise ValueError(f"Could not read image: {path}")
        return image

    def resize(self, image, size=(128, 128)):
        return cv2.resize(image, size, interpolation=cv2.INTER_AREA)

    def grayscale(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    def denoise(self, gray):
        return cv2.GaussianBlur(gray, (5, 5), 0)

    def edges(self, gray):
        return cv2.Canny(gray, 80, 160)

    def process(self, path):
        image = self.load(path)
        resized = self.resize(image)
        gray = self.grayscale(resized)
        clean = self.denoise(gray)
        edges = self.edges(clean)
        return image, resized, gray, clean, edges
