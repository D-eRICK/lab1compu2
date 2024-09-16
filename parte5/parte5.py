import tkinter as tk
from tkinter import messagebox

# Función que se ejecuta cuando se presiona el botón
def mostrar_datos():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    direccion = entry_direccion.get()
    telefono = entry_telefono.get()
    email = entry_email.get()
    ocupacion = entry_ocupacion.get()
    nacionalidad = entry_nacionalidad.get()
    estado_civil = entry_estado_civil.get()
    genero = entry_genero.get()
    hobbie = entry_hobbie.get()

    # Mensaje con los datos introducidos
    messagebox.showinfo("Datos de la persona", f"Nombre: {nombre}\nEdad: {edad}\nDirección: {direccion}\nTeléfono: {telefono}\nEmail: {email}\nOcupación: {ocupacion}\nNacionalidad: {nacionalidad}\nEstado Civil: {estado_civil}\nGénero: {genero}\nHobbie: {hobbie}")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Datos de una Persona")

# Etiquetas y campos de entrada para los 10 datos
tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1)

tk.Label(ventana, text="Edad:").grid(row=1, column=0, padx=10, pady=5)
entry_edad = tk.Entry(ventana)
entry_edad.grid(row=1, column=1)

tk.Label(ventana, text="Dirección:").grid(row=2, column=0, padx=10, pady=5)
entry_direccion = tk.Entry(ventana)
entry_direccion.grid(row=2, column=1)

tk.Label(ventana, text="Teléfono:").grid(row=3, column=0, padx=10, pady=5)
entry_telefono = tk.Entry(ventana)
entry_telefono.grid(row=3, column=1)

tk.Label(ventana, text="Email:").grid(row=4, column=0, padx=10, pady=5)
entry_email = tk.Entry(ventana)
entry_email.grid(row=4, column=1)

tk.Label(ventana, text="Ocupación:").grid(row=5, column=0, padx=10, pady=5)
entry_ocupacion = tk.Entry(ventana)
entry_ocupacion.grid(row=5, column=1)

tk.Label(ventana, text="Nacionalidad:").grid(row=6, column=0, padx=10, pady=5)
entry_nacionalidad = tk.Entry(ventana)
entry_nacionalidad.grid(row=6, column=1)

tk.Label(ventana, text="Estado Civil:").grid(row=7, column=0, padx=10, pady=5)
entry_estado_civil = tk.Entry(ventana)
entry_estado_civil.grid(row=7, column=1)

tk.Label(ventana, text="Género:").grid(row=8, column=0, padx=10, pady=5)
entry_genero = tk.Entry(ventana)
entry_genero.grid(row=8, column=1)

tk.Label(ventana, text="Hobbie:").grid(row=9, column=0, padx=10, pady=5)
entry_hobbie = tk.Entry(ventana)
entry_hobbie.grid(row=9, column=1)

# Botón para mostrar los datos
tk.Button(ventana, text="Mostrar Datos", command=mostrar_datos).grid(row=10, column=0, columnspan=2, pady=10)

# Iniciar el bucle de la ventana
ventana.mainloop()
