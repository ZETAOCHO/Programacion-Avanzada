import tkinter as tk  # Importa el módulo tkinter para interfaces gráficas

# Colores personalizados para el tema de la calculadora
BG_COLOR = "#FF00BF"         # Color de fondo de la ventana principal
BTN_COLOR = "#B4228F"        # Color de fondo de los botones
BTN_TEXT_COLOR = "#eeeeee"   # Color del texto de los botones
ENTRY_BG = "#8A0F6C"         # Color de fondo del campo de entrada
ENTRY_FG = "#000000"         # Color del texto del campo de entrada

# Función que maneja los clics en los botones de la calculadora
def click(event):
    current = entry.get()  # Obtiene el texto actual del campo de entrada
    text = event.widget.cget("text")  # Obtiene el texto del botón presionado
    if text == "=":
        try:
            result = str(eval(current))  # Evalúa la expresión matemática ingresada
            entry.delete(0, tk.END)      # Borra el campo de entrada
            entry.insert(0, result)      # Inserta el resultado en el campo de entrada
        except Exception:
            entry.delete(0, tk.END)      # Si hay error, borra el campo de entrada
            entry.insert(0, "Error")     # Muestra "Error" en el campo de entrada
    elif text == "C":
        entry.delete(0, tk.END)          # Borra todo el campo de entrada si se presiona "C"
    else:
        entry.insert(tk.END, text)       # Agrega el texto del botón al final del campo de entrada

root = tk.Tk()                           # Crea la ventana principal de la aplicación
root.title("Calculadora Básica")         # Establece el título de la ventana
root.configure(bg=BG_COLOR)              # Aplica el color de fondo personalizado

# Frame principal con margen para separar la calculadora del borde de la ventana
main_frame = tk.Frame(root, bg=BG_COLOR)
main_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)  # Usa grid en vez de pack

# Campo de entrada donde se muestran los números y resultados
entry = tk.Entry(
    main_frame, font="Arial 20", borderwidth=8, relief="ridge", justify="right",
    bg=ENTRY_BG, fg=ENTRY_FG, insertbackground=ENTRY_FG
)
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")  # Ubica el campo de entrada en el grid

# Lista con los textos de los botones de la calculadora
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", "C", "=", "+"
]

# Crea y coloca los botones en la ventana usando un grid
for i, text in enumerate(buttons):# Enumerate para obtener el índice y el texto de cada botón
    btn = tk.Button(
        main_frame, text=text, font="Arial 18", width=4, height=2,
        bg=BTN_COLOR, fg=BTN_TEXT_COLOR, activebackground="#000000", activeforeground="#222831"
    )
    btn.grid(row=1 + i // 4, column=i % 4, padx=2, pady=2, sticky="nsew")  # Posiciona el botón en el grid
#   row=1 + i // 4: Calcula la fila para cada botón.
#   column=i % 4: Calcula la columna para cada botón.
#   padx=2, pady=2: Añade espacio alrededor del botón.
#   sticky="nsew": Hace que el botón se expanda para llenar la celda.
    btn.bind("<Button-1>", click)  # Asocia la función click a cada botón

# Configura el tamaño de las columnas para que se expandan al redimensionar la ventana
for i in range(4):
    main_frame.grid_columnconfigure(i, weight=1)
    root.grid_columnconfigure(0, weight=1)
# Configura el tamaño de las filas para que se expandan al redimensionar la ventana
for i in range(5):
    main_frame.grid_rowconfigure(i, weight=1)
    root.grid_rowconfigure(0, weight=1)


root.mainloop()  # Inicia el bucle principal de la interfaz gráfica