# Workflow

```text
Start
  |
  v
Load image dataset
  |
  v
Validate image files
  |
  v
Resize images
  |
  v
Convert to grayscale / HSV
  |
  v
Extract histograms + edge density
  |
  v
Train Random Forest
  |
  v
Save model
  |
  v
Evaluate on separate test set
  |
  +--> Accuracy / Classification Report
  |
  +--> Confusion Matrix
  |
  v
Load new image
  |
  v
Predict class + confidence
  |
  v
Display image statistics
  |
  v
End
```
