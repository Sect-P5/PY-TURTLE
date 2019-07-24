import turtle
import time

# crea el bichito
alex = turtle.Turtle()
pablo = turtle.Turtle()

#mueve el bichito
alex.left(-180)
pablo.left(144)

for x in range(5):
    pablo.forward(100)
    pablo.left(72)
    alex.forward(160)
    alex.left(144)


alex.up()
pablo.up()
pablo.forward(500)
alex.forward(500)

time.sleep(3)
