# # Ejercicio 1: Hacer un programa que muestre un menú con 3 opciones.
# # 1. Comenzar programa
# # 2. Imprimir listado
# # 3. Finalizar programa
# # El usuario debe elegir una opción. Si escoge una inválida, se muestra un mensaje de error.
# # Si elige 1 o 2, se vuelve a mostrar el menú. Si elige 3, se interrumpe el programa.

while True:
    # Muestra el menú de opciones
    print("Menu:")
    print("1. Comenzar programa")
    print("2. Imprimir listado")
    print("3. Finalizar programa")  
    print("Elige una opción (1-3):")
    # Solicita al usuario que elija una opción
    opcion = input("Opción elegida: ")
    
    # Si elige la opción 1
    if opcion == '1':
        print("Programa comenzado.")
    # Si elige la opción 2
    elif opcion == '2':
        print("Listado impreso.")
    # Si elige la opción 3, termina el ciclo y el programa
    elif opcion == '3':
        print("Programa finalizado.")
        break
    # Si elige una opción inválida
    else:
        print("Opción inválida. Por favor, elige una opción válida.")

