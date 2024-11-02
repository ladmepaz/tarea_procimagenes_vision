import sys
import os
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_transformar_color():
    import codigo_estudiante as micodigo
    img = Image.open(os.path.join("data","imagen0.png"))
    imagen_lab = micodigo.transformar_color(img, espacio='LAB')
    imagen_ycrcb = micodigo.transformar_color(img, espacio='YCrCb')
    assert imagen_lab.mean() > 100
    assert imagen_ycrcb.mean() > 100