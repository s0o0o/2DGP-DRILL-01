import turtle

turtle.reset()
turtle.shape('turtle')

def moveW():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def moveA():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def moveS():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()

def moveD():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def restart():
    turtle.reset()

turtle.listen()
turtle.onkey(moveW,'w')
turtle.onkey(moveA,'a')
turtle.onkey(moveS,'s')
turtle.onkey(moveD,'d')
turtle.onkey(restart,'Escape')
