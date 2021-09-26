import math
def Operacion(Lista):
  if len(Lista)&2 == 0:
    resultado = Lista[(((len(Lista))+1)//2)-1]
  else:
    A , B = (len(Lista))//2 , ((len(Lista))//2) + 1
    resultado = float((Lista[A-1] + Lista[B-1])/2)
  return resultado
def Calculos(Opcion, Valor):
  if Opcion == 1:
    return math.sqrt(Valor)
  elif Opcion ==2 :
    return math.degrees(Valor)
  elif Opcion == 3 :
    return math.log(Valor, 4)
  elif Opcion == 4 :
    if Valor == int(Valor):
      return math.factorial(Valor)
    else:
      return math.factorial(Valor//1+1)
def run() :
  Licencia = sorted(set([int(i) for i in input("Por favor ingrese su clave con formato xxx-xxx-xxx-xxx: ") if i != "-" and int(i) != 0 ]))
  Valor = Operacion(Licencia)
  Opcion = int(input("Ingrese una opcion: "))
  print(Calculos(Opcion, Valor))
if __name__ =="__main__":
  run()