from tkinter import*

Raiz= Tk()
Raiz.title('Procesamiento por lotes')
Raiz.config(width=900,height=800)
#-----------------------------------------------------------

MFrame=Frame(Raiz)
MFrame.config(width=900,height=800,bg="#DBF5EF")
MFrame.pack()

#-----------------------------------------------------------
Titulo=Label(MFrame,text="Bienvenido al programa",font=('Ubuntu Mono',20),bg="#A8CDC5")
Titulo.grid(row=0,columnspan=4)
Espacio=Label(MFrame,bg="#DBF5EF")
Espacio.grid(row=1,column=1)
Boton1=Button(MFrame,text="Mostrar variante\n elegida")
Boton1.grid(row=2,column=0,ipadx=5,ipady=5,padx=10,pady=50)
Boton1=Button(MFrame,text="Generar combinación elegida\n y guardar en csv")
Boton1.grid(row=2,column=1,ipadx=5,ipady=5,padx=10,pady=50)
Boton1=Button(MFrame,text="Abrir cvs\n original")
Boton1.grid(row=2,column=2,ipadx=5,ipady=5,padx=10,pady=50)
Boton1=Button(MFrame,text="Abrir cvs\n de combinaciones")
Boton1.grid(row=2,column=3,ipadx=5,ipady=5,padx=10,pady=50)

Raiz.mainloop()