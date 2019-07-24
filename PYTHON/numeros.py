import time
ñ= str(input("¿quieres numeros seguidos? "))

#SI
if str.lower(ñ) == "si":
    print("="*20)
    x=1
    c=1
    while c <= 1:
        p= int(input("numeros en bucle "))
        for i in range(p):
            print(x)
            x=x+1
            time.sleep(0.06)
        print("="*20)

#NO
else:
    print("="*20)
    c=1
    while c <= 1:
        x=1
        p= int(input("numeros en bucle "))
        for i in range(p):
            print(x)
            x=x+1
            time.sleep(0.06)
        print("="*20)
