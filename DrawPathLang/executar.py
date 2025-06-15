import turtle
from comandos import IniciarEm, LinhaPara, CurvaPara, CirculoEm

def executar(comandos):
    turtle.title("DrawPathLang")
    turtle.speed(1)
    turtle.penup()

    for cmd in comandos:
        if isinstance(cmd, IniciarEm):
            turtle.penup()
            turtle.goto(cmd.x, cmd.y)
            turtle.pendown()
        elif isinstance(cmd, LinhaPara):
            turtle.goto(cmd.x, cmd.y)
        elif isinstance(cmd, CurvaPara):
            turtle.goto(cmd.x, cmd.y)
            turtle.circle(cmd.r, 90)
        elif isinstance(cmd, CirculoEm):
            turtle.penup()
            turtle.goto(cmd.x, cmd.y - cmd.r)
            turtle.pendown()
            turtle.circle(cmd.r)

    try:
        turtle.done()
    except turtle.Terminator:
        pass