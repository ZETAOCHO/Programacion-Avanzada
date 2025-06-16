# Ejercicio 3: Sumar números ingresados
# Hacer un programa que solicite al usuario una cantidad y luego itere la cantidad de veces dada.
# En cada iteración se solicita un número al usuario; al finalizar mostrar la suma de todos los 
# números ingresados.

Iteraciones = int(input("Ingrese la cantidad de iteraciones: "))  # Solicita al usuario cuántas veces va a iterar
suma = 0  # Inicializa la variable suma en 0

# Ciclo que se repite la cantidad de veces indicada por el usuario
for i in range(Iteraciones):
    numero = int(input("Ingrese un número: "))  # Solicita un número en cada iteración
    suma += numero  # Suma el número ingresado a la variable suma

# Muestra la suma total de los números ingresados
print(f"La suma de los números ingresados es: {suma}")
