import turtle
import time

#create screen

sc = turtle.Screen()
sc.title("Ping Pong")
sc.bgcolor("black")
sc.cv._rootwindow.resizable(False,False)


#left player
left_pl = turtle.Turtle()
left_pl.shape("square")
left_pl.color("white")
left_pl.speed(0)
left_pl.penup()
left_pl.shapesize(stretch_wid=6,stretch_len=2)
left_pl.goto(-250,0)

#right player

right_pl=turtle.Turtle()
right_pl.shape("square")
right_pl.color("white")
right_pl.speed(0)
right_pl.penup()
right_pl.shapesize(stretch_wid=6,stretch_len=2)
right_pl.goto(250,0)

#ball
ball = turtle.Turtle()
ball.speed(3)
ball.shape("circle")
ball.color("red")
ball.goto(0,0)
ball.penup()
ball.dx=5
ball.dy=-5

player1=0
player2=0

#score
word = turtle.Turtle()
word.speed(0)
word.color("blue")
word.penup()
word.hideturtle()
word.goto(0,260)
word.write("Player_L : 0    Player_R : 0",align = "center" , font=("Ariel",24))


#motion

def playerL_up():
    y = left_pl.ycor()
    if y < 260:
        y+=20
        left_pl.sety(y)

def playerR_up():
    y = right_pl.ycor()
    if y < 260:
        y+=20
        right_pl.sety(y)

def playerL_down():
    y = left_pl.ycor()
    if y > -240:
        y-=20
        left_pl.sety(y)


def playerR_down():
    y = right_pl.ycor()
    if y > -240:
        y-=20
        right_pl.sety(y)

sc.listen()
sc.onkeypress(playerR_up, "Up")
sc.onkeypress(playerR_down, "Down")
sc.onkeypress(playerL_up,"w")
sc.onkeypress(playerL_down,"s")


while True:
    sc.update()
    time.sleep(0.01)
    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball .ycor() > 260:
        ball.sety(260)
        ball.dy*=-1
        
    if ball .ycor() < -260:
        ball.sety(-260)
        ball.dy*=-1

    if ball.xcor() > 450:
        ball.goto(0,0)
        player2 += 1
        word.clear()
        word.write(f"Player_L : {player2}    Player_R : {player1}",align = "center" , font=("Ariel",24))

    if ball .xcor() < -450:
        ball.goto(0,0)
        player1 += 1
        word.clear()
        word.write(f"Player_L : {player2}    Player_R : {player1}",align = "center" , font=("Ariel",24))

    
    if (ball.xcor()>250 and ball.xcor <260 ) and (ball.ycor() < right_pl.ycor()+50 and  ball.ycor() < right_pl.ycor()-50):
        ball.setx(250)
        ball.dx*=-1

    if (ball.xcor() < -250 and ball.xcor > -260 )and (ball.ycor() < left_pl.ycor()+50 and  ball.ycor() < left_pl.ycor()-50):
        ball.setx(-250)
        ball.dx*=-1
        

    
        
        

        
        
    
    
    





















