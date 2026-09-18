# Class Diagram

```text
+------------------------+
| ImagePreprocessor      |
+------------------------+
| load()                 |
| resize()               |
| grayscale()            |
| denoise()              |
| edges()                |
| process()              |
+------------------------+

+------------------------+
| FeatureExtractor      |
+------------------------+
| extract()              |
| feature_names()        |
+------------------------+

+------------------------+
| ImageClassifier        |
+------------------------+
| load_dataset()         |
| train()                |
| predict()              |
| evaluate()             |
+------------------------+

+------------------------+
| ImageAnalyzer          |
+------------------------+
| analyze()              |
| save_edge_image()      |
+------------------------+

+------------------------+
| Evaluator              |
+------------------------+
| save_confusion_matrix()|
+------------------------+

FeatureExtractor <--- ImageClassifier
ImageAnalyzer    <--- app.py
Evaluator        <--- evaluate.py
```
