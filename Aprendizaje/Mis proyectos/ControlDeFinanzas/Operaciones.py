def Egress(Total: int) :
        
        Monto = input("Ingrese el monto que desea egresar del total: ")
        try: 
            Monto = int(Monto)
        except : 
            print( "El valor ingresado no es un monto")
            exit()
        Comentario = input( "Ingrese el detalle del egreso: ")
        Total = int (Total) - int(Monto)
        str(Total)
        str(Monto)
        
        TotalLine = "Total ="
        EgressLine = "Egreso = "
        Newline: str =EgressLine, Monto ,  Comentario, TotalLine, Total
        str(Newline)

        with open ("Data.txt", 'a', encoding= "utf-8") as Data : 
            Data.writelines(str(Newline))
            Data.write("\n")
               
def Ingress(Total: int ) : 
        Monto = input("Ingrese el monto que desea ingresar al total: ")
        try: 
            Monto = int(Monto)
        except : 
            print( "El valor ingresado no es un monto")
            exit()
        Comentario = input( "Ingrese el detalle del egreso: ")
        Total = int(Monto) - int(Total)
        str(Total)
        str(Monto)
        
        TotalLine = "Total ="
        Newline: str = Monto ,  Comentario, TotalLine, Total
        str(Newline)
    
def SeeData() :
    Text: list =[ ]
    with open( "Aprendizaje\Mis proyectos\ControlDeFinanzas\Data.txt", 'r', encoding= "utf-8" ) as Data : 
        for line in Data :
            print(line)
            
def EditData() :
    pass

