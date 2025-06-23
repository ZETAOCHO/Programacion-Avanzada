#Permite crear y personalizar diversos tipos de graficas,como las que se mencionan
#a continuacion:
#Histogamas
#Diagramas de areas
#Diagramas de linea
#Graficas de barra
#Graaficas de contorno
#Mapas de color
#Metodologia general para construir graficas con MatPlotLib:
#1.-Se importa el modulo pyplot
#   pip install matplotlib
#2.-Se define la figura que contendra la grafica, que se refiere a la region donde se 
#   dibujara y los ejes que graficaran los datos (Ventana).Para esto se emplea la función
#   subplots().
#3.-Se dibujan los datos sobre los ejes. En este paso se emplean diversas funciones 
#   dependiendo de la grafica que se requiera.
#   Histograma
#   barras
#   de sectores
#   de caja y bigotes
#   lineas
#   areas
#   Color
#   contorno 
#   de violines
#4.-Personalizacion de la grafica
#   Titulo
#   Leyenda 
#   Colores 
#   Rejilla 
#   etc
#5.-Guardar la grafica, se utiliza la funcion savefig()
#6.-Despliegue de la grafica, se utiliza lafuncion show()


#El primer paso es importar el modulo pyplot con el alias plt
import matplotlib.pyplot as plt
#Despues Creamos la figura y los ejes
fig, ax = plt.subplots()
#En este caso se va a dibujar una serie de puntos
ax.scatter(x=[1, 2, 3], y=[3, 2, 1])
#Se procede aGuardar el grafico en formato PNG
plt.savefig("Diagrama de dispersión.png")
#Por ultimo se muestra el grafico
plt.show()
