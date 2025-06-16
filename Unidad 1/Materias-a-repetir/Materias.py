# Hacer un programa que guarde las materias que se cursan en un cuatrimestre(Sistemas de control, 
# Programacion Avanzada,Ingles, Ingenieria de Proyectos,Sistemas Mecanicos, , ,) en una lista, 
# preguntar al usuario la calificacion que obtuvo en cada una de ellas y elimine de la lista 
# las materias reprobadas.Al final, el programa debe mostrar en pantalla las que debe repetir

# Lista de materias que se cursan en el cuatrimestre
materias = [
    "Sistemas de control",
    "Programacion Avanzada",
    "Ingles",   
    "Ingenieria de Proyectos",
    "Sistemas Mecanicos"
]

# Lista para guardar las materias reprobadas
materias_reprobadas = []

# Ciclo para pedir la calificación de cada materia
for materia in materias:
    calificacion = float(input(f"Ingrese la calificacion de {materia}: "))
    # Si la calificación es menor a 7, se agrega a la lista de reprobadas
    if calificacion < 7.0:
        materias_reprobadas.append(materia)

# Muestra las materias a repetir, si las hay
if materias_reprobadas:
    print("Materias a repetir:")
    for materia in materias_reprobadas:
        print(materia)
else:
    # Si no hay materias reprobadas
    print("No hay materias a repetir.")

