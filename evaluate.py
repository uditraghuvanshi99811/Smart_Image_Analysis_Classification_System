import json
from modules.classifier import ImageClassifier
from modules.evaluator import Evaluator

if __name__ == "__main__":
    clf = ImageClassifier()
    if clf.model is None:
        raise SystemExit("Model not found. Run: python train.py")
    result = clf.evaluate("data/test")
    with open("output/metrics.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
    Evaluator().save_confusion_matrix(
        result["confusion_matrix"], result["classes"], "output/confusion_matrix.png"
    )
    print(f"Accuracy: {result['accuracy']:.2%}")
    print("Saved metrics to output/metrics.json")
    print("Saved confusion matrix to output/confusion_matrix.png")
