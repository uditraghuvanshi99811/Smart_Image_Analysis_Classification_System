import numpy as np
from modules.image_analyzer import ImageAnalyzer

def test_analyzer_output():
    image = np.zeros((20, 30, 3), dtype=np.uint8)
    result = ImageAnalyzer().analyze(image)
    assert result["width"] == 30
    assert result["height"] == 20
    assert result["channels"] == 3
