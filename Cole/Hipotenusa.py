import math
def hipotenusa():
    a = float(input("Ingrese el valor del cateto: "))
    b =float(input("Inngrese el valor del cateto: "))
    hipotenusa =round( math.sqrt(((a*a) + (b*b))),3)
    return hipotenusa

hipotenusa = float(hipotenusa())
print(hipotenusa)
print(2*hipotenusa)
2