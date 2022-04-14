from tkinter import *
from tkinter import ttk as ttk
from tkinter import messagebox
import mariadb

class CmA:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("CmA")
        self.ventana.geometry("800x600")
        self.ventana.config(bg="black")

        #Creacion de los marcos para dar mas orden al programa
        self.flbl1 = LabelFrame(self.ventana, text="Datos del cliente", font=("Arial", 12))
        self.flbl1.pack(fill="both", expand="False", padx="20", pady="10")
        self.flbl2 = LabelFrame(self.ventana, text="Datos del vendedor", font=("Arial", 12))
        self.flbl2.pack(fill="both", expand="False", padx="20", pady="10")
        self.flbl3 = LabelFrame(self.ventana, text="Lista de clientes")
        self.flbl3.pack(fill="both", expand="True", padx="20", pady="10")

        
        #Creacion de las casillas para el ingreso de datos en el marco flbl1
        Label(self.flbl1, text="Ruc/Dni:").grid(row=0, column=0)
        Entry(self.flbl1,).grid(row=0, column=1)
        Label(self.flbl1, text="Nombre:").grid(row=1, column=0)
        Entry(self.flbl1,).grid(row=1, column=1)
        Label(self.flbl1, text="Provincia:").grid(row=2, column=0)
        Entry(self.flbl1,).grid(row=2, column=1)
        Label(self.flbl1, text="Direccion:").grid(row=0, column=3)
        Entry(self.flbl1,).grid(row=0, column=4)
        Label(self.flbl1, text="Telefono:").grid(row=1, column=3)
        Entry(self.flbl1,).grid(row=1, column=4)
        Label(self.flbl1, text="Correo:").grid(row=2, column=3)
        Entry(self.flbl1,).grid(row=2, column=4)

        #creacion de los botones para el marco flbl1
        Button(self.flbl1, text="Agregar",padx=10,pady=2).grid(row=3, column=0)
        Button(self.flbl1, text="Modificar",padx=10,pady=2).grid(row=3, column=1)
        Button(self.flbl1, text="Eliminar",padx=10,pady=2).grid(row=3, column=2)
        Button(self.flbl1, text="Limpiar",padx=10,pady=2).grid(row=3, column=3)




        #creacion de las casillas la busqueda de datos en el marco flbl2
        Label(self.flbl2, text="Buscar:").grid(row=0, column=0)
        Entry(self.flbl2,).grid(row=0, column=1)

        #creacion de boton para buscar datos en el marco flbl2
        Button(self.flbl2, text="Buscar").grid(row=0, column=2)
        





if __name__ == '__main__':
    ventana=Tk()
    app=CmA(ventana)
    ventana.mainloop()