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
        Entry(self.flbl1).grid(row=0, column=1)
        Label(self.flbl1, text="Nombre:").grid(row=1, column=0)
        Entry(self.flbl1).grid(row=1, column=1)
        Label(self.flbl1, text="Ciudad:").grid(row=2, column=0)
        Entry(self.flbl1).grid(row=2, column=1)
        Label(self.flbl1, text="Direccion:").grid(row=0, column=3)
        Entry(self.flbl1).grid(row=0, column=4)
        Label(self.flbl1, text="Telefono:").grid(row=1, column=3)
        Entry(self.flbl1).grid(row=1, column=4)
        Label(self.flbl1, text="Correo:").grid(row=2, column=3)
        Entry(self.flbl1).grid(row=2, column=4)

        #creacion de los botones para el marco flbl1
        ttk.Button(self.flbl1, text="Agregar").grid(row=3, column=0)
        ttk.Button(self.flbl1, text="Modificar").grid(row=3, column=1)
        ttk.Button(self.flbl1, text="Eliminar").grid(row=3, column=2)
        #ttk.Button(self.flbl1, text="Limpiar").grid(row=3, column=3)

        #creacion de las casillas la busqueda de datos en el marco flbl2
        Label(self.flbl2, text="Buscar:").grid(row=0, column=0)
        Entry(self.flbl2,).grid(row=0, column=1)

        #creacion de boton para buscar datos en el marco flbl2
        ttk.Button(self.flbl2, text="Buscar").grid(row=0, column=3)

        #treeview para mostrar los datos en el marco flbl3
        self.tabla=ttk.Treeview(self.flbl3, columns=("#0","#1","#2","#3","#4","#5"))
        self.tabla.grid(row=0, column=0, sticky="nsew")
        self.tabla.heading("#0", text="Ruc/Dni", anchor="center")
        self.tabla.heading("#1", text="Nombre", anchor="center")
        self.tabla.heading("#2", text="Ciudad", anchor="center")
        self.tabla.heading("#3", text="Direccion", anchor="center")
        self.tabla.heading("#4", text="Telefono",anchor="center")
        self.tabla.heading("#5", text="Correo", anchor="center")







        #conexion a la base de datos de cma
    def ConsultaClientes(self, query):
        try:
            conn=mariadb.connect(
            user='root', 
            password='', 
            database='cma', 
            host='localhost'
            )
        except mariadb.Error as e:
            print("Error al conectarse a la base de datos",e)
        cur=conn.cursor()
        cur.execute(query)
        return cur
    def MostrarDatos(self):
        cur = self.ConsultaClientes("SELECT `ruc_dni`,`nombre`,`ciudad`,`direccion`,`telefono`,`email` FROM `customers`")
        for (ruc_dni,nombre,ciudad,direccion,telefono,email) in cur:
            print(ruc_dni,nombre,ciudad,direccion,telefono,email)







if __name__ == '__main__':
    ventana=Tk()
    app=CmA(ventana)
    app.MostrarDatos()
    ventana.mainloop()