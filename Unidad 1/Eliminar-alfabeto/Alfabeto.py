# Hacer un programa que contenga las letras del abecedario en una lista,de la a a la z, incluyendo 
# la ñ, que elimine de dicha lista las letras con posicion multiplo de x, que ingresara el usuario 
# y muestre por pantalla, la lista resultante.

Alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
           "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
x = int(input("Introduce un numero entero <= 26: ", ))
# Verifica si el número es menor o igual a 26
if x <= 26:
    # Elimina las letras con posición múltiplo de x
    # Se recorre la lista al reves para evitar problemas al eliminar elementos
    # porque al eliminar un elemento, los indices de los siguientes elementos cambian
    for i in range(len(Alfabeto)-1 ,-1,-1):
        if ((i + 1) % x) == 0:  # +1 porque las posiciones empiezan en 0
            del Alfabeto[i]
    print("Lista resultante:", Alfabeto)
else:
    print("El numero debe ser menor o igual a 26")