import turtle

#window

ablak = turtle.Screen()
ablak.setup(width=800, height=600)
ablak.bgcolor("black")
ablak.title("TurtlePong")
ablak.tracer(0)

# left turtle

left_turtle = turtle.Turtle()
left_turtle.speed(0)
left_turtle.shape("turtle")
left_turtle.shapesize(stretch_wid=5, stretch_len=5)
left_turtle.color("green")
left_turtle.penup()
left_turtle.goto(-350,0)

# right turtle

right_turtle = turtle.Turtle()
right_turtle.speed(0)
right_turtle.shape("turtle")
right_turtle.shapesize(stretch_wid=5, stretch_len=5)
right_turtle.color("green")
right_turtle.penup()
right_turtle.goto(350,0)
right_turtle.tilt(180)

# labda

labda= turtle.Turtle()
labda.speed(0)
labda.shape("circle")
labda.penup()
labda.color("yellow")
labda.goto(0,0)


while True:
    ablak.update()