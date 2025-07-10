import tkinter as tk  # Importa el módulo tkinter para crear interfaces gráficas

# Función que se ejecuta al presionar el botón "Sumar"
def Generar_suma():
    # Obtiene los valores de los campos de entrada y los convierte a enteros
    num1 = Number_1.get()
    num2 = Number_2.get()
    try:

        if num1.count(".") == 1 or num2.count(".") == 1:
            suma = float(num1) + float(num2)
            etiqueta.config(text=f"La suma es: {suma}")
        elif num1.count(".") == 0 or num2.count(".") == 0:
            suma = int(num1) + int(num2)  # Realiza la suma
            etiqueta.config(text=f"La suma es: {suma}")  # Actualiza el texto de la etiqueta con el resultado

    except ValueError:
        etiqueta.config(text="Por favor, ingrese números válidos")  # Muestra un mensaje de error si la entrada no es válida

# Crear la ventana principal
ventana = tk.Tk()  # Crea la ventana principal de la aplicación
ventana.title("Sumas")  # Establece el título de la ventana
ventana.geometry("250x100")  # Establece el tamaño de la ventana

Number_1 = tk.Entry(ventana)  # Campo de entrada para el primer número
Number_1.pack()  # Muestra el campo en la ventana

Number_2 = tk.Entry(ventana)  # Campo de entrada para el segundo número
Number_2.pack()  # Muestra el campo en la ventana

boton = tk.Button(ventana, text="Sumar", command=Generar_suma)  # Botón que ejecuta la suma
boton.pack()  # Muestra el botón en la ventana

etiqueta = tk.Label(ventana, text="La suma es: ")  # Etiqueta para mostrar el resultado
etiqueta.pack()  # Muestra la etiqueta en la ventana

# Mostrar la ventana y esperar acciones del usuario
ventana.mainloop()
