def tabla_del(numero2):
    """
    Imprime la tabla de multiplicar del número dado.

    :param numero: Número para el cual se imprimirá la tabla de multiplicar.
    """
    resultados = []
    for i in range(11):
        resultados.append(numero2 * i)
    return resultados
numero2 = int(input('Ingrese el numero a multiplicar: '))
resultados = tabla_del(numero2)
print(f'Tabla del {numero2}: {resultados}')

def saludo(nombre):
    """
    Imprime un saludo personalizado.

    :param nombre: Nombre de la persona a saludar.
    """
    print(f'Hola {nombre}')
print(saludo('Mecatronica'))
