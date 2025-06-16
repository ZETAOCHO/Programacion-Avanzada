# Ejercicio 6: Suma de negativos y promedio de positivos
# Hacer un programa que solicite al usuario ingresar 6 numeros enteros que pueden ser positivos o negativos,
# al terminar, mostrar la suma de los numeros negativos y el promedio de los numeros positivos.
# Tener en cuenta que no es posible dividir por 0, por lo que se requiere evitar que
# de un error si no se ingresan numeros positivos.

numeros_positivos = []  # Lista para almacenar los números positivos ingresados
suma_negativos = 0      # Variable para acumular la suma de los números negativos
x = 0                   # Variable de control para reiniciar el ciclo en caso de error

while True:
    # Ciclo for para solicitar los 6 números al usuario
    for i in range(x, 6):
        entrada = input(f"Ingrese el numero {i + 1} (positivo o negativo): ")
        try:
            numero = int(entrada)  # Intenta convertir la entrada a entero
            if numero < 0:
                suma_negativos += numero  # Suma los números negativos
            else:
                numeros_positivos.append(numero)  # Agrega los positivos a la lista
        except ValueError:
            # Si la entrada no es un número entero válido, muestra un mensaje y reinicia desde el número actual
            print("Por favor, ingrese un número entero válido.")
            x = i
            break  # Sale del for para volver a pedir el mismo número
    else:
        # Si se completaron las 6 iteraciones sin interrupción, salimos del bucle while
        if len(numeros_positivos) > 0:
            # Calcula el promedio de los positivos si hay al menos uno
            promedio_positivos = sum(numeros_positivos) / len(numeros_positivos)
            print(f"La suma de los números negativos es: {suma_negativos}")
            print(f"El promedio de los números positivos es: {promedio_positivos}")
        else:
            # Si no hay positivos, informa que no se puede calcular el promedio
            print("No se ingresaron números positivos, no se puede calcular el promedio.")
            print(f"La suma de los números negativos es: {suma_negativos}")
        break  # Termina el ciclo principal