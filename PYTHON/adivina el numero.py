import random
import time
print("------- ADIVINA EL UN NUMERO ALEATORIO ENTRE EL 1 Y EL 20 -------")
time.sleep (1)
c = 1
while c <= 1:
    print()
    numero_random = random.randint(1, 20)
    for i in range(5):
        y = int(input("¿que numero? "))
        
        if y < numero_random and i < 4:
            print("más alto")
            time.sleep (1)
                                
        if y < 0:
            print("tonto del nabo que es de 1 a 20")
            time.sleep (1)
            
        if y > 20:
            print("tonto del nabo que es de 1 a 20")
            time.sleep (1)
            
        if y > numero_random and i < 4:
            print("más bajo")
            time.sleep (1)
               
        if y == numero_random:
            print("enhorabuena")
            break
                    
        if i == 3:
            print("ultima oportunidad")
            time.sleep (3)

    print()
    time.sleep (1.3)
    if y == numero_random:
        print("lo has adivinado en" + i + "intentos")
        time.sleep (1)

    if y != numero_random:
        print(numero_random)
        print("ese era el numero")
        time.sleep (1)
        
    print("...................")
        
