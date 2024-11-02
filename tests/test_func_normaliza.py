import sys
import os
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_normaliza():
    import codigo_estudiante as micodigo
    img = Image.open(os.path.join("data","imagen0.png"))
    Inorm = micodigo.normaliza(img)
    # Aplanar la matriz para calcular el histograma
    valores = Inorm.flatten()
    assert valores.max() == 1.0
    assert valores.min() == 0.0