import sys
import os
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_aplicar_filtro():
    import codigo_estudiante as micodigo
    img = Image.open(os.path.join("data","imagen0.png"))
    imagen_laplacian = micodigo.aplicar_filtro(img, tipo_filtro="Laplacian")
    assert imagen_laplacian.max() > 300