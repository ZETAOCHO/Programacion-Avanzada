# Permite crear y personalizar diversos tipos de gráficas, como las que se mencionan a continuación:
# Histogramas, diagramas de áreas, diagramas de línea, gráficas de barra, gráficas de contorno, mapas de color

# Metodología general para construir gráficas con MatPlotLib:
# 1.- Se importa el módulo pyplot
#    pip install matplotlib
# 2.- Se define la figura que contendrá la gráfica, que se refiere a la región donde se 
#     dibujará y los ejes que graficarán los datos (Ventana). Para esto se emplea la función subplots().
# 3.- Se dibujan los datos sobre los ejes. En este paso se emplean diversas funciones 
#     dependiendo de la gráfica que se requiera (histograma, barras, sectores, caja y bigotes, líneas, áreas, color, contorno, violines).
# 4.- Personalización de la gráfica (título, leyenda, colores, rejilla, etc).
# 5.- Guardar la gráfica, se utiliza la función savefig().
# 6.- Despliegue de la gráfica, se utiliza la función show().

# El primer paso es importar el módulo pyplot con el alias plt
import matplotlib.pyplot as plt  # Importa la librería principal para graficar
# Después creamos la figura y los ejes
fig, ax = plt.subplots()  # Crea una figura (ventana) y un conjunto de ejes (ax) donde se dibujará la gráfica
# En este caso se va a dibujar una serie de puntos
ax.scatter(x=[1, 2, 3], y=[3, 2, 1])  # Dibuja un diagrama de dispersión (scatter plot) con los puntos dados
# Se procede a guardar el gráfico en formato PNG
plt.savefig("Diagrama de dispersión.png")  # Guarda la figura actual como una imagen PNG
# Por último se muestra el gráfico
plt.show()  # Muestra la ventana con la gráfica generada

# Como realizar las demás gráficas

import matplotlib.pyplot as plt  # Se vuelve a importar, aunque ya está arriba (no es necesario repetir)
import numpy as np  # Importa la librería para trabajar con arreglos numéricos

# Datos de ejemplo para las gráficas
datos = np.random.randn(100)  # Genera 100 datos aleatorios con distribución normal
categorias = ['A', 'B', 'C']  # Nombres de categorías para gráficas de barras y pastel
valores = [5, 7, 3]  # Valores asociados a las categorías
x = np.linspace(0, 10, 100)  # 100 valores equiespaciados entre 0 y 10
y = np.sin(x)  # Calcula el seno de cada valor de x

# Histograma
plt.figure()  # Crea una nueva figura
plt.hist(datos, bins=10)  # Dibuja un histograma de los datos con 10 barras
plt.title("Histograma")  # Agrega título
plt.savefig("histograma2.png")  # Guarda la imagen
plt.show()  # Muestra la gráfica

# Barras
plt.figure()  # Nueva figura
plt.bar(categorias, valores)  # Dibuja una gráfica de barras
plt.title("Gráfica de barras")  # Título
plt.savefig("barras.png")  # Guarda la imagen
plt.show()  # Muestra la gráfica

# Sectores (pastel)
plt.figure()  # Nueva figura
plt.pie(valores, labels=categorias)  # Dibuja un gráfico de pastel con etiquetas
plt.title("Gráfica de sectores")  # Título
plt.savefig("sectores.png")  # Guarda la imagen
plt.show()  # Muestra la gráfica

# Caja y bigotes
plt.figure()  # Nueva figura
plt.boxplot([datos, np.random.randn(100)])  # Dibuja un diagrama de caja y bigotes para dos conjuntos de datos
plt.title("Caja y bigotes")  # Título
plt.savefig("caja_bigotes.png")  # Guarda la imagen
plt.show()  # Muestra la gráfica

# Líneas
plt.figure()  # Nueva figura
plt.plot(x, y)  # Dibuja una gráfica de líneas (x contra y)
plt.title("Gráfica de líneas")  # Título
plt.savefig("lineas.png")  # Guarda la imagen
plt.show()  # Muestra la gráfica

# Áreas
plt.figure()  # Nueva figura
plt.fill_between(x, y)  # Rellena el área bajo la curva y
plt.title("Gráfica de áreas")  # Título
plt.savefig("areas.png")  # Guarda la imagen
plt.show()  # Muestra la gráfica

# Mapa de color (matriz de calor)
matriz = np.random.rand(10,10)  # Genera una matriz 10x10 de valores aleatorios
plt.figure()  # Nueva figura
plt.imshow(matriz, cmap='viridis')  # Muestra la matriz como imagen de colores
plt.title("Mapa de color")  # Título
plt.colorbar()  # Agrega barra de colores
plt.savefig("mapa_color.png")  # Guarda la imagen
plt.show()  # Muestra la gráfica

# Contorno
X, Y = np.meshgrid(np.linspace(-3,3,100), np.linspace(-3,3,100))  # Crea una malla de coordenadas
Z = np.sin(X**2 + Y**2)  # Calcula valores para cada punto de la malla
plt.figure()  # Nueva figura
plt.contour(X, Y, Z)  # Dibuja líneas de contorno para los valores de Z
plt.title("Gráfica de contorno")  # Título
plt.savefig("contorno.png")  # Guarda la imagen
plt.show()  # Muestra la gráfica

# Violines
plt.figure()  # Nueva figura
plt.violinplot([datos, np.random.randn(100)])  # Dibuja un diagrama de violín para dos conjuntos de datos
plt.title("Gráfica de violines")  # Título
plt.savefig("violines.png")  # Guarda la imagen
plt.show()  # Muestra la gráfica


#Que es la poo, que es una clase, que es un objeto; diferencias, metodo,atributo, encapsulamiento, 
# herencia, polimorfismo, abstracción, ejemplos y ejercicios de tarea para el alumno 
# Fecha de entrega Miercoles 9