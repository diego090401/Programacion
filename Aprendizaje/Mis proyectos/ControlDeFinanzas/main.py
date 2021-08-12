from Operaciones import Egress, Ingress, SeeData,EditData



def run()-> None: 
    print("Bienvenido al inventario  de python ")
    print("Cual de las siguientes operaciones quiere realizar :")
    print("1. Egreso")
    print("2. Ingreso")
    print("3. Ver data")
    print("4. Editar data")
    Election: int = int(input("Eleccion: "))
    if Election == 1 : 
        Egress()
        
    elif Election == 2 :
        Ingress()
        
    elif Election == 3 :
        SeeData() 
        
    elif Election == 4 :
        EditData()
         
    else : 
        raise "No ha ingresado ninguna de las opciones"
if __name__ == "__main__":
    run()