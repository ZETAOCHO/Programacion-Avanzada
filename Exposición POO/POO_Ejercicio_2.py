


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