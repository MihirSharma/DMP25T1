import turtle

turtle_obj = turtle.Turtle()

turtle_obj.fillcolor("green")
turtle_obj.begin_fill()
for _ in range(8):
    turtle_obj.forward(100)
    turtle_obj.right(45)

turtle_obj.end_fill()

turtle_obj.right(70)
turtle_obj.forward(150)

turtle_obj.color("white")
turtle_obj.write("GO", align="center", font=("Arial", 48, "bold"))

turtle.done()