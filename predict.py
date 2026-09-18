import argparse
import cv2
from modules.classifier import ImageClassifier
from modules.image_analyzer import ImageAnalyzer

parser = argparse.ArgumentParser(description="Classify and analyze an image.")
parser.add_argument("image", help="Path to an image")
args = parser.parse_args()

clf = ImageClassifier()
if clf.model is None:
    raise SystemExit("Model not found. Run: python train.py")

image = cv2.imread(args.image)
if image is None:
    raise SystemExit("Could not read the image.")

label, confidence = clf.predict(image)
stats = ImageAnalyzer().analyze(image)

print(f"Prediction: {label}")
print(f"Confidence: {confidence:.2%}")
print(f"Resolution: {stats['width']} x {stats['height']}")
print(f"Mean brightness: {stats['mean_brightness']}")
print(f"Edge density: {stats['edge_density']}")
print(f"Mean saturation: {stats['mean_saturation']}")
