# Ejercicio 1:
# Crea un programa que pida dos números enteros al usuario y diga si alguno de ellos 
# es múltiplo del otro. 
# Crea una función EsMultiplo que reciba los dos números,
# y devuelve si el primero es múltiplo del segundo.

def es_multiplo(num1, num2):
    # Devuelve True si num1 es múltiplo de num2, es decir, si el residuo de la 
    # división es 0
    return num1 % num2 == 0

def main():
    # Solicita al usuario el primer número entero
    num1 = int(input("Introduce el primer número entero: "))
    # Solicita al usuario el segundo número entero
    num2 = int(input("Introduce el segundo número entero: "))
    # Verifica si el primer número es múltiplo del segundo
    if es_multiplo(num1, num2):
        print(f"{num1} es múltiplo de {num2}.")
    # Verifica si el segundo número es múltiplo del primero
    elif es_multiplo(num2, num1):
        print(f"{num2} es múltiplo de {num1}.")
    # Si ninguno es múltiplo del otro, lo indica
    else:
        print(f"Ninguno de los números es múltiplo del otro.")

# Bucle infinito que ejecuta el programa principal si el archivo es ejecutado 
# directamente
while True:
    if __name__ == "__main__":
        main()