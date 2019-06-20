import sys
from tkinter import *
#Evento clic
def hacer_clic():
    try:
        _valor=int(entrada_texto.get())
        _valor=_valor*5
        etiqueta.config(text=_valor)
    except:
        etiqueta.config(text="Ingresa un numero")
app=Tk()
#VENTANA PRINCIPAL
vp=Frame(app)
vp.grid(column=0,row=0,padx=(50,50),pady=(10,10))
vp.columnconfigure(0,weight=1)
vp.rowconfigure(0,weight=1)
#Creacion y diseño de una etuiqueta
etiqueta=Label(vp,text="Valor")
etiqueta.grid(column=2,row=2,sticky=(W,E))
#Creacion de un boton
boton=Button(vp,text="OK",command=hacer_clic)
boton.grid(column=1,row=1)
#Creacion de un cuadro de texto
valor=""
entrada_texto=Entry(vp,width=10,textvariable=valor)
entrada_texto.grid(column=2,row=1)
app.mainloop()
