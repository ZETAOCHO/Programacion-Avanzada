# Solicita al usuario que ingrese el dividendo
Us_Num1 = input("Ingrese el Dividendo: ",)
# Solicita al usuario que ingrese el divisor
Us_Num2 = input("Ingrese el Divisor: ",)

# Función para verificar si un valor es un número flotante válido
def es_flotante(valor):
    if valor.count('.') <= 1 and valor.replace('.', '', 1).isdigit():
        return True

    else:
        return False

# Verifica si ambos valores ingresados son números (enteros o flotantes)
if (Us_Num1.isdigit() or es_flotante(Us_Num1)) and (Us_Num2.isdigit() or es_flotante(Us_Num2)):
    Num1 = float(Us_Num1)
    Num2 = float(Us_Num2)
    # Verifica que el divisor no sea cero
    if Num2 == 0:
        print("La division no puede realizarse con 0 como divisor.")
    else:
        # Realiza la división y muestra el resultado
        div = Num1 / Num2
        print(f'El resultado de su division es: {div}')
else:
    # Si los valores no son numéricos, muestra un mensaje de error
    print("La division requiere valores numericos.")
