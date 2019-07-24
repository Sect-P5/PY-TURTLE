import time
x = input(str("desea saber la hora "))

if x == "si":
    print(time.strftime("%H:%M:%S"))
    time.sleep(1)
else:
    print("para que coño me abres")
    time.sleep(2)
