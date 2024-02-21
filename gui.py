from tkinter import *
import pandas as pd
from tkinter import filedialog

Raiz = Tk()
Raiz.title('Actividad 4')
Raiz.config(width=900, height=800)

#Funciones nuevas----------------------------------------------------
def leer():
    global filename
    # Configurar los tipos de archivo a mostrar (solo archivos CSV)
    filetypes = [('Archivos CSV', '*.csv')]
    filename = filedialog.askopenfilename(filetypes=filetypes)

    if filename:
        df = pd.read_csv(filename, header=0)
        original_string = df['string_a_modificar'][0]
        print(original_string)
        posiciones()
        referencia()
        alteracion()
        return original_string

def posiciones():
    global filename
    df = pd.read_csv(filename, header=0)
    pos = df['posicion'].tolist()
    print(pos)
    return pos

def referencia():
    global filename
    df = pd.read_csv(filename, header=0)
    ref = df['referencia'].str.cat()
    print(ref)
    return ref

def alteracion():
    global filename
    df = pd.read_csv(filename, header=0)
    alt = df['alteracion'].str.cat()
    print(alt)
    return alt
#------------------------------------------------------------------------------------------------------
MFrame = Frame(Raiz)
MFrame.config(width=900, height=800, bg="#DBF5EF")
MFrame.pack()

Titulo = Label(MFrame, text="Bienvenido al programa", font=('Ubuntu Mono', 20), bg="#18757B")
Titulo.grid(row=0, columnspan=4)

Espacio = Label(MFrame, bg="#DBF5EF")
Espacio.grid(row=1, column=1)

Boton1 = Button(MFrame, text="Mostrar variante\n elegida",bg="#555C5D",fg="white")
Boton1.grid(row=2, column=0, ipadx=5, ipady=5, padx=10, pady=50)

Boton2 = Button(MFrame, text="Generar combinación elegida\n y guardar en csv",bg="#555C5D",fg="white")
Boton2.grid(row=2, column=1, ipadx=5, ipady=5, padx=10, pady=50)

Boton3 = Button(MFrame, text="Abrir cvs\n original", command=leer,bg="#555C5D",fg="white")
Boton3.grid(row=2, column=2, ipadx=5, ipady=5, padx=10, pady=50)

Boton4 = Button(MFrame, text="Abrir cvs\n de combinaciones",bg="#555C5D",fg="white")
Boton4.grid(row=2, column=3, ipadx=5, ipady=5, padx=10, pady=50)

Raiz.mainloop()
