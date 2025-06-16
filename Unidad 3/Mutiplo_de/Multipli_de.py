#Ejercicio 1:
#1- Crea un programa que pida dos números enteros al usuario y diga si alguno de ellos 
# es múltiplo del otro. Crea una función EsMultiplo que reciba los dos números,
#  y devuelve si el primero es múltiplo del segundo.

def es_multiplo(num1, num2):
    return num1 % num2 == 0
def main():
    num1 = int(input("Introduce el primer número entero: "))
    num2 = int(input("Introduce el segundo número entero: "))
    if es_multiplo(num1, num2):
        print(f"{num1} es múltiplo de {num2}.")
    elif es_multiplo(num2, num1):
        print(f"{num2} es múltiplo de {num1}.")
    else:
        print(f"Ninguno de los números es múltiplo del otro.")
while True:
    if __name__ == "__main__":
        main()