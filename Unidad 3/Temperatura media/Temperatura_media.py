# Ejercicio 2
# Crear una función que calcule la temperatura media de un día a partir de 
# la temperatura máxima y mínima. El programa principal pide el número de días,
# solicita las temperaturas y muestra la media de cada día.

# Función que pide al usuario cuántos días quiere introducir
def pedir_dias():
    # Solicita al usuario el número de días y lo devuelve como entero
    dias = int(input("¿Cuántos días quieres introducir? "))
    return dias

# Función que calcula la temperatura media
def temperatura_media(temp_max, temp_min):
    # Calcula la media sumando la máxima y mínima y dividiendo entre 2
    return (temp_max + temp_min) / 2

# Función principal que gestiona la entrada de datos y muestra la temperatura media
def main():
    media = {}  # Diccionario para almacenar la media de cada día
    dias = pedir_dias()  # Pide al usuario el número de días
    for i in range(dias):
        # Solicita la temperatura máxima para el día i+1
        temp_max = float(input(f"Introduce la temperatura máxima del día {i + 1} en °C: "))
        # Solicita la temperatura mínima para el día i+1
        temp_min = float(input(f"Introduce la temperatura mínima del día {i + 1} en °C: "))
        # Calcula y guarda la media en el diccionario
        media[i] = f"Día {i + 1}: {temperatura_media(temp_max, temp_min):.2f}°C"
    # Recorre el diccionario 'media' para imprimir la temperatura media de cada día
    # 'dias' es la clave (índice del día) y 'temp' es el valor (cadena con la media)
    for dias, temp in media.items():
        print(f"Temperatura media segun el dia: {temp}")

# Ejecuta la función principal si el archivo es ejecutado directamente
if __name__ == "__main__":
    main()
