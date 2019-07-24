import time
y = 1
while y <= 100:
    caracter_1 = int(input("¿caracter 1? "))
    caracter_2 = int(input("¿caracter 2? "))
    print()
    print(caracter_1 - caracter_2)

    pregunta = str(input("¿otra resta? "))
    if pregunta == "si":
        print()
        print(".....................")
                    
    if pregunta == "no":
        break
