#PROGRAMA QUE INCLUYE HERRAMIENTAS PARA TEXTOS
#importa libreria para interfaz gráfica
from tkinter import *

#importa funciones de archivos
from contar_letras import * 
from linea_azar import *

#crea objeto ventana 
ventana = Tk() 
ventana.config(width='800', height='600')
ventana.title("Herramientas de texto V.1.0")

#Bloquear el cambio de tamaño de la ventana
ventana.resizable(False, False)

#crea un primer label
lbl1= Label(ventana, text="Entrada de texto", font=("Arial Bold",14))
#define ubicación del label 1
lbl1.place(x=50, y=20)

#crea un segundo label
lbl2 = Label(ventana, text="Resultado", font=("Arial Bold",14))
#define ubicación del label 1
lbl2.place(x=50, y=320)

#crea un campo de texto para ingresar
txt_in = Text(ventana)
txt_in.place(x=50, y=50, width=600, height=200)

#crea un campo de texto para el resultado
txt_out = Text(ventana)
txt_out.place(x=50, y=350, width=600, height=200)

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
btn_contar_letras = Button(ventana, text="Contar letras", command=lambda: resultado(contar_letras(txt_in.get("1.0","end-1c"))))
btn_buscar_reemplazar = Button(ventana, text="Buscar reemplazar",command=lambda: open_popup())
btn_linea_azar =Button(ventana,text="Linea alazar",command=lambda: resultado(linea_azar(txt_in.get("1.0","end-1c"))))

#define ubicación del botón
#btn_mover_resultado.place(x=10,y=50)
btn_contar_letras.place(x=50, y=260)
# btn_reversa_de_texto.place(x=160,y=260)
# btn_eliminar_espacios.place(x=270,y=260)
# btn_contar_palabras.place(x=400,y=260)
# btn_buscar_reemplazar.place(x=520,y=260)
# Linea Abajo
# btn_borrar_espacios_extra.place(x=50, y=290)
# btn_ordenar_lista.place(x=80,y=290)
btn_linea_azar.place(x=200,y=260)
ventana.mainloop()