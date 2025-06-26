# Ejercicio 1: Clase Estudiante
# --------------------------------
# Enunciado:
# Crea una clase llamada Estudiante que almacene el nombre, la edad y una lista de calificaciones de un estudiante.
# La clase debe tener un método que calcule y retorne el promedio de las calificaciones.
# Crea un objeto de la clase Estudiante, asígnale valores y muestra el promedio de sus calificaciones.

class Estudiante:
    def __init__(self, nombre, edad, calificaciones):
        # Atributos del objeto: nombre, edad y calificaciones (lista de notas)
        self.nombre = nombre
        self.edad = edad
        self.calificaciones = calificaciones

    def calcular_promedio(self):
        # Método para calcular el promedio de calificaciones
        if self.calificaciones:  # Verifica que la lista no esté vacía
            return sum(self.calificaciones) / len(self.calificaciones)
        return 0  # Si no hay calificaciones, retorna 0

# Creamos una instancia (objeto) de la clase Estudiante
alumno1 = Estudiante("Ana", 20, [90, 85, 88])

# Mostramos el promedio usando el método de la clase
print(f"Promedio de {alumno1.nombre}: {alumno1.calcular_promedio():.2f}")



# Ejercicio 2: Herencia con Empleado y Gerente
# --------------------------------------------
# Enunciado:
# Crea una clase base llamada Empleado con atributos para el nombre y el salario, y un método para mostrar su información.
# Luego, crea una clase derivada llamada Gerente que herede de Empleado y agregue un atributo para la cantidad de empleados a cargo.
# Sobrescribe el método para mostrar la información del gerente incluyendo este nuevo dato.
# Crea objetos de ambas clases y muestra su información.

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar_info(self):
        # Método común para mostrar información del empleado
        return f"Empleado: {self.nombre}, Salario: ${self.salario}"

# La clase Gerente hereda de Empleado
class Gerente(Empleado):
    def __init__(self, nombre, salario, empleados_a_cargo):
        super().__init__(nombre, salario)  # Llama al constructor de la clase base
        self.empleados_a_cargo = empleados_a_cargo

    def mostrar_info(self):
        # Sobrescribe el método para agregar información adicional
        return (f"Gerente: {self.nombre}, Salario: ${self.salario}, "
                f"Empleados a cargo: {self.empleados_a_cargo}")

# Creamos una instancia de Gerente
gerente1 = Gerente("Luis", 50000, 7)

# Mostramos la información del gerente usando el método sobrescrito
print(gerente1.mostrar_info())

# También podemos crear un empleado normal para comparar
empleado1 = Empleado("Carlos", 30000)
print(empleado1.mostrar_info())



# Ejercicio 3: Polimorfismo con Figura, Cuadrado, Círculo y Triángulo
# -------------------------------------------------------------------
# Enunciado:
# Define una clase abstracta llamada Figura que tenga un método abstracto area().
# Luego, crea las clases Cuadrado, Círculo y Triángulo que hereden de Figura e implementen el método area() de acuerdo a su fórmula.
# Crea una lista con objetos de estas clases y muestra el área de cada figura usando polimorfismo.

from abc import ABC, abstractmethod
import math

# Definimos una clase abstracta Figura
class Figura(ABC):
    @abstractmethod
    def area(self):
        # Método abstracto que deben implementar las subclases
        pass

# Subclase Cuadrado que hereda de Figura
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        # Calcula el área del cuadrado
        return self.lado ** 2

# Subclase Círculo que hereda de Figura
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        # Calcula el área del círculo
        return math.pi * self.radio ** 2

# Subclase Triángulo que hereda de Figura (mejora propuesta)
class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        # Calcula el área del triángulo
        return (self.base * self.altura) / 2

# Creamos una lista de figuras de diferentes tipos
figuras = [
    Cuadrado(4),    # Lado = 4
    Circulo(3),     # Radio = 3
    Triangulo(5, 2) # Base = 5, Altura = 2
]

# Usamos polimorfismo para calcular el área de cada figura
for figura in figuras:
    # type(figura).__name__ nos da el nombre de la clase (Cuadrado, Circulo, Triangulo)
    print(f"{type(figura).__name__} - Área: {figura.area():.2f}")



# Ejercicio 4: Polimorfismo con Animales
# ---------------------------------------
# Enunciado:
# Crea una clase base llamada Animal con un método abstracto hablar().
# Luego, crea clases derivadas Perro y Gato que implementen el método hablar() con un sonido característico.
# Crea una lista de animales y haz que cada uno hable usando polimorfismo.

from abc import ABC, abstractmethod

# Clase base Animal
class Animal(ABC):
    @abstractmethod
    def hablar(self):
        # Método que será sobrescrito por las subclases (polimorfismo)
        pass

# Clase Perro que hereda de Animal
class Perro(Animal):
    def __init__(self, nombre, raza):
        # Llama al constructor de la clase base para inicializar 'nombre'
        super().__init__(nombre)
        # Inicializa el atributo raza específico de Perro
        self.raza = raza

    def hablar(self):
        # Sobrescribe el método hablar de Animal (polimorfismo)
        print(f"{self.nombre} dice: ¡Guau!")

# Clase Gato que hereda de Animal
class Gato(Animal):
    def __init__(self, nombre, color):
        # Llama al constructor de la clase base para inicializar 'nombre'
        super().__init__(nombre)
        # Inicializa el atributo color específico de Gato
        self.color = color

    def hablar(self):
        # Sobrescribe el método hablar de Animal (polimorfismo)
        print(f"{self.nombre} dice: ¡Miau!")

# Ejemplo de polimorfismo:
animales = [Perro("Rex", "Labrador"), Gato("Michi", "Blanco")]

for animal in animales:
    # Aquí se aplica polimorfismo: cada objeto responde a 'hablar' según su clase
    animal.hablar()