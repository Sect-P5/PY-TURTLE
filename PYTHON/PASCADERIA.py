import sys
import time

print("pulse A para tiket de pescaderia")
time.sleep(0.05)
print("pulse Ñ para tiket de carniceria")
time.sleep(0.05)
print("pulse H para sumar 1 al contador de la pescaderia")
time.sleep(0.05)
print("PULSE J para sumar 1 al contador de la carniceria")
print("para parar el programa pulse P")
time.sleep(4)


x='si'
A= 0
B= 0
C= 0 #NUMERO
D= 0

print("===========")
print("CARNICERIA")
print(0)
print("===========")
print()
print()
print("===========")
print("PESCADERIA")
print(0)
print("===========")


while x =='si':
    print()
    print()
    tecla = sys.stdin.read(1)
    #TECLA Ñ
    if tecla=="ñ":
            A = A+1
            print("===========")
            print("TIKET CARNICERIA")
            print(A)
            print("===========")
    else:
        #TECLA A
        if tecla =="a":
            B = B+1
            print("===========")
            print("TIKET PESCADERIA")
            print(B)
            print("===========")
        else:
            #TECLA H
            if tecla=="h":
                C = C+1
                print("=========================")
                print("CONTADOR DE LA PESCADERIA")
                print(C)
                print("QUEDAN POR ATENDER")
                y= B-C
                if y > 0:
                    y= B-C
                    print(y)
                else:
                    print("0")
                print("=========================")
            else:
                #TECLA J
                if tecla=="j":
                    D = D+1
                    print("=========================")
                    print("CONTADOR DE LA CARNICERIA")
                    print(D)
                    print("QUEDAN POR ATENDER")
                    y= A-D
                    if y > 0:
                        p= A-D
                        print(p)
                    else:
                        print("0")
                    print("=========================")
                else:
                    if tecla =="p":
                        break




