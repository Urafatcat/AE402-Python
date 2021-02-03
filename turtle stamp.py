import turtle
mark=turtle.Turtle()
turtle.color("blue")
mark.shape("turtle")
mark.penup()
for x in range(0,100,5):
    mark.forward(40+x)
    mark.left(40)
    mark.stamp()