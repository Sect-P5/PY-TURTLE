import turtle
import time


# crea el bichito
p = turtle.Turtle()

#definicion de colores
p.color("blue","pink")

#velocidad
p.speed(50)

#tamaño
p.pensize(3)

#codigo
p.begin_fill()
for i in range(9):

    p.left(40)
    for i in range(4):
        p.forward(120)
        p.left(120)

p.end_fill()


#luis.albert@robotschool.es
#cambiar extension a .txt
