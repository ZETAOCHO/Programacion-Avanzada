# Solicita al usuario que ingrese su edad
x = int(input("Digite su edad: ", ))

# Solicita al usuario que ingrese su ingreso mensual
y = int(input("Digite su ingreso mensual(entero sin comas): ", ))

# Verifica si el usuario es mayor de edad y tiene un ingreso mensual superior a 20,000
if x >= 18 and y > 20000:
    print("Usted es mayor de edad y tiene un ingreso mensual superior a 20,000 por lo tanto debe pagar impuestos")
else:
    # Si no cumple alguna de las condiciones anteriores
    print("Usted no es mayor de edad o no tiene un ingreso mensual superior a 20,000 por lo tanto no debe pagar impuestos")