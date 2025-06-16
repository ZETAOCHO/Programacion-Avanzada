# Escribir un programa que guarde en una variable el diccionario {"Euro" : "€", "Dolar": "$", "Yen": "¥"} 
# pregunte por una divisa y muestre su símbolo o un mensaje de aviso si no está en el diccionario.
# Diccionario que almacena las divisas y sus símbolos
divisas = {"euro": "€", "dolar": "$", "yen": "¥"}

# Solicita al usuario que ingrese una divisa y la convierte a minúsculas, luego busca el símbolo en el diccionario
divisa = divisas.get(input("Introduce una divisa (Euro, Dolar, Yen): ").lower(), "No disponible")

# Muestra el símbolo de la divisa o un mensaje si no está disponible
print(divisa)
