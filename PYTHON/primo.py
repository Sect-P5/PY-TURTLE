kk = 1
import time
   
#inicio de programa

while kk <= 100:
    print("******************************")
    NU = int(input("¿que numero? "))
    primo = "sí"

#buscador de primos

    for f in range(1, NU):
        if NU%f == 0:
            if not f == 1: 
                primo = "no"

#resolucion

    print(" ")
    print((primo) + (" es primo"))
    print("==========================")
    
#¿otra?

    pregunta = input("¿otro numero? ")
    if pregunta == "si":
        print("==========================")
        print(" ")
    if pregunta == "no":
          break

#final
          
time.sleep (2)
