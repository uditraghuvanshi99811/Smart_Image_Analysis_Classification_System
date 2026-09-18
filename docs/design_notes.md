# Design Notes

## Input
Images in common formats such as JPG, PNG, BMP and WEBP.

## Processing
Images are resized to 128x128. Grayscale and HSV representations are used
for compact histogram-based features. Canny edge detection provides an edge
density feature.

## Output
For a new image:
- predicted class
- model confidence
- resolution
- mean brightness
- edge density
- mean saturation

## Reproducibility
The Random Forest uses `random_state=42`. Keep the training and test folders
separate and document the exact dataset counts in the final report.
