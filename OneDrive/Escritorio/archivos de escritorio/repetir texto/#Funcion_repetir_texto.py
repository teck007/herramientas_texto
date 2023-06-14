from tkinter import *

def repetir_texto():
    texto = texto_input.get()
    repeticiones = int(repeticiones_input.get())
    resultado = texto + ' ' + (texto + ' ') * (repeticiones - 1)
    resultado_label.config(text=resultado)

# Crear la ventana
ventana = Tk()
ventana.title("Repetir Texto")
ventana.geometry("240x200")

# Etiqueta de entrada de texto
texto_label = Label(ventana, text="Texto:")
texto_label.pack()

texto_input = Entry(ventana)
texto_input.pack()

# Etiqueta de entrada de repeticiones
repeticiones_label = Label(ventana, text="Repeticiones:")
repeticiones_label.pack()

repeticiones_input = Entry(ventana)
repeticiones_input.pack()

# Botón para repetir el texto
repetir_boton = Button(ventana, text="Repetir", command=repetir_texto)
repetir_boton.pack()

# Etiqueta de resultado
resultado_label = Label(ventana, text="")
resultado_label.pack()

# Ejecutar la ventana
ventana.mainloop() 
