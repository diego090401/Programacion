a = (1,2,3,8)
b = (4,6,7,8)
lista = []
total = 0

for i in range (len(a)):
    lista.append( a[i]* b[i])
    print(lista[i])

for k in lista:
    total = total + k
print(total)