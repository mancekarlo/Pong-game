#PONG GAME

import turtle

wn = turtle.Screen()
wn.title ("Pong game")
wn.bgcolor("red")
wn.setup(width=800, height=600)
wn.tracer(0)

#igrač 1
igrac_1 = turtle.Turtle()
igrac_1.speed(0)
igrac_1.shape("square")
igrac_1.color("white")
igrac_1.shapesize(stretch_wid=5, stretch_len=1)
igrac_1.penup()
igrac_1.goto(-350,0)

#igrač 2
igrac_2 = turtle.Turtle()
igrac_2.speed(0)
igrac_2.shape("square")
igrac_2.color("white")
igrac_2.shapesize(stretch_wid=5, stretch_len=1)
igrac_2.penup()
igrac_2.goto(350,0)

#lopta
lopta = turtle.Turtle()
lopta.speed(0)
lopta.shape("square")
lopta.color("white")
lopta.penup()
lopta.goto(0,0)

#igrač 1 funkcije
def igrac_1_gore():
    y = igrac_1.ycor()
    y += 20
    igrac_1.sety(y)

def igrac_1_dole():
    y = igrac_1.ycor()
    y -= 20
    igrac_1.sety(y)

#igrač 2 funkcije
def igrac_2_gore():
    y = igrac_2.ycor()
    y += 20
    igrac_2.sety(y)

def igrac_2_dole():
    y = igrac_2.ycor()
    y -= 20
    igrac_2.sety(y)    

    
wn.listen()
wn.onkeypress(igrac_1_gore,"w")
wn.onkeypress(igrac_1_dole,"s")
wn.onkeypress(igrac_2_gore,"Up")
wn.onkeypress(igrac_2_dole,"Down")

while True:
    wn.update()






















