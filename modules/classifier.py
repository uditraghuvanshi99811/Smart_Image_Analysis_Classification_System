from pathlib import Path
import cv2
import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from .feature_extraction import FeatureExtractor

class ImageClassifier:
    def __init__(self, model_path="output/model.joblib"):
        self.model_path = Path(model_path)
        self.extractor = FeatureExtractor()
        self.model = None
        if self.model_path.exists():
            self.model = joblib.load(self.model_path)

    def load_dataset(self, root):
        root = Path(root)
        X, y = [], []
        for class_dir in sorted(p for p in root.iterdir() if p.is_dir()):
            for path in sorted(class_dir.iterdir()):
                if path.suffix.lower() not in {".jpg", ".jpeg", ".png", ".bmp", ".webp"}:
                    continue
                image = cv2.imread(str(path))
                if image is not None:
                    X.append(self.extractor.extract(image))
                    y.append(class_dir.name)
        if not X:
            raise ValueError(f"No valid images found in {root}")
        return np.array(X), np.array(y)

    def train(self, train_dir):
        X, y = self.load_dataset(train_dir)
        self.model = RandomForestClassifier(
            n_estimators=120, random_state=42, class_weight="balanced"
        )
        self.model.fit(X, y)
        self.model_path.parent.mkdir(parents=True, exist_ok=True)
        joblib.dump(self.model, self.model_path)
        return {"samples": len(y), "classes": sorted(set(y))}

    def predict(self, image):
        if self.model is None:
            raise ValueError("Model not trained. Run train.py first.")
        x = self.extractor.extract(image).reshape(1, -1)
        label = self.model.predict(x)[0]
        confidence = float(max(self.model.predict_proba(x)[0]))
        return label, confidence

    def evaluate(self, test_dir):
        X, y = self.load_dataset(test_dir)
        pred = self.model.predict(X)
        return {
            "accuracy": float(accuracy_score(y, pred)),
            "report": classification_report(y, pred, output_dict=True, zero_division=0),
            "confusion_matrix": confusion_matrix(y, pred).tolist(),
            "classes": sorted(set(y))
        }
