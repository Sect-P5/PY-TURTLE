i = 1
import time
while i <= 1000:
    veces = int(input("¿Cuantas veces quiere que ponga un punto? "))
    for x in range(veces):
        print(".")
        time.sleep(0.03)
