#Panda es una librería de Python que permite trabajar con datos de manera eficiente y sencilla.
# Esta librería es especialmente útil para el análisis de datos mediante el uso de columnas y filas.
# Importando la librería pandas
# Esta librería es ampliamente utilizada en la comunidad de ciencia de datos y análisis de datos.

#La creacion del asistente virtual de Panda permite a los usuarios interactuar con la librería de 
# manera más intuitiva.

# La serie es una estructura de datos unidimensional que puede contener cualquier tipo de dato.
# En este caso, la serie contiene números enteros y tiene un índice personalizado con los nombres
# de las personas. La serie se imprime en la consola, mostrando los valores y sus respectivos índices.

#El uso de headers en pandas permite a los usuarios identificar fácilmente las columnas de un DataFrame.
# Los headers son etiquetas que se utilizan para nombrar las columnas de un DataFrame, lo que facilita


import pandas as pd

serie = pd.Series([23,34,28] , index=['Ana', 'Luis', 'Carlos'])
print(serie)

# Esto crea un DataFrame con dos columnas: 'Nombre' y 'Edad' y

serie2 = pd.DataFrame(
    {
        'Nombre': ['Ana', 'Luis', 'Carlos'],
        'Edad': [23, 34, 28]
    }
)
print(serie2)  
ordenado_por_edad = serie2.sort_values(by='Edad')
# ordena el DataFrame por la columna 'Edad' en orden ascendente.
print(ordenado_por_edad)



#Ejercicios:
# 1. 