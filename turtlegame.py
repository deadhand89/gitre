import turtle

#window

ablak = turtle.Screen()
ablak.setup(width=800, height=600)
ablak.bgcolor("black")
ablak.title("TurtlePong")

# left turtle

left_turtle = turtle.Turtle()
left_turtle.speed(0)
left_turtle.shape("turtle")
left_turtle.shapesize(stretch_width=5, stretch_height=5)
left_turtle.color("green")
left_turtle.penup()
left_turtle.goto(-350,0)

while True:
    pass