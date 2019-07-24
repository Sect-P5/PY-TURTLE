import time

columna = int(input("¿cuantas columnas quieres alineadas? "))
for c in range(columna):
    c = c+1
    print("*" * c)



columna_2 = int(input("¿cuantas columnas quieres alineadas invertidas? "))
for c in range(columna_2):
    print("*"*columna_2)
    columna_2 = columna_2 - 1



columna_3 = int(input("¿cuantas columnas quieres alineadas a la derecha? "))
for c in range(columna_3):
    c = c+1
    print(" "*(79-c) + c*"*")



columna_4 = int(input("¿cuantas columnas quieres alineadas invertidas a la derecha? "))
for c in range(columna_4):
    c = c+1
    print(" "*(79-columna_4) + "*"*columna_4)
    columna_4 = columna_4 - 1
time.sleep(1)
