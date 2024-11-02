import sys
import os
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_binariza():
    import codigo_estudiante as micodigo
    img = Image.open(os.path.join("data","imagen0.png"))
    # Aplicar la función binariza con un umbral de 128
    imggray = img.convert("L")  # Convertir a escala de grises
    arreglo_img = np.array(imggray)
    imagen_binarizada = micodigo.binariza(arreglo_img, umbral=128)
    assert imagen_binarizada.mean() > 0.5