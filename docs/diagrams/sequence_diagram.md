# Sequence Diagram

```text
User -> CLI: python predict.py image.jpg
CLI -> ImageClassifier: load model
CLI -> OpenCV: read image
CLI -> ImageClassifier: predict(image)
ImageClassifier -> FeatureExtractor: extract(image)
FeatureExtractor --> ImageClassifier: feature vector
ImageClassifier --> CLI: class + confidence
CLI -> ImageAnalyzer: analyze(image)
ImageAnalyzer --> CLI: image statistics
CLI --> User: prediction + analysis
```
