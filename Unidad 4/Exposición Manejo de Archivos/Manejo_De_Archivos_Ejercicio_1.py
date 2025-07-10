# `Escribe un programa en Python que:
# 1.Cree un archivo de Excel llamado inventario.xlsx
# 2.Agregue una tabla con los siguientes encabezados:
# Producto, Cantidad, Precio
# 3.Inserta 3 productos con valores inventados
# 4.Muestra un mensaje al final que diga: “Inventario guardado con éxito”
import os
import pandas as pd

# Crear un DataFrame con los encabezados
df = pd.DataFrame(columns=['Producto', 'Cantidad', 'Precio'])

# Insertar 3 productos con valores inventados
df = df._append({'Producto': 'Manzanas', 'Cantidad': 10, 'Precio': 0.5}, ignore_index=True)
df = df._append({'Producto': 'Peras', 'Cantidad': 5, 'Precio': 0.8}, ignore_index=True)
df = df._append({'Producto': 'Naranjas', 'Cantidad': 8, 'Precio': 0.6}, ignore_index=True)

ruta_guardar = os.path.dirname(os.path.abspath(__file__)) + '/inventario.xlsx'
writer = pd.ExcelWriter(ruta_guardar)

# Guardar el DataFrame en un archivo Excel
df.to_excel(writer, index=False, sheet_name='Inventario')
writer.close()  
print("Inventario guardado con éxito")  # Mensaje de confirmación
