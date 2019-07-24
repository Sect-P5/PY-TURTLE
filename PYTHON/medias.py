import time
print()
print("------ SOLO SE PUEDEN PONER 6 NOTAS --------")
print()
time.sleep (1)

x = 1
while x <= 1000:
    #notas
    n=0
    caracter1 = int(input("nota 1 ")) 
    caracter2 = int(input("nota 2 "))
    caracter3 = int(input("nota 3 "))
    caracter4 = int(input("nota 4 "))
    caracter5 = int(input("nota 5 "))
    caracter6 = int(input("nota 6 "))
    #suma
    total = ((caracter1) + (caracter2) + (caracter3) + (caracter4) + (caracter5) + (caracter6))
    print()
    #division
    print((total) / (6))

    print()
    pregunta = str(input("¿otra media? "))
    if pregunta == "si":
        print()
        print(".....................")
                    
    if pregunta == "no":
        break

#final
print()
print()
print("         by Sect_P5         ")
time.sleep (1)
