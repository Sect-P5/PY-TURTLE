import time
x=1
y=1
pp= int(input("cuantas notas "))

print("="*15)

while x <= 1:
    lista1=[]
    for x in range (pp):
        while y <= 1:
            res= float(input("¿nota? "))
            if res > 10:
                print("solo notas menores de 10")
            if res < 0:
                print("solo notas mayores de 0")
            if res < 10:
                lista1.append(res)
                break

    #saca la media
            
    suma=float(sum(lista1))
    div=len(lista1)
    print(suma/div)

    #finalizacion del bucle

    i=input("¿otra media? ")
    if str.lower(i)== "si":
        print()
        print("="*15)
    else:
        break
