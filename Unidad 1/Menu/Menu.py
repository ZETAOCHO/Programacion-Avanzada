# Hacer un programa que guarde los precios de los alimentos mostrados en la tabla, pregunte el
# usuario por uno de ellos, el numero de unidades que va a consumir y le muestre por pantalla
# el precio en pantalla acumulado hasta que indique que es todo. si lo que pide el usuario 
# no se encuentra en la tabla, que le muestre un mensaje informando de que no se encuentra 
# en la tabla.

# Tabla de precios de alimentos
# | Alimento       | Precio por unidad |
# |----------------|-------------------|
# | Enchiladas     | $120              |
# | Montado        | $150              |
# | Quesibirrias   | $169.99           |
# | Coca-Cola      | $39.49            |
# | Chilaquiles    | $113.05           |
# | Jamaica        | $29.90            |



# Diccionario que almacena los precios de los alimentos
precios = {
    "enchiladas": 120,
    "montado": 150,
    "quesabirrias": 169.99,
    "coca-cola": 39.49,
    "chilaquiles": 113.05,
    "jamaica": 29.90
}

# Variable para acumular el total a pagar
total = 0

# Ciclo principal para pedir alimentos y cantidades al usuario
while True:
    # Muestra el menú de alimentos y precios
    print("\n--- Menú ---")
    for alimento, precio in precios.items():
        print(f"{alimento:12} - ${precio:.2f}")
    print("Escriba 'salir' para terminar.")

    # Solicita el nombre del alimento al usuario
    alimento = input("Ingrese el nombre del alimento: ").strip()
    # Si el usuario escribe 'salir', termina el ciclo
    if alimento.lower() == 'salir':
        break

    # Verifica si el alimento está en el diccionario de precios
    if alimento in precios:
        # Solicita el número de unidades del alimento
        unidades = int(input(f"Ingrese el número de unidades de {alimento}: "))
        # Suma el precio de las unidades al total
        total += precios[alimento] * unidades
        # print(f"Precio acumulado: ${total:.2f}")  Línea comentada que mostraria el
        #  total acumulado si se desea
    else:
        # Si el alimento no está en la tabla, muestra un mensaje
        print("El alimento no se encuentra en la tabla.")

# Muestra el total a pagar al final
print(f"Total a pagar: ${total:.2f}")



