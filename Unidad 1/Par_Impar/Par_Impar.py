# Hacer un programa que solicite al usuario un número entero y muestre si es par o impar.
# Diccionario para asociar el residuo de la división entre 2 con "Par" o "Impar"
mod = {0: "Par", 1: "Impar"}
# Solicita al usuario que ingrese un número entero
x = input("Digite un numero entero: ", )    
# Verifica si la entrada es un número entero positivo
# Si es así, determina si es par o impar y lo muestra
# Si no, muestra un mensaje de error
print("El numero es", mod[int(x) % 2]) if x.isdigit() else print("El valor ingresado no es un numero entero")