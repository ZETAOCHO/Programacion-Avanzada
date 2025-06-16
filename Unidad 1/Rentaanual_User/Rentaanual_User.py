# Solicita al usuario que ingrese el valor del alquiler anual
x = float(input("Digite el valor del alquiler(Entero sin comas): ", ))

# Verifica en qué rango se encuentra el valor del alquiler y muestra el porcentaje de 
# impuesto correspondiente

if x < 10000:
    print("El impuesto sera del 5%")
elif x >= 10000 and x < 20000:
    print("El impuesto sera del 15%")
elif x >= 20000 and x < 35000:
    print("El impuesto sera del 20%")
elif x >= 35000 and x < 60000:
    print("El impuesto sera del 30%")
elif x > 60000:
    print("El impuesto sera del 45%")
# El porcentaje de impuesto segun el valor del alquiler anual es
# 5% si es menor a 10000, 15% si es mayor o igual a 10000 y menor a 20000,
# 20% si es mayor o igual a 20000 y menor a 35000, 30% si es mayor o igual a 35000 y
# menor a 60000, y 45% si es mayor a 60000.