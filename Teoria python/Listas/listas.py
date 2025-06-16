numeros = [1, 2, 3, 4, 5]
print(numeros)
# imprime: [1, 2, 3, 4, 5]

mixto = [1, "Hola", 3.14, True]
print(mixto)
# imprime: [1, "Hola", 3.14, True]


# Acceso a elementos de la lista
frutas = ["manzana", "banana", "cereza"]
print(frutas[0])
# imprime: "manzana"
print(frutas[-1])
# imprime: "cereza"

# Modificación de elementos de la lista
frutas = ["manzana", "banana", "cereza"]
frutas[1] = "naranja"
print(frutas)
# imprime: ["manzana", "naranja", "cereza"]

# Agregar y eliminar elementos
frutas = ["manzana", "banana", "cereza"]
frutas.append("uva")
# agrega "uva" al final de la lista
print(frutas)
# imprime: ["manzana", "banana", "cereza", "uva"]
frutas.remove("banana")
# elimina "banana" de la lista
print(frutas)
# imprime: ["manzana", "cereza", "uva"]

# Longitud de la lista
frutas = ["manzana", "banana", "cereza"]
print(len(frutas))
# imprime: 3

# Listas anidadas
lista_anidada = [[1, 2], [3, 4], [5, 6]]
print(lista_anidada[1])
# imprime: [3, 4]
print(lista_anidada[1][0])
# imprime: 3

# vaciar una lista
numeros = [1, 2, 3, 4, 5]
numeros.clear()
print(numeros)
# imprime: []

# unir listas
numeros1 = [1, 2, 3]
numeros2 = [4, 5, 6]
print(numeros1)
# imprime: [1, 2, 3]
print(numeros2)
# imprime: [4, 5, 6]
numeros9 = numeros1 + numeros2
print("numeros9:", numeros9)
# extend
numeros1.extend(numeros2)
print(numeros1)
# imprime: [1, 2, 3, 4, 5, 6]
# insert
numeros1.insert(0, 0)
print(numeros1)
# imprime: [0, 1, 2, 3, 4, 5, 6]


# count
numeros3 = [1, 2, 3, 4, 5, 2]
print(numeros3.count(2))
# imprime: 2
# del
del numeros3[0]
print(numeros3)
# imprime: [2, 3, 4, 5, 2]
# pop
numeros3.pop()
print(numeros3)
# imprime: [2, 3, 4, 5]

#tuplas
# Definición de una tupla
tupla = (1, 2, 3)
print(tupla)
# imprime: (1, 2, 3)
# Que es una tupla
# Una tupla es una colección de elementos ordenados e inmutables
#metodos de las tuplas
# count
tupla = (1, 2, 3, 1)  
print(tupla.count(1))
# imprime: 2
# index
tupla = (1, 2, 3)
print(tupla.index(2))
# imprime: 1
# length
tupla = (1, 2, 3)
print(len(tupla))
# imprime: 3
# Acceso a elementos de la tupla
tupla = (1, 2, 3)
print(tupla[0])
# imprime: 1
print(tupla[-1])
# imprime: 3
# Modificación de elementos de la tupla
# Las tuplas son inmutables, por lo que no se pueden modificar
# Agregar y eliminar elementos
# Las tuplas son inmutables, por lo que no se pueden agregar ni eliminar elementos


# Insertar
numeros4 = [1]
numeros4.insert(3, 0)
print(numeros4)
# imprime: [0, 1]




# De tareas Diccionarios y conjuntos: Metodos, funciones y ejemplos
# Diccionarios: Métodos, funciones y ejemplos

# Definición de un diccionario
persona = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}
print(persona)
# imprime: {'nombre': 'Ana', 'edad': 25, 'ciudad': 'Madrid'}

# Acceso a elementos
print(persona["nombre"])
# imprime: Ana

# Modificación de valores
persona["edad"] = 26
print(persona)
# imprime: {'nombre': 'Ana', 'edad': 26, 'ciudad': 'Madrid'}

# Agregar un nuevo par clave-valor
persona["profesion"] = "Ingeniera"
print(persona)
# imprime: {'nombre': 'Ana', 'edad': 26, 'ciudad': 'Madrid', 'profesion': 'Ingeniera'}

# Eliminar un elemento
del persona["ciudad"]
print(persona)
# imprime: {'nombre': 'Ana', 'edad': 26, 'profesion': 'Ingeniera'}

# Métodos útiles
print(persona.keys())    # dict_keys(['nombre', 'edad', 'profesion'])
print(persona.values())  # dict_values(['Ana', 26, 'Ingeniera'])
print(persona.items())   # dict_items([('nombre', 'Ana'), ('edad', 26), ('profesion', 'Ingeniera']))

# Obtener valor con get (evita error si no existe la clave)
print(persona.get("ciudad", "No disponible"))
# imprime: No disponible

# Limpiar diccionario
persona.clear()
print(persona)
# imprime: {}

# Conjuntos: Métodos, funciones y ejemplos

# Definición de un conjunto
conjunto = {1, 2, 3, 4}
print(conjunto)
# imprime: {1, 2, 3, 4}

# Agregar elementos
conjunto.add(5)
print(conjunto)
# imprime: {1, 2, 3, 4, 5}

# Eliminar elementos
conjunto.remove(3)
print(conjunto)
# imprime: {1, 2, 4, 5}

# Métodos útiles
otro_conjunto = {4, 5, 6}
print(conjunto.union(otro_conjunto))        # {1, 2, 4, 5, 6}
print(conjunto.intersection(otro_conjunto)) # {4, 5}
print(conjunto.difference(otro_conjunto))   # {1, 2}

# Verificar pertenencia
print(2 in conjunto)  # True
print(3 in conjunto)  # False

# Limpiar conjunto
conjunto.clear()
print(conjunto)
# imprime: set()



diccionario = {1: "uno", 2: "dos", 3: "tres"}
get = diccionario.get(2)
print(get)
keys = diccionario.keys()
values = diccionario.values()
print("Keys:", keys)    # imprime: Keys: dict_keys([1, 2, 3])
print("Values:", values)  # imprime: Values: dict_values(['uno', 'dos', 'tres'])

diccionario.pop(2)  # Elimina el elemento con clave 2
print(diccionario)  # imprime: {1: 'uno', 3: 'tres'}    




