# Ejercicio 2: Hacer un programa que pide al usuario ingresar títulos de libros por teclado,
# terminando el ingreso al leerse el string o el caracter asterisco(*).
# Cada vez que el usuario ingrese un string de longitud 1 que contenga solo una diagonal (/),
# se considera que termina una línea.
# Por cada línea completa, informar al usuario cuántos dígitos numéricos (0-9) aparecieron en total
# (en todos los nombres de libros que contienen esa línea).
# Informar al final cuántas líneas se ingresaron.

digitos = 0         # Contador total de dígitos numéricos
lineas = 0          # Contador de líneas ingresadas
completo = ""       # Acumula todos los títulos ingresados

while True:
    # Solicita al usuario el título del libro o el carácter especial para finalizar
    linea = input("Ingrese el titulo del libro (o finalice con *): ")
    # Si el usuario ingresa '*', finaliza el ingreso
    if linea == "*":
        print("Listado Finalizado")
        break
    # Si el usuario ingresa solo '/', cuenta como una línea
    if len(linea) == 1 and linea == "/":
        lineas += 1
    # Si el usuario ingresa un título de más de un carácter, también cuenta como línea
    if len(linea) > 1:
        lineas += 1
    # Acumula el texto ingresado
    completo = completo + linea

# Cuenta la cantidad total de dígitos numéricos en todos los títulos ingresados
digitos = digitos + sum(c.isdigit() for c in completo)
# Muestra la cantidad total de dígitos encontrados
print(f"Cantidad de dígitos en total: {digitos}")
# Muestra la cantidad de líneas ingresadas
print(f"Cantidad de líneas ingresadas: {lineas}")