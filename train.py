from modules.classifier import ImageClassifier

if __name__ == "__main__":
    clf = ImageClassifier()
    info = clf.train("data/train")
    print("Training complete.")
    print(f"Images: {info['samples']}")
    print(f"Classes: {', '.join(info['classes'])}")
