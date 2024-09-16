import tkinter as tk

def mostrar_datos():
    cedula = entry_cedula.get()
    nombre = entry_nombre.get()
    print(f"Cédula: {cedula}, Nombre: {nombre}")
    ventana.destroy()

ventana = tk.Tk()
ventana.title("Cédula y Nombre")
ventana.geometry("300x150")

label_cedula = tk.Label(ventana, text="Ingrese su cédula:")
label_cedula.pack()
entry_cedula = tk.Entry(ventana)
entry_cedula.pack()

label_nombre = tk.Label(ventana, text="Ingrese su nombre completo:")
label_nombre.pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

boton = tk.Button(ventana, text="Aceptar", command=mostrar_datos)
boton.pack()

ventana.mainloop()