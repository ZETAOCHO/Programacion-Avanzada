# Funciones en Python
# Una función es un bloque de código que realiza una tarea específica y puede ser reutilizado en diferentes partes del programa.
# Las funciones pueden recibir parámetros y devolver valores.

def main():
    print('Comienzo del programa')
    numero = int(input('Ingrese el numero a multiplicar: '))
    multiplica_por_5(numero)
    num = int(input('Ingrese el numero a evaluar: '))
    cuadrado_de_par(num)

def multiplica_por_5(numero):
    """
    Multiplica el número dado por 5.

    :param numero: Número a multiplicar.
    """
    print(f'{numero} * 5 = {numero * 5}')

def cuadrado_de_par(num):
    """
    Calcula el cuadrado de un número si es par.
    
    :param num: Número a evaluar.
    :return: El cuadrado del número si es par, o None si es impar.
    """
    if not num % 2 == 0:
        print('No par')
        return
    else:
        print(num ** 2)

if __name__ == "__main__":
    main()

    

# def multiplica_por_5(numero):
#     """
#     Multiplica el número dado por 5.

#     :param numero: Número a multiplicar.
#     """
#     print(f'{numero} * 5 = {numero * 5}')

# def cuadrado_de_par(num):
#     """
#     Calcula el cuadrado de un número si es par.
    
#     :param num: Número a evaluar.
#     :return: El cuadrado del número si es par, o None si es impar.
#     """
#     if not num % 2 == 0:
#         print('No par')
#         return
#     else:
#         print(num ** 2)

# def main():
#     print('Comienzo del programa')
#     # Solicita al usuario un número para multiplicar por 5
#     numero = int(input('Ingrese el numero a multiplicar: '))
#     multiplica_por_5(numero)

#     # Solicita al usuario un número para evaluar si es par y calcular su cuadrado
#     num = int(input('Ingrese el numero a evaluar: '))
#     cuadrado_de_par(num)

# if __name__ == "__main__":
#     main()



