from tkinter import *
from tkinter import messagebox


def multiplicar():
    # obtener el texto ingresado
    entrada= entrada_numero.get().strip()
    if not entrada.isdigit():
        messagebox.showerror("Error", "Por favor, ingresa un número válido.")
        return

    numero = int(entrada)

    area_resultado.configure(state="normal")# Habilitar para escribir
    area_resultado.delete(1.0, END)# Limpiar resultado anterior

    # tabla de multiplicar
    area_resultado.insert(END, f"--- Tabla del {numero} ---\n\n")
    for i in range (1,11):
        resultado= f"{numero} x {i} = {numero*i}\n"
        area_resultado.insert(END, resultado)

    area_resultado.configure(state="disabled")# Bloquear para evitar edición del usuario


def limpiar():
    entrada_numero.delete(0, END)
    area_resultado.configure(state="normal")
    area_resultado.delete(1.0, END)
    area_resultado.configure(state="disabled")
    entrada_numero.focus()

# configuración de ventana
ventana = Tk()
ventana.title("Tabla de multiplicar")
ventana.geometry("500x500")

# etiquetas de instriccion
lbl_instruccion= Label(ventana, text="Ingrese un numero")
lbl_instruccion.pack(pady=5)# Agrega 5 píxeles de espacio vacío arriba y abajo del botón
                            # padx Agrega 5 píxeles de espacio vacío a la izquierda y derecha del botón
# campo de entrada
entrada_numero = Entry(ventana, font=("Arial", 12), justify="center")
entrada_numero.pack(pady=5)
entrada_numero.focus()

# si se importa from tkinter import * no es necesario usar tk.
btn_calcular= Button(
    ventana,
    text="Generar Tabla",
    command=multiplicar,
    bg="white",  # color fondo
    fg="black",  # color letra
    font=("Arial", 12),
)
btn_calcular.pack(pady=10)

# área de resultado de la tabla
area_resultado= Text(ventana, height=12, width=28, font=("Arial", 12))
area_resultado.pack(pady=10)
area_resultado.configure(state="disabled")# inicia bloqueado

btn_limpiar= Button(
    ventana,
    text="Consultar otro numero",
    command=limpiar,
    bg="white",# color fondo
    fg="black",# color letra
    font=("Arial", 12),
)
btn_limpiar.pack(pady=5)

# iniciar interfaz grafica
ventana.mainloop()