import turtle
import random
bg=turtle.Turtle()
bg= turtle.Screen()
bg.bgpic('3xel.gif')

lives=5
game= turtle.Screen()
game.title('Egg Drop')
game.bgcolor('green')
game.setup(width=700, height=100)
#game.tracer(0)
#adding basket
basket= turtle.Turtle()
basket.speed(0)
basket.shape('square')
basket.penup()
basket.goto(0,-200)
basket.direction='stop'
#falling eggs
eggs= turtle.Turtle()
eggs.speed(0)
eggs.shape('circle')
eggs.color('white')
eggs.penup()
eggs.goto(0,250)
eggs1= turtle.Turtle()
eggs1.speed(0)
eggs1.shape('circle')
eggs1.color('blue')
eggs1.penup()
eggs1.goto(-140,255)
eggs2= turtle.Turtle()
eggs2.speed(0)
eggs2.shape('circle')
eggs2.color('blue')
eggs2.penup()
eggs2.goto(180,245)

def go_left():
    basket.direction='left'
def go_right():
    basket.direction='right'
#keyboard binding
game.listen()
game.onkeypress(go_left,'Left')
game.onkeypress(go_right,'Right')

#main game loop
while True:
    #game.update()
    #move basket
    x=basket.xcor()
    if basket.direction=='left':
        x-=10
        basket.setx(x)
    elif x>390:
        basket.direction=('stop')    
    if basket.direction=='right':
        x+=10
        basket.setx(x)
    elif x<-390:
        basket.direction=('stop')
    
    
    #falling eggs
    y= eggs.ycor()
    y-=7
    eggs.sety(y)
    #check if off the screen
    if y<-300:
        x= random.randint(-380,380)
        y= random.randint(300,400)
        eggs.goto(x,y)
    # check for the collision with basket
    if eggs.distance(basket) < 40:
        x= random.randint(-380,380)
        y= random.randint(300,400)
        eggs.goto(x,y)
    if (eggs1.distance(basket) < 40):
        x= random.randint(-380,380)
        y= random.randint(300,400)
        eggs1.goto(x,y)
    if (eggs2.distance(basket) < 40):
        x= random.randint(-380,380)
        y= random.randint(300,400)
        eggs1.goto(x,y)
    lives=turtle.Turtle()
    style=('Courier',30,'italic')
    lives.write('lives',font=style,align='left')
    #falling eggs1
    y= eggs1.ycor()
    y-=7
    eggs1.sety(y)
    #check if off the screen
    if y<-300:
        x= random.randint(-380,380)
        y= random.randint(300,400)
        eggs1.goto(x,y)
    # check for the collision with basket
    if eggs1.distance(basket) < 40:
        x= random.randint(-380,380)
        y= random.randint(300,400)
        eggs1.goto(x,y)
    #falling eggs2
    y= eggs1.ycor()
    y-=7
    eggs2.sety(y)
    #check if off the screen
    if y<-300:
        x= random.randint(-380,380)
        y= random.randint(300,400)
        eggs2.goto(x,y)
    # check for the collision with basket
    if eggs2.distance(basket) < 40:
        x= random.randint(-380,380)
        y= random.randint(300,400)
        eggs2.goto(x,y)
    
game.mainloop()

