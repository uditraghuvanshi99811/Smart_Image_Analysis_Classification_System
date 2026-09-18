import numpy as np
from modules.feature_extraction import FeatureExtractor

def test_feature_length():
    image = np.zeros((128, 128, 3), dtype=np.uint8)
    features = FeatureExtractor().extract(image)
    assert features.shape == (49,)
    assert np.isfinite(features).all()
