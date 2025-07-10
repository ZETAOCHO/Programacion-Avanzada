import numpy as np

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
