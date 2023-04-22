
from tkinter import *
from tkinter import messagebox

ventana = Tk()

listbox=Listbox(ventana)
listbox.pack()




def agregarNota():
    try:
        nota=float(entry.get())
        listbox.insert(listbox.size()-1,nota)
        entry.delete(0,END)
    except:
        messagebox.showerror(message="Debe ingresar una nota válida", title="Error_notas")

def calcularPromedio():
    if listbox.size() <= 1:
        messagebox.showinfo(message="Tienes que tener más de una nota para poder sacar el promedio", title="Error_notas")
    else:
        suma = 0

        elementos=listbox.get(0,listbox.size())
        length=len(elementos)

        promedio=sum(elementos)/length if length>0 else 0
        mensaje="El promedio es: {}".format(round(promedio,3))

        # for elemento in elementos:
        #     suma = suma + elemento
        print(mensaje)
        messagebox.showinfo(message=mensaje, title="Promedio")

entry=Entry(ventana)
entry.pack()
ventana.geometry("500x500")#DIMENCION VENTANA PRINCIPAL

etiqueta1=Label(ventana,text="NOMBRE   ",bd=2,bg="pink",font="curier 10")#ETIQUETA NOMBRE font fuente bg color
etiqueta1.place(x=5, y=300)
entrada1=Entry(ventana)
entrada1.place(x=120,y=300)
etiqueta2=Label(ventana,text="APELLIDO  ",bd=2,bg="pink",font="curier 10")#ETIQUETA NOMBRE font fuente bg color)#ETIQUETA APELLIDO
etiqueta2.place(x=5, y=325)


entrada2=Entry(ventana)
entrada2.place(x=120,y=325)
etiqueta3=Label(ventana,text="GRADO      ",bd=2,bg="pink",font="curier 10")#ETIQUETA NOMBRE font fuente bg color)
etiqueta3.place(x=5, y=350)
entrada3=Entry(ventana)
entrada3.place(x=120,y=350)

button_NADA=Button(ventana, text="BIENVENIDO SISTEMA CALIFICACIONES", fg="BLACK", bg="PINK", command=agregarNota)# boton  bienvenida
button_NADA.place(x=120,y=250)

button_agregar=Button(ventana, text="Nueva nota", fg="white", bg="black", command=agregarNota)# boton  agregar notas
button_agregar.pack()#PARA POSICIONAR UNO AL LADO DE OTRO EN CAMBIO X Y Y LE DAN LAS CORDENADAS

button=Button(ventana, text="Calcular", fg="white", bg="black", command=calcularPromedio)# boton calcular promedio
button.pack()
button_Saludar=Button(ventana, text="SALUDAR", fg="BLACK", bg="PINK", command=ventana.iconify)# SALUDAR
button_Saludar.place(x=10,y=400)
button_minimizar=Button(ventana, text="MINIMIZAR", fg="BLACK", bg="PINK", command=ventana.iconify)# SALUDAR
button_minimizar.place(x=80,y=400)
button_salir=Button(ventana, text="SALIR", fg="BLACK", bg="PINK", command=ventana.iconify)# SALUDAR
button_salir.place(x=180,y=400)
def saludar():
    saludo.set("hola"+nombre.get()+"")

    nombre=StringVar()
    apellido=StringVar()
    Grado=StringVar()

    agregarNota()
ventana.mainloop()