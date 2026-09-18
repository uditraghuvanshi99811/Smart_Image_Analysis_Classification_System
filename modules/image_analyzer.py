import cv2
import numpy as np

class ImageAnalyzer:
    def analyze(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 80, 160)
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        return {
            "width": int(image.shape[1]),
            "height": int(image.shape[0]),
            "channels": int(image.shape[2]) if len(image.shape) == 3 else 1,
            "mean_brightness": round(float(gray.mean()), 2),
            "edge_density": round(float((edges > 0).mean()), 4),
            "mean_saturation": round(float(hsv[:, :, 1].mean()), 2)
        }

    def save_edge_image(self, image, output_path):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 80, 160)
        cv2.imwrite(str(output_path), edges)
