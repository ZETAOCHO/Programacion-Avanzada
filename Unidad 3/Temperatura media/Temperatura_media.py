#Ejercicio 2
#2.- Crear una función que calcule la temperatura media de un día a partir de 
# la temperatura máxima y mínima. Crear un programa principal, que utilizando 
# la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y 
# vaya mostrando la media. El programa pedirá el número de días que se van a introducir
# Función que pide al usuario cuántos días quiere introducir
def pedir_dias():
    dias = int(input("¿Cuántos días quieres introducir? "))
    return dias
# Función que calcula la temperatura media
def temperatura_media(temp_max, temp_min):
    return (temp_max + temp_min) / 2
# Función principal que gestiona la entrada de datos y muestra la temperatura media
def main():
    media = {}
    dias = pedir_dias()
    for i in range(dias):
        temp_max = float(input(f"Introduce la temperatura máxima del día {i + 1} en °C: "))
        temp_min = float(input(f"Introduce la temperatura mínima del día {i + 1} en °C: "))
        media[i] = f"Día {i + 1}: {temperatura_media(temp_max, temp_min):.2f}°C"
    for dias, temp in media.items():
        print(f"Temperatura media segun el dia: {temp}")


if __name__ == "__main__":
    main()
