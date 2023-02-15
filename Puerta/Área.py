import cv2
import numpy as np

# Cargar la imagen
img = cv2.imread('puerta2.png')

# Seleccionar los puntos
punto1 = (85, 106)
punto2 = (85, 135)
punto3 = (180, 106)
punto4 = (180, 135)

# Dibujar los puntos en la imagen
cv2.circle(img, punto1, 5, (0, 0, 255), -1)
cv2.circle(img, punto2, 5, (0, 0, 255), -1)
cv2.circle(img, punto3, 5, (0, 0, 255), -1)
cv2.circle(img, punto4, 5, (0, 0, 255), -1)

puntos = np.array([punto1, punto2, punto3, punto4])

# Crear una matriz de ceros del mismo tamaño que la imagen
mascara = np.zeros_like(img[:,:,0])

# Dibujar el cuadrilátero en la máscara
cv2.fillPoly(mascara, [puntos], (255,255,255))

# Calcular los momentos de la máscara
momentos = cv2.moments(mascara)

# Hallar el área del cuadrilátero
area = momentos['m00']

print('El área del cuadrilátero es', area)

cv2.imshow('Imagen', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
