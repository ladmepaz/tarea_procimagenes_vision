# -*- coding: utf-8 -*-
"""
Ejercicios del curso de Visión por Computador
"""

import numpy as np
import cv2
from PIL import Image

def nueva_resolucion(img, nueva_resolucion=None):
    """
    Cambia de resolución de imagen.

    Parámetros:
    img (Image de PIL): Objeto tipo Image de PIL.
    nueva_resolucion (tuple): Tupla (ancho, alto) para redimensionar la imagen.

    Retorna:
    img: Objeto tipo Image de PIL.
    """
    
    img = None # Ingresa código aquí
        
    return img

def detecta_bordes(img):
    """
    Aplica detección de bordes.

    Parámetros:
    img: Objeto tipo Image de PIL.

    Retorna:
    bordes: Arreglo con los bordes detectados.
    """

    img_array = np.array(img)
    _, _, num_canales = img_array.shape
    
    if num_canales == 1:
        bordes = cv2.Canny(img_array, 100, 200)
    else:
        bordes = cv2.Canny(None, 100, 200) # Ingresa código aquí
    
    return bordes

def normaliza(img):
    """
    Normaliza los valores del arreglo en el rango [0, 1].

    Parámetros:
    img (PIL.Image): Imagen a convertir.
    
    Retorna:
    np.ndarray: Arreglo de NumPy con los datos de la imagen.
    """
    
    arreglo = np.array(img)
    arreglo = None # Ingresa código aquí
    
    return arreglo

def transformar_color(img, espacio='HSV'):
    """
    Convierte la imagen a un espacio de color especificado.

    Parámetros:
    img: Objeto tipo Image de PIL.
    espacio (str): Espacio de color al que se quiere convertir ('HSV', 'LAB', 'YCrCb').

    Retorna:
    np.ndarray: Imagen en el nuevo espacio de color.
    """
    img_np = np.array(img)
    if espacio == 'HSV':
        img_np = cv2.cvtColor(img_np, cv2.COLOR_RGB2HSV)
    elif espacio == 'LAB':
        img_np = cv2.cvtColor(img_np, None) # Ingresa código aquí
    elif espacio == 'YCrCb':
        img_np = cv2.cvtColor(img_np, None) # Ingresa código aquí
    else:
        raise ValueError("Espacio de color no soportado")
    return img_np

def aplicar_filtro(img, tipo_filtro="GaussianBlur", **kwargs):
    """
    Aplica un filtro especificado a la imagen.

    Parámetros:
    img: Objeto tipo Image de PIL.
    tipo_filtro (str): Tipo de filtro a aplicar ('GaussianBlur', 'Laplacian', 'Canny').
    kwargs: Parámetros adicionales para el filtro.

    Retorna:
    np.ndarray: Imagen filtrada como arreglo de NumPy.
    """
    img_np = np.array(img)
    if tipo_filtro == "GaussianBlur":
        filtrada = cv2.GaussianBlur(img_np, kwargs.get("ksize", (5, 5)), kwargs.get("sigmaX", 0))
    elif tipo_filtro == "Laplacian":
        filtrada = None # Ingresa código aquí
    elif tipo_filtro == "Canny":
        filtrada = cv2.Canny(img_np, kwargs.get("threshold1", 100), kwargs.get("threshold2", 200))
    else:
        raise ValueError("Filtro no soportado")
    return filtrada

def binariza(arreglo_img, umbral=128):
    """
    Segmenta una imagen en función de un umbral de intensidad.

    Parámetros:
    arreglo_img (np.ndarray): Imagen en escala de grises como arreglo de NumPy.
    umbral (int): Valor de umbral para la segmentación.

    Retorna:
    np.ndarray: Imagen segmentada en binario {0, 1}.
    """
    segmentada = None # Ingresa código aquí
    return segmentada

def aplicar_mascara(img_array, mascara):
    """
    Aplica una máscara binaria a una imagen, eliminando las regiones donde la máscara tiene valores de cero.

    Parámetros:
    img_array (np.ndarray): Imagen en escala de grises o RGB como un arreglo de NumPy.
    mascara (np.ndarray): Máscara binaria (0s y 1s) de la misma dimensión que la imagen (o expandible en caso de imágenes RGB).

    Retorna:
    np.ndarray: Imagen con la máscara aplicada, manteniendo solo las intensidades en las regiones de la máscara con valor 1.
    """
    # Verificar que la máscara tiene las mismas dimensiones espaciales que la imagen
    if img_array.shape[:2] != mascara.shape:
        raise ValueError("La máscara debe tener las mismas dimensiones espaciales que la imagen.")
    
    # Expandir la máscara para que tenga las mismas dimensiones que una imagen RGB si es necesario
    if len(img_array.shape) == 3:  # Imagen RGB
        mascara = np.repeat(mascara[:, :, np.newaxis], 3, axis=2)
    
    # Aplicar la máscara a la imagen
    img_mascarada = None # Ingresa código aquí
    
    return img_mascarada

def aplicar_filtro_convolucion(img_array, kernel):
    """
    Aplica un filtro a una imagen utilizando convolución sin librerías de procesamiento de imágenes.

    Parámetros:
    img_array (np.ndarray): Imagen en escala de grises como un arreglo de NumPy.
    kernel (np.ndarray): Matriz del filtro a aplicar (kernel), debe tener dimensiones impares.

    Retorna:
    np.ndarray: Imagen filtrada como un arreglo de NumPy.

    # Ejemplo de un kernel de detección de bordes (Sobel horizontal)
    kernel_sobel_x = np.array([[-1, 0, 1],
                               [-2, 0, 2],
                               [-1, 0, 1]])
    
    # Imagen de entrada en escala de grises
    img_filtrada = aplicar_filtro_convolucion(img_array, kernel_sobel_x)
    """
    # Dimensiones del kernel
    k_height, k_width = kernel.shape
    assert k_height % 2 == 1 and k_width % 2 == 1, "El kernel debe tener dimensiones impares."
    
    # Padding para mantener el tamaño de la imagen original
    pad_h = k_height // 2
    pad_w = k_width // 2
    img_padded = np.pad(img_array, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant', constant_values=0)
    
    # Crear una imagen de salida
    output = np.zeros_like(img_array)
    
    # Aplicar la convolución
    for i in range(None): # Ingresa código aquí
        for j in range(None): # Ingresa código aquí
            # Extraer la región correspondiente de la imagen
            region = img_padded[i:i + k_height, j:j + k_width]
            # Aplicar el kernel a la región (producto elemento a elemento y suma)
            output[i, j] = np.sum(region * kernel)
    
    # Normalizar el resultado para valores válidos de intensidad (0 a 255)
    output = np.clip(output, 0, 255)
    return output.astype(np.uint8)