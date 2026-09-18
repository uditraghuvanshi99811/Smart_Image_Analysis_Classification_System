# System Architecture

```text
                 +------------------+
                 |   Input Image    |
                 +--------+---------+
                          |
                          v
                +--------------------+
                | Image Preprocessing|
                | resize / gray /    |
                | denoise / edges    |
                +---------+----------+
                          |
                          v
                +--------------------+
                | Feature Extraction |
                | histograms + edges |
                +---------+----------+
                          |
             +------------+------------+
             |                         |
             v                         v
    +----------------+       +------------------+
    | Random Forest  |       | Image Analyzer   |
    | Classification |       | brightness/edges |
    +-------+--------+       +--------+---------+
            |                         |
            +------------+------------+
                         v
                +--------------------+
                | Results & Metrics  |
                +--------------------+
```

## Components
- `ImagePreprocessor`: prepares raw images.
- `FeatureExtractor`: converts images into numerical feature vectors.
- `ImageClassifier`: trains, predicts and evaluates the model.
- `ImageAnalyzer`: calculates image-level measurements.
- `Evaluator`: creates evaluation visualizations.
- Flask `app.py`: optional presentation layer.
