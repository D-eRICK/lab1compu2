import tkinter as tk

def obtener_clave():
    clave = entry.get()
    print(f"Clave ingresada: {clave}")
    ventana.destroy()

ventana = tk.Tk()
ventana.title("Clave Secreta")
ventana.geometry("300x100")

label = tk.Label(ventana, text="Ingresa la clave:", font=("Arial", 12))
label.pack()

entry = tk.Entry(ventana, show="*")
entry.pack()

boton = tk.Button(ventana, text="Aceptar", command=obtener_clave)
boton.pack()

ventana.mainloop()