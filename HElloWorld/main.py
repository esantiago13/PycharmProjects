import turtle

b = "Hello"
print(b)

a = 5
print(a)

ed_turtle = turtle.Turtle()
ed_turtle2 = turtle.Turtle()


def square():
    ed_turtle.forward(100)
    ed_turtle.right(90)
    ed_turtle.forward(100)
    ed_turtle.right(90)
    ed_turtle.forward(100)
    ed_turtle.right(90)
    ed_turtle.forward(100)

    ed_turtle2.forward(100)
    ed_turtle2.left(90)
    ed_turtle2.forward(100)
    ed_turtle2.left(90)
    ed_turtle2.forward(100)
    ed_turtle2.left(90)
    ed_turtle2.forward(100)


square()
ed_turtle.forward(400)
ed_turtle2.forward(400)
ed_turtle.left(300)
ed_turtle.back(200)
