#Boton en TKinter 
#Los botones son los controles mas empleados en aplicaciones graficas 
#Un boton es un elemento con un texto y/o imagen  que al ser activados pr el usuario
#(presionado), ejecuta una operacion definida. En TKinter, esta representado por las
#clases tk.Button y ttk.Button; como cualquier otro control de TKinter, para crear un boton
#debemos crear una instancia de la clase correspondiente.
#En el siguiente codigo e crea una ventanacon un boton, cuyo texto esta representado por 
#el parametro text(IMEC91M)

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.config(width=300, height=200)
root.title("Boton en TK")
root.config(bg="lightblue")
root.config(cursor="no")  # Cambia el cursor a "no disponible")
boton = ttk.Button(text="¡Mecatronica, IMEC91M!")
boton.place(x=50, y=50)
root.mainloop()

#Tarea:
#Hacer una calculadora basica
