import turtle
import time
# crea el bichito
alex = turtle.Turtle()

#mueve el bichito


for x in range(3):
    alex.forward(120)
    alex.left(120)

alex.up()
alex.left(90)
alex.forward(60)
alex.down()

alex.left(-90)
alex.forward(120)

for x in range(2):
    alex.left(-120)
    alex.forward(120)

time.sleep(3)
