import time

#pregunta
pop = int(input("¿cunantos años tienes? "))

#procesando
print("procesando")
time.sleep (1)
for i in range(5):
    print(".")
    time.sleep (0.06)

#condicionales
if pop > 105:
    print("que pasa trolololo, aqui no te queremos")

if pop < 105:
    if pop > 18 or pop == 18:
        print("nice, eres mayor de 18 años")
    
if pop < 18:
    print("bye bye, aqui no queramos canijos")

time.sleep (4)
