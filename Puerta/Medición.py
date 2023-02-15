import cv2

# Cargar la imagen
img = cv2.imread('puerta.png')

# Seleccionar los dos puntos
#Línea amarilla
p1 = (138, 190)
p2 = (138, 310)
#Línea cyan
p3 = (123, 144)
p4 = (123, 310)
#Línea verde
p5 = (137, 20)
p6 = (137, 108)
#Línea roja
p7 = (175, 310)
p8 = (100, 310)

# Dibujar los puntos en la imagen
cv2.circle(img, p1, 5, (0, 149, 196), -1)
cv2.circle(img, p2, 5, (0, 149, 196), -1)

cv2.circle(img, p3, 5, (143, 102, 11), -1)
cv2.circle(img, p4, 5, (143, 102, 11), -1)

cv2.circle(img, p5, 5, (55, 185, 33), -1)
cv2.circle(img, p6, 5, (55, 185, 33), -1)

cv2.circle(img, p7, 5, (0, 0, 255), -1)
cv2.circle(img, p8, 5, (0, 0, 255), -1)

# Calcular la distancia
dA = ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5
dC = ((p4[0] - p3[0])**2 + (p4[1] - p3[1])**2)**0.5
dV = ((p6[0] - p5[0])**2 + (p6[1] - p5[1])**2)**0.5
dR = ((p8[0] - p7[0])**2 + (p8[1] - p7[1])**2)**0.5

#Calcular la distancia en metros
dmA = 3
dmC = (dmA * dC)/dA
dmV = (dmA * dV)/dA
dmR = (dmA * dR)/dA

# Mostrar la distancia en pixeles
print('La distancia en pixeles es:')
print('La distancia de la línea amarilla es:', dA)
print('La distancia de la línea cyan es:', dC)
print('La distancia de la línea verde es:', dV)
print('La distancia de la línea roja es:', dR)
print('\n')

#Mostrar la distancia en metros
print('La distancia en metros es:')
print('La distancia de la línea amarilla es:', dmA)
print('La distancia de la línea cyan es:', dmC)
print('La distancia de la línea verde es:', dmV)
print('La distancia de la línea roja es:', dmR)

# Mostrar la imagen con los puntos y la distancia

cv2.imshow('Imagen', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
