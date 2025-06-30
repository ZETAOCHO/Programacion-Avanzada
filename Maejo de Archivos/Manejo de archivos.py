# Manejo de Archivos en Python
# En esta sección aprenderemos a manejar archivos en Python, incluyendo
# cómo abrir, leer, escribir y cerrar archivos.

#Como crear un archivo de excel, se requiere instalar 
# las siguientes librerias:
#pandas
#Openpyxl
#Xlsxwriter
#Python xlrd
# pip install pandas openpyxl xlsxwriter xlrd
import pandas as pd
datos = {
    'Nombres': ['Isvan', 'Fernando', 'Mauricio', 'Kaleb'],
    'Mecanica': [87, 75, 94, 62],
    'Calculo': ['91', '85', '67', '78'],
    'Programacion': ['Python', 'Java', 'C++']
}
df = pd.DataFrame(datos)
# Guardar el DataFrame en un archivo Excel
df.to_excel('calificaciones.xlsx', index=False, engine='openpyxl')
#Crear un archivo de texto word
#Utilizaremos la libreria python-docx
# pip install python-docx
from docx import Document
from docx.shared import Inches
# Crear un nuevo documento de Word
doc = Document()




#Manejo de Archivos en Python
#OS
import os
print(os.getcwd())  # Obtener el directorio de trabajo actual#
#Crear un directorio
os.mkdir('Nuevo_Directorio')
#Cambiar el nombre del directorio de trabajo
os.rename('Nuevo_Directorio', 'Directorio_Cambiado')
#Remover un directorio
os.rmdir('Directorio_Cambiado')
#Solo puede remover un directorio si este esta vacio
#Utilizacion de Shutil
import shutil
#renombrar un archivo
shutil.move('calificaciones.xlsx', 'calificaciones_nuevo.xlsx')
#Eliminar un directorio
shutil.rmtree('Directorio_Cambiado')
#Espacio en disco
uso= shutil.disk_usage('/')
print(f"Total: {uso.total // (1024**3)} GB")
print(f"Usado: {uso.used // (1024**3)} GB")
print(f"Libre: {uso.free // (1024**3)} GB")
