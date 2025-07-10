import numpy as np

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