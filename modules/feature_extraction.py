import cv2
import numpy as np

class FeatureExtractor:
    def extract(self, image):
        image = cv2.resize(image, (128, 128))
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        hist = cv2.calcHist([gray], [0], None, [32], [0, 256]).flatten()
        hist = hist / (hist.sum() + 1e-8)

        edges = cv2.Canny(gray, 80, 160)
        edge_density = np.array([edges.mean() / 255.0])

        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        color_hist = cv2.calcHist([hsv], [0], None, [16], [0, 180]).flatten()
        color_hist = color_hist / (color_hist.sum() + 1e-8)

        return np.concatenate([hist, color_hist, edge_density]).astype(np.float32)

    def feature_names(self):
        return [f"gray_hist_{i}" for i in range(32)] +                [f"hue_hist_{i}" for i in range(16)] + ["edge_density"]
