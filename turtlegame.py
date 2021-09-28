import turtle

#window

ablak = turtle.Screen()
ablak.setup(width=800, height=600)
ablak.bgcolor("black")
ablak.title("TurtlePong")

teknos = turtle.Turtle()
teknos.speed(1)
teknos.shape ("turtle")
teknos.color ("green")
teknos.shapesize (stretch_wid=5, stretch_len=5)
teknos.penup()

teknos.forward (200)
teknos.right (90)
teknos.forward (200)
teknos.right (90)
teknos.forward (200)
teknos.right (90)
teknos.forward (200)
teknos.right (90)