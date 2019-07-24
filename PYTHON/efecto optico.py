inicio = 1
y = 1
veces = 1
import time
print("----------------- BIENVENIDO A EL EFECTO OPTICO -----------------")
time.sleep (0.4)
#cuenta atras

while inicio <= 1:
    pregunta = str(input("¿empezamos? "))
    if pregunta == "si":
        print("3")
        time.sleep (1)
        print("2")
        time.sleep (1)
        print("1")
        time.sleep (1)
        print("go")
        time.sleep (1)
        break
                
    if pregunta == "no":
        print("tonto del nepe, entonces para que te metes")
        time.sleep (1)
        print("te lo pregunto otra vez")
        time.sleep (0.4)
        print()

#efecto optico
while y <= 1:
    print("ox            xo")
    time.sleep (0.2)
    for x in range(5):
        print()          
        print("  ox       xo   ")
        time.sleep (0.2)
        print()
        print("       o       ")
        time.sleep (0.2)
        print()
        print("  ox       xo   ")
        time.sleep (0.2)
        print()
        print("ox            xo")
        time.sleep (0.2)
        print()
    print("  ox       xo   ")
    time.sleep (0.2)
    print()
    print("       o       ")
    print()
    #impresión del user
    if veces < 2:
        input("¿Te gusto? ")
        print("procesando")
        for x in range(5):
            time.sleep (0.2)
            print(".")
            
    #repetición
    time.sleep (1)
    pregunta = str(input("¿otra vez? "))
    if pregunta == "si":
        print("ok")
        veces = veces + 1
        time.sleep (1)
            
    if pregunta == "no":
        break
#final
print()
print("----------------- GRACIAS POR PROBAR ESTE EFECTO OPTICO -----------------")
print()
print("                                by Sect_P5                               ")

time.sleep (3)

