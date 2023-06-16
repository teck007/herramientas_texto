#PROGRAMA QUE INCLUYE HERRAMIENTAS PARA TEXTOS
#importa libreria para interfaz gráfica y fondo
from tkinter import *
from PIL import ImageTk, Image, ImageFont, ImageDraw

#importa funciones de archivos
from contar_letras import *
from borrar_espacios_extra import *

#crea objeto ventana 
ventana = Tk() 
ventana.config(width='1330', height='570', background="#5dc1b9")
ventana.title("Herramientas de texto V.1.0")

#Bloquear el cambio de tamaño de la ventana
ventana.resizable(False, False)

# Esto es para verificar que la imagen del fondo está en la ubicación acordada.
import os
if not os.path.isfile("./17010.jpg"):
    print("El archivo '17010.jpg' no existe en la ubicación especificada.")

### FONDO ###
imagen_fondo = Image.open("17010.jpg")
imagen_fondo = imagen_fondo.resize((1330, 570), Image.ANTIALIAS)
fondo = ImageTk.PhotoImage(imagen_fondo)

label_fondo = Label(ventana, image=fondo)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

#Abre y cierre de marco decorativo dentro de la ventana
lbl1= Label(ventana, text="╭══　　　　　　　　　　Herramientas de texto　　　　　　　　　══╮", font=("Arial Bold",14), background="#05294D", fg="white")
lbl_CierreDecorativo_lbl1= Label(ventana, text="╰══　　　　　　　　　　　　　　　　　　　　　　　　　　　　　　══╯", font=("Arial Bold",14), background="#05294D", fg="white")
#Define ubicación del abre y cierre del marco decorativo dentro de la ventana
lbl1.place(x=345, y=15)
lbl_CierreDecorativo_lbl1.place(x=345,y=150)

#crea label "Ingresa texto" y "Resultado"
lbl_resul = Label(ventana, text="»»————　↓ ★ Resultado ★ ↓　————««", font=("Arial Bold",14), background="#05294D", fg="white")
lbl_ingrese = Label(ventana, text="»»————　↓ ★ Ingrese texto aquí ★ ↓　————««", font=("Arial Bold",14), background="#05294D", fg="white")
#define ubicación del label 2
lbl_resul.place(x=775, y=250)
lbl_ingrese.place(x=110, y=250)


#crea un campo de texto para ingresar
txt_in =Text(ventana)
txt_in.place(x=50, y=290, width=600, height=200)

#crea un campo de texto para el resultado
txt_out = Text(ventana)
txt_out.place(x=680, y=290, width=600, height=200)

#función que envia el resultado al campo de texto
def resultado(texto):
	txt_out.delete("1.0", END)
	txt_out.insert(END, texto)
def mover_resultado(texto):
	txt_out.delete("1.0", END)
	txt_out.insert(END, texto)


def open_popup():
	top = Toplevel(ventana)

	#Bloquear el cambio de tamaño de la ventana
	top.resizable(False, False)
	
	top.geometry("240x200")
	top.title("Buscar y reemplazar")
	Label(top, text= "Texto a buscar", font=('Mistral 10 bold')).place(x=40,y=20)
	txt_bus=Entry(top, textvariable="")
	txt_bus.place(x=40,y=45)
	Label(top, text= "Texto a reemplazar", font=('Mistral 10 bold')).place(x=40,y=80)
	txt_ree=Entry(top, textvariable="")
	txt_ree.place(x=40,y=105)
	Button(top, text="Buscar reemplazar",command=lambda: resultado(buscar_reemplazar(txt_in.get("1.0","end-1c"),txt_bus.get(),txt_ree.get()))).place(x=50,y=150)
	
	#Centrar ventana sobre ventana madre 
	top.wm_transient(ventana)
	top.mainloop()

#crea un botón
btn_contar_letras = Button(ventana, text="       Contar letras        ", command=lambda: resultado(contar_letras(txt_in.get("1.0","end-1c"))))
btn_contar_palabras = Button(ventana, text=" Contar palabras ",command=lambda: resultado(contar_palabras(txt_in.get("1.0","end-1c"))))
btn_reversa_de_texto = Button(ventana, text="Invertir texto", command=lambda: resultado(invertir_texto(txt_in.get("1.0","end-1c"))))
btn_borrar_espacios_extra= Button(ventana, text="Eliminar espacios extra", command=lambda:resultado(borrar_espacios_extra(txt_in.get("1.0","end-1c"))))
btn_eliminar_espacios = Button(ventana, text="Eliminar espacios", command=lambda: resultado(eliminar_espacios(txt_in.get("1.0","end-1c"))))
btn_ordenar_lista = Button(ventana, text="Ordenar lista", command=lambda: resultado(ordenar_lista(txt_in.get("1.0","end-1c"))))

#define ubicación del botón
# btn_mover_resultado.place(x=10,y=50)
btn_contar_letras.place(x=405, y=60)
btn_contar_palabras.place(x=630,y=60)
btn_reversa_de_texto.place(x=825,y=60)
# Linea Abajo
btn_borrar_espacios_extra.place(x=405, y=105)
btn_eliminar_espacios.place(x=630,y=105)
btn_ordenar_lista.place(x=825,y=105)
ventana.mainloop()