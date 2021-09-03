
def i_want_to_sort(Cedula):
    Cedula = [ int(i) for i in list(Cedula) if i != "-"]
    Mayor = max(Cedula)
    return Mayor
def i_want_options(Mayor):
    
    if Mayor ==1:
        Output ="su numero es " + str(Mayor)
    if Mayor ==2:
        Output ="su numero es " + str(Mayor)
    if Mayor ==3:
        Output ="su numero es " + str(Mayor)
    if Mayor ==4:
        Output ="su numero es " + str(Mayor)
    if Mayor ==5:
        Output ="su numero es " + str(Mayor)
    if Mayor ==6:
        Output ="su numero es " + str(Mayor)
    if Mayor ==7:
        Output ="su numero es " + str(Mayor)
    if Mayor ==8 :
      Output ="su numero es " + str(Mayor)
    if Mayor ==9:
        Output ="su numero es " + str(Mayor)
    return Output

def run():
    Cedula = input("Ingrese su cedula con formato x-xxxx-xxx: ")
    Mayor =i_want_to_sort(Cedula)
    Output = i_want_options(Mayor)
    print(Output)
    
if __name__ == "__main__":
    run()
