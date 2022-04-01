import turtle
import time
import random

speed=0.15

window=turtle.Screen()
window.title("Yılan Oyunu")
window.bgcolor("lightblue")
window.setup(width=600,height=600)
window.tracer(0)

head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.penup()
head.goto(0,100)
head.direction="stop"

eat=turtle.Turtle()
eat.speed(0)
eat.shape("circle")
eat.color("green")
eat.penup()
eat.goto(0,0)
eat.shapesize(0.95,0.95)


tails=[]
highScore=0

score=turtle.Turtle()
score.speed(0)
score.shape("square")
score.color("white")
score.penup()
score.goto(0,260)
score.hideturtle()
score.write("Score:{}".format(highScore),align="center",font=('Courier',24,'normal'))

def move():
    if head.direction == "up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction == "right":
        x=head.xcor()
        head.setx(x+20)
    if head.direction == "left":
        x=head.xcor()
        head.setx(x-20)

def goUp():
    if head.direction != "down":
        head.direction ="up"

def goDown():
    if head.direction!="up":
        head.direction="down"

def goRight():
    if head.direction!='left':
        head.direction='right'

def goLeft():
    if head.direction!='right':
        head.direction='left'

window.listen()
window.onkey(goUp,'Up')
window.onkey(goDown,'Down')
window.onkey(goRight,'Right')
window.onkey(goLeft,'Left')

while True:
    window.update()

    if head.xcor()>300 or head.xcor()<-300 or head.ycor()>300 or head.ycor()<-300:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"
        speed=0.15
        for tail in tails:
            tail.goto(1000,1000)
        tails.clear()
        highScore=0
        score.clear()
        score.write("Score:{}".format(highScore), align="center", font=('Courier', 24, 'normal'))

    if head.distance(eat)<15:
        x=random.randint(-250,250)
        y=random.randint(-250,250)
        eat.goto(x,y)
        highScore=highScore+10
        score.clear()
        score.write("Score:{}".format(highScore), align="center", font=('Courier', 24, 'normal'))
        speed=speed-0.01
        newTail=turtle.Turtle()
        newTail.speed(0)
        newTail.shape('square')
        newTail.color("brown")
        newTail.penup()
        tails.append(newTail)

    for i in range(len(tails)-1,0,-1):
        x=tails[i-1].xcor()
        y=tails[i-1].ycor()
        tails[i].goto(x,y)

    if len(tails)>0:
        x= head.xcor()
        y=head.ycor()
        tails[0].goto(x,y)

    move()
    time.sleep(speed)
