'''
Pelumi Tayo-Orisadare
pelumi.tayoorisadare@gmail.com
12.01.2021
'''

import turtle
import random
import time


#creating the game window for the snake game
window = turtle.Screen()
window.title('Snake Game by Pelumi Tayo-Orisadare')
window.bgcolor('green')
width, height = 450, 450
window.setup(width, height)
window.tracer(0)

#score of the game being played
current_score = 0
high_score = 0
delay = 0.1

#creating the head of the turtle body, the main character
#the one that eats the food.

turt = turtle.Turtle()
turt.shape('turtle')
turt.color('blue')
turt.penup()
turt.goto(50,0)
turt.direction = 'Stop'

#food for the turtle in game
food = turtle.Turtle()
food.shape('circle')
food.color('red')
food.speed(0)
food.shapesize(.60,.60,1)
food.penup()
food.goto(150,0)

#creates the heading pen for the game 
heading = turtle.Turtle()
heading.speed(0)
heading.color('white')
heading.penup()
heading.hideturtle()
heading.goto(0,190)
heading.write('Score : 0 High Score : 0', align = 'center', font = ('Arial', 25, 'bold'))

def game_score():
    '''
    shows the current and high score of the player at the top of the screen and
    changes the score as the player eats the food.
    '''
    heading.clear()
    heading.write('Score : {} High Score : {} '.format(current_score, high_score), \
              align = 'center', font = ('Arial', 25, 'bold'))



def up():
    '''
    moves the snake up
    '''
    if turt.direction != "down":
        turt.direction = "up"
 
 
def down():
    '''
    moves the turtle down
    '''
    
    if turt.direction != "up":
        turt.direction = "down"
 
 
def left():
    '''
    moves the turtle left
    '''
    if turt.direction != "right":
        turt.direction = "left"
 
 
def right():
    '''
    move the turtle right
    '''
    if turt.direction != "left":
        turt.direction = "right"
 
 
def snake_movements():
    '''
    moves the snake in the player's desired direction.
    '''
    if turt.direction == "up":
        y = turt.ycor()
        turt.sety(y+20)
    if turt.direction == "down":
        y = turt.ycor()
        turt.sety(y-20)
    if turt.direction == "left":
        x = turt.xcor()
        turt.setx(x-20)
    if turt.direction == "right":
        x = turt.xcor()
        turt.setx(x+20)

#correlates keys on the keyboard to the movements of the turtle   
window.listen()
window.onkeypress(up, 'Up')
window.onkeypress(down, 'Down')
window.onkeypress(left, 'Left')
window.onkeypress(right, 'Right')
window.onkeypress(up, 'w')
window.onkeypress(down, 's')
window.onkeypress(left, 'a')
window.onkeypress(right, 'd')

def game_over():
    '''
    Action that takes place after the game ends. Prints out game over and resets the map. 
    '''
    time.sleep(1)
    turt.goto(0,0)
    turt.hideturtle()
    turt.pendown()
    turt.write('Game Over.', align = 'center', font = ('Arial', 25, 'bold'))
    time.sleep(2)
    turt.clear()
    turt.showturtle()
    turt.penup()
    turt.direction = 'Stop'
    return True

def food_placement():
    '''
    randomizes the placement of the food on the map
    '''
    x = random.randint(-220, 210)
    y = random.randint(-210, 185)
    food.goto(x, y)


body = []
game = True
while game:
    window.update()
    if turt.xcor() > 210 or turt.xcor() < -220 or turt.ycor() > 185 or turt.ycor() < -210: #boundaries of the map
        game_over()
        food.goto(150,0)
        for i in body:
            i.goto(478, 478)
        body.clear()
        current_score = 0
        delay = 0.1
        game_score()
    #randomizes the food placement
    if turt.distance(food) < 20:
        food_placement()
        # Adding an extra body to the snake as it eats.
        new_turt = turtle.Turtle()
        new_turt.speed(0)
        new_turt.shape("turtle")
        new_turt.color("blue")  
        new_turt.penup()
        body.append(new_turt)
        delay = delay - 0.001
        current_score += 1
        if current_score > high_score:
            high_score = current_score
        game_score()
    # Checking for head collisions with body segments
    for index in range(len(body)-1, 0, -1):
        x = body[index-1].xcor()
        y = body[index-1].ycor()
        body[index].goto(x, y)
    if len(body) > 0:
        x = turt.xcor()
        y = turt.ycor()
        body[0].goto(x, y)
    snake_movements()
    for i in body:
        if i.distance(turt) < 20:
            time.sleep(1)
            turt.goto(0, 0)
            turt.direction = "stop"
            food.goto(150,0)
            game_over() #calls game_over function and relays to the player that they have lost the game.
            for i in body:
                i.goto(478, 478)
            body.clear()
            current_score = 0
            delay = 0.1
            game_score()
    time.sleep(delay)
game = False

window.mainloop()




