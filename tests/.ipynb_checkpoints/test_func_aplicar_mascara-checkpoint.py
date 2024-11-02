import sys
import os
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_aplicar_mascara():
    import codigo_estudiante as micodigo
    img = Image.open(os.path.join("data","imagen0.png"))
    img_array = np.array(img)
    img_array_gray = np.array(img.convert('L'))
    
    # Crea máscara
    mascara = micodigo.binariza(img_array_gray, umbral=200)
    
    # Aplicar la máscara a la imagen original
    imagen_mascarada = micodigo.aplicar_mascara(img_array, mascara)
    assert imagen_mascarada.mean() < 80