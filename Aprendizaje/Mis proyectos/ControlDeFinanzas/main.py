from typing import Dict,List

from ManejoDeData import ManejoDeDatos
from FuncLogin import  InsertManyUsers, InsertUser, Login, Update, Compro

Total = 0 
Userid: int = 0
Users :  list[dict]= [{"Userkey": "Prueba", "passwordkey" : "1234" }]
access = False

def run ():
    while True : 
        Eleccion = input("Desea ingresar usuarios ?(s o n) \nEn caso de quere ingresar mas de uno digite sx: ")
        if Eleccion == "s" or Eleccion =="n" or Eleccion == "sx":
            pass
        
        else:
            print("No ha ingresado ninguna de las opciones, intente de nuevo")
            exit()

        if Eleccion == "s":
            InsertUser()
        if Eleccion =="sx":
            InsertManyUsers()

        Eleccion = input("Desea ingresar a su cuenta (s o n) ? ")
        Eleccion.lower()
        Compro(Eleccion)
        if Eleccion == "s":
                access = Login()
                if access == True: 
                    Eleccion = input("Desea utilizar la herramienta de manejo de finanzas ? ")
                    Eleccion.lower()
                    Compro(Eleccion)
                    if Eleccion == "s":
                        ManejoDeDatos(Total)
            

        Eleccion = input("Desea actualizar su clave (s o n) ? ")
        Eleccion.lower()
        Compro(Eleccion)
        if Eleccion == "s":
            Update( access)

        Eleccion = input("Desea volver al inicio (s o n) ? ")
        Eleccion.lower()
        Compro(Eleccion)
        if Eleccion == "s":

            pass
        else:
            exit()
    
if __name__ == "__main__":
    run()
# asd


