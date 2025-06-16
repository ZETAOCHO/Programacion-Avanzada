# Ejercicio 5: Sucesión de Fibonacci
# Hacer un programa que muestre los primeros 10 numeros de la sucesion de Fibonacci.
# La sucesión comienza con 0 y 1, y a partir de estos cada elemento es la suma de los dos
# numeros anteriores en la secuencia: 0 1 1 2 3 5 8 13 21 34.

def fibonacci(n):
    # Creamos una lista vacía para guardar la secuencia
    fib_sequence = []
    # Inicializamos los dos primeros números de la sucesión
    a, b = 0, 1
    # Repetimos el proceso n veces
    for _ in range(n):
        # Agregamos el valor actual de 'a' a la lista
        fib_sequence.append(a)
        # Actualizamos 'a' y 'b' para el siguiente número de la secuencia
        a, b = b, a + b
    # Devolvemos la lista con la secuencia generada
    return fib_sequence

# Imprimimos los primeros 10 números de la sucesión de Fibonacci
print(fibonacci(10))
