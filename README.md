# Smart Image Analysis and Classification System

## Project Overview

The Smart Image Analysis and Classification System is a Computer Vision and Machine Learning project that analyzes an input image and classifies it as a **Cat** or **Dog**.

The system performs image preprocessing, extracts visual features, uses a Random Forest classifier for prediction, and provides additional image statistics such as resolution, brightness, edge density, and saturation.

The project provides both a **Flask-based web interface** and a **command-line interface (CLI)**.

## Problem Statement

Manual image classification can be time-consuming when a large number of images need to be analyzed. This project aims to develop a computer vision system that can automatically analyze an image, extract meaningful visual information, and classify it as a cat or dog.

## Objectives

- Develop an image classification system using Computer Vision techniques.
- Preprocess input images before classification.
- Extract meaningful visual features from images.
- Train a machine learning model for classification.
- Analyze additional properties of the input image.
- Provide an easy-to-use web interface.
- Evaluate the performance of the trained model.
- Implement automated tests for important modules.

## Main Features

- Cat/Dog image classification
- Image upload through Flask web interface
- Command-line prediction
- Image preprocessing
- Grayscale conversion
- Gaussian blurring
- Canny edge detection
- Grayscale histogram extraction
- Hue histogram extraction
- Edge-density calculation
- Random Forest classification
- Prediction confidence
- Image resolution analysis
- Mean brightness analysis
- Mean saturation analysis
- Model evaluation
- Confusion matrix generation
- Automated unit testing

## Technologies Used

- Python
- OpenCV
- NumPy
- scikit-learn
- Flask
- Matplotlib
- Pillow
- pytest
- Git and GitHub

## System Workflow

```text
Input Image
     |
     v
Image Preprocessing
     |
     v
Feature Extraction
     |
     v
Random Forest Classifier
     |
     +----> Prediction
     |
     +----> Confidence
     |
     v
Image Analysis
     |
     v
Final Results
```

## Dataset

The project uses the Microsoft Cats and Dogs image dataset.

The dataset is organized as:

```text
data/
├── train/
│   ├── cats/
│   └── dogs/
│
└── test/
    ├── cats/
    └── dogs/
```

For this project experiment:

| Dataset | Cats | Dogs | Total |
|---|---:|---:|---:|
| Training | 80 | 80 | 160 |
| Testing | 20 | 20 | 40 |

The dataset images are not included in the GitHub repository.

## Feature Extraction

The system extracts a 49-dimensional feature vector from each image:

- 32 grayscale histogram features
- 16 hue histogram features
- 1 edge-density feature

```text
Total Features = 32 + 16 + 1 = 49
```

## Machine Learning Model

The project uses a **Random Forest Classifier**.

Configuration:

```text
Number of Estimators: 120
Random State: 42
Class Weight: balanced
```

## Installation

Clone the repository:

```bash
git clone https://github.com/uditraghuvanshi99811/Smart_Image_Analysis_Classification_System.git
```

Move into the project directory:

```bash
cd Smart_Image_Analysis_Classification_System
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Dataset Setup

Place the dataset images into:

```text
data/train/cats/
data/train/dogs/
data/test/cats/
data/test/dogs/
```

The folder name determines the class label.

## Training

Run:

```bash
python train.py
```

The trained model is saved locally as:

```text
output/model.joblib
```

## Evaluation

Run:

```bash
python evaluate.py
```

This generates:

```text
output/metrics.json
output/confusion_matrix.png
```

### Experimental Results

The model achieved an accuracy of **67.50%** on the selected 40-image test set.

| Metric | Cats | Dogs |
|---|---:|---:|
| Precision | 62.96% | 76.92% |
| Recall | 85.00% | 50.00% |
| F1-Score | 72.34% | 60.61% |

### Confusion Matrix

```text
                 Predicted
              Cats    Dogs
Actual Cats    17       3
Actual Dogs    10      10
```

## Command-Line Prediction

Run:

```bash
python predict.py "path/to/image.jpg"
```

Example:

```bash
python predict.py ".\data\test\cats\10069.jpg"
```

The program displays:

- Prediction
- Confidence
- Resolution
- Mean brightness
- Edge density
- Mean saturation

## Web Application

Start the Flask application:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

Upload an image to receive its classification and image-analysis results.

## Testing

Run the automated tests:

```bash
python -m pytest
```

Current test result:

```text
3 passed
```

Tests cover:

- Image preprocessing
- Feature extraction
- Image analysis

## Project Structure

```text
Smart_Image_Analysis_Classification_System/
│
├── app.py
├── train.py
├── evaluate.py
├── predict.py
├── requirements.txt
├── README.md
├── statement.md
├── .gitignore
│
├── modules/
│   ├── __init__.py
│   ├── classifier.py
│   ├── evaluator.py
│   ├── feature_extraction.py
│   ├── image_analyzer.py
│   ├── image_preprocessing.py
│   └── utils.py
│
├── tests/
│   ├── test_analyzer.py
│   ├── test_features.py
│   └── test_preprocessing.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── css/
│       └── style.css
│
├── data/
│   └── README.md
│
├── docs/
│   ├── architecture.md
│   ├── workflow.md
│   ├── design_notes.md
│   ├── report_outline.md
│   ├── report_checklist.md
│   └── diagrams/
│       ├── use_case.md
│       ├── class_diagram.md
│       └── sequence_diagram.md
│
└── output/
    └── .gitkeep
```

## Limitations

- The experiment uses a relatively small dataset.
- The system currently supports only two classes.
- The model uses handcrafted visual features.
- Performance may vary depending on image quality and characteristics.
- Deep learning approaches may provide better performance on larger datasets.

## Future Enhancements

- Increase the training dataset size.
- Add HOG and additional texture features.
- Experiment with CNN-based models.
- Use transfer learning.
- Support additional image categories.
- Add prediction history.
- Improve the web interface.
- Add more automated tests.
- Generate downloadable analysis reports.

## Documentation

Additional project documentation is available in the `docs/` directory, including:

- System architecture
- Workflow
- Design decisions
- Use case diagram
- Class diagram
- Sequence diagram
- Report outline
- Report checklist

## Author

**Udit Raghuvanshi**

**Registration No.:** 24BAI10173

**Course:** Computer Vision

**Course Code:** CSE3010

**University:** VIT Bhopal University

## GitHub Repository

https://github.com/uditraghuvanshi99811/Smart_Image_Analysis_Classification_System
