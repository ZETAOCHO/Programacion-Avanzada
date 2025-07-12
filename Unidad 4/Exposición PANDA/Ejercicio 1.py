# Crea un programa que pida al
# usuario n nombres y edades de
# personas, las ordene en un
# data frame y guardarlo como
# Excel.
import pandas as pd
import os


nombres = []
edades = [] 
num_personas = int(input("¿Cuántas personas quieres ingresar? "))
for i in range(num_personas):   
    nombre = input(f"Ingrese el nombre de la persona {i+1}: ")
    edad = int(input(f"Ingrese la edad de {nombre}: "))
    nombres.append(nombre)
    edades.append(edad)
# Crea un DataFrame con los datos ingresados.
df_personas =  pd.DataFrame({
    'Nombre': nombres,
    'Edad': edades
})  
# Ordena el DataFrame por la columna 'Edad' en orden ascendente.
df_ordenado = df_personas.sort_values(by='Edad')
# Guarda el DataFrame ordenado en un archivo Excel.
ruta_guardar = os.path.dirname(os.path.abspath(__file__)) + '/Lista.xlsx'
df_ordenado.to_excel(ruta_guardar, index=False)
print("DataFrame ordenado por edad:")
print(df_ordenado)  