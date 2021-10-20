def Frecuencia():
    while 1==1 :
        Logitud= float(input("Ingrese la longitud de onda en nanometros: "))
        C = 300000000
        Logitud_en_metros = Logitud * 1.0*(10**-9) 
        Frecuencia = C/Logitud_en_metros
        print(Frecuencia)
def Joules():
    while 1==1 :
        Energia = float(input("Ingrese la energia en eV: "))
        Conversion = 1.6021774232052327*(10**-19)
        Joules = (Conversion*Energia)

        print(f'{Joules:.20f}')
Frecuencia()