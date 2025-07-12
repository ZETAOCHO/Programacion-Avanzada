# Crea un programa que abra el
# Excel anterior y obtenga la
# edad mínima y máxima.
import pandas as pd
import os
# Cargar el archivo Excel
df = pd.read_excel(os.path.dirname(os.path.abspath(__file__)) + '/Lista.xlsx')
# Obtener la edad mínima y máxima
edad_minima = df['Edad'].min()
edad_maxima = df['Edad'].max()
print(f"La edad mínima es: {edad_minima}")
print(f"La edad máxima es: {edad_maxima}")