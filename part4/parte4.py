import tkinter as tk

def mostrar_mascotas():
    mascota1 = f"Nombre: {entry_mascota1.get()}, Edad: {entry_edad1.get()}, Tipo: {entry_tipo1.get()}"
    mascota2 = f"Nombre: {entry_mascota2.get()}, Edad: {entry_edad2.get()}, Tipo: {entry_tipo2.get()}"
    mascota3 = f"Nombre: {entry_mascota3.get()}, Edad: {entry_edad3.get()}, Tipo: {entry_tipo3.get()}"
    print(mascota1)
    print(mascota2)
    print(mascota3)
    ventana.destroy()

ventana = tk.Tk()
ventana.title("Datos de las Mascotas")
ventana.geometry("400x300")

# Mascota 1
tk.Label(ventana, text="Mascota 1").pack()
entry_mascota1 = tk.Entry(ventana)
entry_mascota1.pack()
tk.Label(ventana, text="Edad").pack()
entry_edad1 = tk.Entry(ventana)
entry_edad1.pack()
tk.Label(ventana, text="Tipo").pack()
entry_tipo1 = tk.Entry(ventana)
entry_tipo1.pack()

# Mascota 2
tk.Label(ventana, text="Mascota 2").pack()
entry_mascota2 = tk.Entry(ventana)
entry_mascota2.pack()
tk.Label(ventana, text="Edad").pack()
entry_edad2 = tk.Entry(ventana)
entry_edad2.pack()
tk.Label(ventana, text="Tipo").pack()
entry_tipo2 = tk.Entry(ventana)
entry_tipo2.pack()

# Mascota 3
tk.Label(ventana, text="Mascota 3").pack()
entry_mascota3 = tk.Entry(ventana)
entry_mascota3.pack()
tk.Label(ventana, text="Edad").pack()
entry_edad3 = tk.Entry(ventana)
entry_edad3.pack()
tk.Label(ventana, text="Tipo").pack()
entry_tipo3 = tk.Entry(ventana)
entry_tipo3.pack()

boton = tk.Button(ventana, text="Aceptar", command=mostrar_mascotas)
boton.pack()

ventana.mainloop()