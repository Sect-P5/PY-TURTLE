import turtle
import time
# crea el bichito
alex = turtle.Turtle()

#mueve el bichito


for x in range(4):
    alex.forward(200) 
    alex.left(90)

alex.left(-150)
alex.forward(100)
alex.left(150)
alex.forward(200) 

for x in range(4):
    alex.left(90)
    alex.forward(200)


alex.left(30)
alex.forward(100)

alex.left(60)
alex.forward(200)

alex.left(120)
alex.forward(100)

alex.left(-30)
alex.forward(200)

alex.left(-150)
alex.forward(100)
alex.up()

alex.forward(200)

time.sleep(3)
