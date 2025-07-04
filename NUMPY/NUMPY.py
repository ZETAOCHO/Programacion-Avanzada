import numpy as np
#funciones de numpy
#

a = np.array([[1,2,3],[4,5,6]])
print(a)


b = np.array([3,4])
print(np.linalg.norm(b))

#se tiene un circuito
#electronico de dos mallas, que 
#tiene las siguientes ecuaciones.
#Crea un programa que calcule
#los valores de I1 e I2  
#    c = np.array([10,-5,12])
#   d = np.array([-5,15,6])
#   e = (3*c) + d
#   print(e)
#   I1 = e[2] / e[0]
#   I2 = (12-(10*I1))/-5
#   print(f"El valor de I1 es: {I1}")
#   print(f"El valor de I2 es: {I2}")
f = np.array([[10,-5],[-5, 15]])
g = np.array([12,6])
H = np.linalg.solve(f, g)
print(f"El valor de I1 es: {H[0]}")
print(f"El valor de I2 es: {H[1]}")

#Un sensor dde temperatura conectado a un 
#microcontrolador realizo las siguientes
#mediciones en grados centigrados:
# 31, 29, 34, 35, 39, 40, 28.
#Calcula la media, la mediana, la desviacion estandar
# varianzay temperatura maxima y minima.

temperaturas = np.array([31, 29, 34, 35, 39, 40, 28])
print(f"La media es: {np.mean(temperaturas)}")
print(f"La mediana es: {np.median(temperaturas)}")
print(f"La desviacion estandar es: {np.std(temperaturas)}")
print(f"La varianza es: {np.var(temperaturas)}")
print(f"La temperatura minima es: {np.min(temperaturas)}")
print(f"La temperatura maxima es: {np.max(temperaturas)}")
