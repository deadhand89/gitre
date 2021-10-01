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
left_turtle.color("red")
left_turtle.penup()
left_turtle.goto(-350,0)

# right turtle

right_turtle = turtle.Turtle()
right_turtle.speed(0)
right_turtle.shape("turtle")
right_turtle.shapesize(stretch_wid=5, stretch_len=5)
right_turtle.color("blue")
right_turtle.penup()
right_turtle.goto(350,0)
right_turtle.tilt(180)

# ball

labda= turtle.Turtle()
labda.speed(0)
labda.shape("circle")
labda.penup()
labda.color("yellow")
labda.goto(0,0)
labda.dx = 0.1
labda.dy = -0.1

# points

right_points = 0
left_points = 0

points = turtle.Turtle()
points.speed(0)
points.color("yellow")
points.penup()
points.hideturtle()
points.goto(0,260)
points.write(f"Right player: {right_points} Left player: {left_points}", align="center", font=("Curier", 24, "normal"))

#turtle movement

def left_turtle_up():
    y = left_turtle.ycor()
    y= y+30
    left_turtle.sety(y)

def left_turtle_down():
    y = left_turtle.ycor()
    y= y-30
    left_turtle.sety(y)

def right_turtle_up():
    y = right_turtle.ycor()
    y= y+30
    right_turtle.sety(y)

def right_turtle_down():
    y = right_turtle.ycor()
    y= y-30
    right_turtle.sety(y)

ablak.onkey(left_turtle_up, "w")
ablak.onkey(left_turtle_down, "s")

ablak.onkey(right_turtle_up, "Up")
ablak.onkey(right_turtle_down, "Down")

ablak.listen()


while True:
    ablak.update()

    labda.setx(labda.xcor() + labda.dx)
    labda.sety(labda.ycor() + labda.dy)

    # bounce
    if labda.ycor() > 288:
        labda.sety(288)
        labda.dy *= -1
    
    if labda.ycor() < -288:
        labda.sety(-288)
        labda.dy *= -1

    # right side
    if labda.xcor() > 388:
        labda.goto(0,0)
        labda.dx *= -1
        left_points +=1
        points.clear()
        points.write(f"Right player: {right_points} Left player: {left_points}", align="center", font=("Curier", 24, "normal"))



    # left side
    if labda.xcor() < -388:
        labda.goto(0,0)
        labda.dx *= -1
        right_points += 1
        points.clear()
        points.write(f"Right player: {right_points} Left player: {left_points}", align="center", font=("Curier", 24, "normal"))


    #paddle touch
    if right_turtle.xcor()-20 < labda.xcor() < right_turtle.xcor() and right_turtle.ycor()-40 < labda.ycor() < right_turtle.ycor() + 40:
        labda.setx(right_turtle.xcor()-20)
        labda.dx *= -1
    if left_turtle.xcor()+20 > labda.xcor() > left_turtle.xcor() and left_turtle.ycor()-40 < labda.ycor() < left_turtle.ycor() + 40:
        labda.setx(left_turtle.xcor()+20)
        labda.dx *= -1