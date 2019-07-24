import turtle
import time
# crea el bichito
alex = turtle.Turtle()

#mueve el bichito
alex.up ()
alex.left (180)
alex.forward (90)
alex.left (90)


alex.down ()
for x in range(32):
    alex.forward(20)
    alex.left(11.25)

alex.up ()

alex.forward(123)

time.sleep(3)
