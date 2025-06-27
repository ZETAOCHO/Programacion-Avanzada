import tkinter as tk

def mostrar_nombre():
    nombre = entrada.get()
    etiqueta.config(text=f"Hola, {nombre}!")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Hola")
ventana.geometry("250x100")

entrada = tk.Entry(ventana)
entrada.pack()

boton = tk.Button(ventana, text="Mostrar nombre", command=mostrar_nombre)
boton.pack()

etiqueta = tk.Label(ventana, text="")
etiqueta.pack()
# Mostrar la ventana
ventana.mainloop()

