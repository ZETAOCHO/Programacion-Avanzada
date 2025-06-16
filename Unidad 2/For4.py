# Ejercicio 4: Contar vocales en una palabra
# Diseñar un programa que le pida al usuario que ingrese una palabra y despues imprimir la cantidad
# de vocales que se encuentrarn en dicha palabra.

print("Ingrese Una palabra: ")
palabra = input()  # Solicita al usuario que ingrese una palabra
vocales = "aeiouAEIOU"  # Cadena que contiene todas las vocales (mayúsculas y minúsculas)
CountVocals = 0  # Inicializa el contador de vocales en 0

# Recorre cada letra de la palabra ingresada
for letra in palabra:
    # Si la letra es una vocal, incrementa el contador
    if letra in vocales:
        CountVocals += 1

# Muestra la cantidad de vocales encontradas en la palabra
print(f"La cantidad de vocales en la palabra '{palabra}' es: {CountVocals}")