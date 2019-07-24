import turtle

cian = 0,1,1

x = 5
p= x*80
o= p/2


p = turtle.Turtle()
p.pensize(5)
p.speed(400)
p.color("green")

p.left(180)
p.forward(o)
p.left(180)

for ñ in range(x):
    p.color(cian)
    
    #cabeza
    for i in range(90):
        p.forward(2)
        p.left(4)

    #cuerpo  
    p.left(-90)
    p.forward(100)
    p.left(180)
    p.forward(70)

    #brazos
    p.left(90)
    p.forward(40)
    p.left(180)
    p.forward(80)
    p.left(180)
    p.forward(40)

    #pirnas
    p.left(90)
    p.forward(70)
    p.left(50)
    p.forward(50)
    p.left(180)
    p.forward(50)
    p.left(80)
    p.forward(50)

    p.color("blue")
    p.left(140)
    p.forward(123)   #distancia repe
    p.left(90)
    p.forward(132) # altura repe
    p.left(-90)
