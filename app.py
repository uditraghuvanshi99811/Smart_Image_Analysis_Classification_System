from pathlib import Path
import cv2
from flask import Flask, render_template, request
from modules.classifier import ImageClassifier
from modules.image_analyzer import ImageAnalyzer

app = Flask(__name__)
UPLOAD = Path("input")
UPLOAD.mkdir(exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    clf = ImageClassifier()
    if request.method == "POST":
        file = request.files.get("image")
        if not file or not file.filename:
            error = "Please choose an image."
        elif clf.model is None:
            error = "Model not found. Train it first with: python train.py"
        else:
            path = UPLOAD / file.filename
            file.save(path)
            image = cv2.imread(str(path))
            if image is None:
                error = "The uploaded file is not a valid image."
            else:
                label, confidence = clf.predict(image)
                stats = ImageAnalyzer().analyze(image)
                result = {"label": label, "confidence": f"{confidence:.2%}", **stats}
    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
