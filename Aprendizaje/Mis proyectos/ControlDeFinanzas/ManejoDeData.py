from Operaciones import Egress, Ingress, SeeData,EditData
def ManejoDeDatos(Total) :
        print("Bienvenido al inventario  de python ")
        print("Cual de las siguientes operaciones quiere realizar :")
        print("1. Egreso")
        print("2. Ingreso")
        print("3. Ver data")
        print("4. Editar data")
        Election: int = int(input("Eleccion: "))
        try : 
            Election = int(Election)
        except : 
            print("El valor ingresado no es un numero valido")
            exit()
        if Election == 1 : 
            Egress(Total)
            
        elif Election == 2 :
            Ingress(Total)
            
        elif Election == 3 :
            SeeData() 
            
        elif Election == 4 :
            EditData()
            
        else : 
            raise "No ha ingresado ninguna de las opciones"
