# 1. Elaborar un programa en el cual aparezcan dos
#    imagenes que tengan diferentes dimensiones.

import cv2
import numpy as np

# Cargar una imagen y mostrarla en una ventana
width = 320
height = 240
imagen = cv2.imread("C:\\Users\\vagoa\\Downloads\\diamond_painting_map (7).png")
imagen2 = cv2.imread("C:\\Users\\vagoa\\Downloads\\color_legend (8).png")

# Redimensiona las imágenes antes de mostrarlas
imagen_resized = cv2.resize(imagen, (width, height))
imagen2_resized = cv2.resize(imagen2, (width*2, height*2))

cv2.imshow("Imagen", imagen_resized)
cv2.moveWindow("Imagen", 100, 100)
cv2.imshow("Imagen 2", imagen2_resized)
cv2.moveWindow("Imagen 2", 800, 100)

cv2.waitKey(0)
cv2.destroyAllWindows() 
