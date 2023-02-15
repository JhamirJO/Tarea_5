import cv2
import numpy as np

# Leer la imagen
img = cv2.imread("bordes.png")

# Convertimos la imagen a escala de grises y aplicamos difuminado Gaussiano.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplicar un filtro gaussiano para suavisar la imagen
blurred = cv2.GaussianBlur(gray, (5,5),0)

# Aplicar el algoritmo de detección de bordes de Canny
edges = cv2.Canny(blurred, 30, 150)

# Mostrar la imagen original y la imagen con bordes detectados
cv2.imshow("Original", img)
cv2.imshow("imagen en escala de grises ", gray)
cv2.imshow("imagen con filtro gausiano ", blurred)
cv2.imshow("Bordes", edges)


cv2.waitKey(0)
cv2.destroyAllWindows()