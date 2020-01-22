# Draw a spiral using Turtle
import turtle


def drawSpiral(t_handle, lineLen: int):
    if lineLen > 0:
        t_handle.forward(lineLen)
        t_handle.right(20)
        drawSpiral(t_handle, lineLen - 1)


if __name__ == '__main__':
    t = turtle.Turtle()
    window = turtle.Screen()
    drawSpiral(t, 40)
    window.exitonclick()
