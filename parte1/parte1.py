import tkinter as tk

def mostrar_datos():
    ventana = tk.Tk()
    ventana.title("Nombre y Edad")
    ventana.geometry("300x100")

    nombre = "Juan Pérez"
    edad = 25

    label = tk.Label(ventana, text=f"Nombre: {nombre}\nEdad: {edad}", font=("Arial", 14))
    label.pack(expand=True)  # Para centrar el texto

    ventana.mainloop()

mostrar_datos()