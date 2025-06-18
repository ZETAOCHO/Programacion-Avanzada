# Hacer un programa que agregue un color al inicio de la lista dada mediante una funcion.
# Se debe comprobar si el color se añadio correctamente a la lisa, ese proceso debe de hacersse fuera de la funcion
#     colors = ["Negro", "Verde", "Amarillo", "Magenta"]

def agregar_color(color, lista_colores):  
    # Agrega un color al inicio de la lista de colores.
    # :param color: Color a agregar.
    # :param lista_colores: Lista de colores donde se agregará el color.
    lista_colores.insert(0, color)

# Lista de colores inicial
colors = ["Negro", "Verde", "Amarillo", "Magenta"]
# Color a agregar
color_a_agregar = input("Introduce un color: ")
color_a_agregar = f'"{color_a_agregar}"'  # Poner el texto del color entre comillas
# Llamada a la función para agregar el color
agregar_color(color_a_agregar, colors)
# Verificación de si el color se agregó correctamente
if colors[0] == color_a_agregar:
    print(f"El color {color_a_agregar} se ha agregado correctamente al inicio de la lista.")



