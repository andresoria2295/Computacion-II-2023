#!/usr/bin/python3
import turtle
import colorsys

#Configuración inicial de Turtle.
turtle.speed(0)
turtle.bgcolor("black")
turtle.hideturtle()
turtle.title("Efecto visual sorprendente")

#Función para dibujar espiral colorida.
def draw_colorful_spiral():
    side = 10
    hue = 0

    for _ in range(600):
        turtle.pencolor(colorsys.hsv_to_rgb(hue, 1, 1))
        turtle.forward(side)
        turtle.right(91)
        side += 2
        hue += 0.01

#Gráfica de espiral.
draw_colorful_spiral()

#Cierre de ventana.
turtle.exitonclick()

