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
