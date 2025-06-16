# sentencia if
if True:
    print('!El bloque if se ejecutara¡')
    x = 5
    if x > 4 :
        print('!Era verdad¡')

# sentencia elf
if not True:
     print('sentencia if se ejecutara')
else:
    print('sentencia if no se ejecutara')

b = 7
if b >= 7:
    print('No imprimire nada') #Esta sentencia no se ejecuta
else: 
    print('No te creas, si imprimi') #Esta sentencia se ejecuta

# Sentencia elif
# Se pueden verificar varias opciones
# Al incluir una o mas verificaciones elif
# Despues de la declaracion if inicial
# Tomando en cuenta que solo se ejecutara una condición

z = int(input("Ingrese un valor para z: ",))
if z > 8:
    print('!No voy a imprimir¡')#Esta sentencia no se ejecuta
elif z > 5:
    print('!Yo lo hare¡')#Esta sentencia se ejecuta
elif z > 6:
    print('!Yo tampoco voy a imprimir¡')#Esta sentencia no se ejecuta
else:
    print('!Yo tampoco¡')#Esta sentencia no se ejecuta

#Sentencia while
#Permite ejecutar bloques de codigo
# repetidamente mientras se cumpla
# cierta condición

numero = 0
print('Tabla del 3:')
while numero <= 10:
    print(f'{numero * 3}')
    numero +=1
print('Fin')


valores = [5, 1, 9, 2, 7, 4]

encontrado = False
indice = 0
longitud = len(valores)
while not encontrado and indice < longitud:
    valor = valores[indice]
    if valor == 2:
        encontrado = True
    else:
        indice += 1
if encontrado:
    print(f'El numero 2 ha sido encontrado en el indice {indice}')
else:
    print('El numero 2 no ha sido encontrado en la lista de valores')

valores_2 = [5, 1, 9, 2, 7, 4]
encontrado_2 = False
indice_2 = 0
longitud_2 = len(valores_2)
while not encontrado_2 and indice_2 < longitud_2:
    valor_2 = valores_2[indice_2]
    if valor_2 == 2:
        encontrado_2 = True
        break
    else:
        indice_2 += 1
if encontrado_2:
    print(f'El numero 2 ha sido encontrado en el indice {indice_2}')
else:
    print('El numero 2 no ha sido encontrado en la lista de valores')

