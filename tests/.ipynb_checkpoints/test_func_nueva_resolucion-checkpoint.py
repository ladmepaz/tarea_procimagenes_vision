import sys
import os
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_nueva_resolucion():
    import codigo_estudiante as micodigo
    img = Image.open(os.path.join("data","imagen0.png"))
    img_rs = micodigo.nueva_resolucion(img, nueva_resolucion=(128, 256))
    assert img_rs.size[1] == 256