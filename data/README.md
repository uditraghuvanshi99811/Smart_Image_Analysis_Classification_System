# Sample Data Instructions

The repository intentionally does not contain a large image dataset.

Create this structure:

data/
  train/
    class_a/
    class_b/
  test/
    class_a/
    class_b/

Put your own images into the folders. For example, `class_a` and `class_b`
can represent two visually distinguishable categories relevant to your
demonstration. Use at least 20 images per class for a small demo and more
for a meaningful evaluation.

Keep train and test images separate. Do not use the same image in both sets.

Supported formats: JPG, JPEG, PNG, BMP, WEBP.

After adding images:
    python train.py
    python evaluate.py
