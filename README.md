# Smart Image Analysis and Classification System

A modular Computer Vision project that combines OpenCV preprocessing,
handcrafted visual features, Random Forest classification, image analysis,
evaluation metrics, and an optional Flask demonstration interface.

## 1. Objectives
- Build a complete computer-vision processing pipeline.
- Demonstrate preprocessing and feature extraction.
- Train and evaluate an image classifier.
- Provide reproducible command-line execution.
- Present interpretable image measurements and evaluation results.

## 2. Functional Modules
1. Image preprocessing: resizing, grayscale conversion, denoising and Canny edges.
2. Feature extraction: grayscale histogram, hue histogram and edge density.
3. Classification: Random Forest model trained on user-provided classes.
4. Analysis/evaluation: image statistics, accuracy, classification report and confusion matrix.

## 3. Technologies
- Python
- OpenCV
- NumPy
- Scikit-learn
- Matplotlib
- Flask
- Joblib

## 4. Project Structure
```text
app.py
train.py
evaluate.py
predict.py
requirements.txt
modules/
tests/
data/
input/
output/
templates/
static/
docs/
```

## 5. Environment Setup

Python 3.10+ is recommended.

### Windows
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### Linux/macOS
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 6. Add Dataset
Read `data/README.md`.

Create:
```text
data/train/class_a/
data/train/class_b/
data/test/class_a/
data/test/class_b/
```

Add your own labeled images. The class names can be changed to meaningful
categories for your experiment.

## 7. Train
```bash
python train.py
```

This creates:
```text
output/model.joblib
```

## 8. Evaluate
```bash
python evaluate.py
```

Outputs:
- `output/metrics.json`
- `output/confusion_matrix.png`

## 9. Predict One Image
```bash
python predict.py input/example.jpg
```

The terminal prints the predicted class, confidence, resolution, brightness,
edge density and saturation.

## 10. Run Web Demo
```bash
python app.py
```
Open the local address shown by Flask in a browser and upload an image.

The web interface is only a demonstration layer; the core project remains
fully executable from the command line.

## 11. Run Tests
```bash
python -m pytest -q
```

## 12. Model Selection Rationale
A Random Forest classifier is used because it works well with compact
handcrafted feature vectors, requires relatively little preprocessing, and is
simple to inspect and explain in an academic project. The feature vector uses
image intensity distribution, hue distribution and edge density.

## 13. Evaluation Methodology
The dataset is divided into independent training and testing folders.
Accuracy and a classification report are generated on the test set. A
confusion matrix is saved to visualize class-wise prediction behavior.

Do not reuse test images during training.

## 14. Non-Functional Requirements
- Performance: resize images to a fixed size and use a compact feature vector.
- Usability: provide simple CLI commands and an optional web interface.
- Reliability: validate image loading and model availability.
- Maintainability: separate preprocessing, features, classification, analysis
  and evaluation into modules.
- Resource efficiency: use a small Random Forest and fixed-size features.

## 15. Limitations
The model depends strongly on the quality and representativeness of the
user-provided dataset. Handcrafted histogram features cannot capture complex
semantic information as effectively as modern deep-learning models.

## 16. Future Enhancements
- Add transfer learning with a pretrained CNN.
- Support multiclass datasets with automated dataset statistics.
- Add data augmentation.
- Add precision/recall charts and per-class visualizations.
- Add model comparison between Random Forest, SVM and a CNN.
