import sys
import os
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_detecta_bordes():
    import codigo_estudiante as micodigo
    img = Image.open(os.path.join("data","imagen0.png"))
    img_bord = micodigo.detecta_bordes(img)    
    assert img_bord.shape[0] == 1024