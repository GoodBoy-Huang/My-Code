import time
import turtle

turtle.pensize(2)
turtle.bgcolor("black")
colors=["red","purple","white","blue","green","orange"]
turtle.speed("fastest")

for x in range(300):
    turtle.forward(2*x)
    turtle.left(60)
    turtle.color(colors[x%6])

time.sleep(100)
