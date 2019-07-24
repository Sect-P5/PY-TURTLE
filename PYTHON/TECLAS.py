import sys

x=1
A= 0
B= 0
C= 0
D= 0

while x ==1:
    tecla = sys.stdin.read(1)
    #TECLA W
    if tecla=="w":
        A = A+1
        print(A)
    else:
        #TECLA A
        if tecla =="a":
            B = B+1
            print(B)
        else:
            #TECLA S
            if tecla=="s":
                C = C+1
                print(C)
            else:
                #TECLA D
                if tecla =="d":
                    D = D+1
                    print(D)
