import turtle


def tree(t: turtle.Turtle, branchLen: int):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(t, branchLen - 15)
        t.left(40)
        tree(t, branchLen - 15)
        t.right(20)
        t.backward(branchLen)


if __name__ == '__main__':
    t = turtle.Turtle()
    window = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")

    tree(t, 75)
    window.exitonclick()
