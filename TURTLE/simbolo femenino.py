import turtle

p = turtle.Turtle()
p.color("pink")
p.pensize(5)
p.speed(100)  #de 0 a 100

#############################

#cabeza
for i in range(90):
    p.forward(2)
    p.left(4)

#cuerpo
p.left(-90)
p.forward(100)
p.left(180)
p.forward(60)

#brazos
p.left(90)
p.forward(40)
p.left(180)
p.forward(80)
