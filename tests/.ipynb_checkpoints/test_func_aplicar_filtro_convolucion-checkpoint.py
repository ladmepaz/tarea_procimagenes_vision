import sys
import os
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_aplicar_filtro_convolucion():
    import codigo_estudiante as micodigo
    img = Image.open(os.path.join("data","imagen0.png"))
    img_array = np.array(img.convert('L'))

    # Definir el kernel Sobel en dirección horizontal
    kernel_sobel_x = np.array([[-1, 0, 1],
                               [-2, 0, 2],
                               [-1, 0, 1]])
    
    # Aplicar el filtro de convolución con el kernel Sobel
    img_filtrada = micodigo.aplicar_filtro_convolucion(img_array, kernel_sobel_x)
    assert img_filtrada.mean() > 100