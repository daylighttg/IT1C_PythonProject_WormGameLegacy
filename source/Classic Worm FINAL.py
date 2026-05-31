# WORM Game - FINAL 
import turtle
import time
import random
import winsound  

# ----------------------
#  VARIABLE AREA
# ----------------------
delay = 0.1
score = 0
high_score = 0
game_running = True  
game_state = "play"  

# ----------------------
# SCREEN AREA
# ----------------------
wn = turtle.Screen()
wn.title("Classic Worm - Python Style")
wn.setup(width=600, height=600)
wn.tracer(0)

try:
   
    wn.bgpic("worm_bg.png") 
except:
    
    wn.bgcolor("lightgreen") 
    print("GAME IS NOW RUNNING")


def close_game():
    global game_running
    game_running = False
    wn.bye()

wn._root.protocol("WM_DELETE_WINDOW", close_game)

# ----------------------
# HEAD WORM AREA
# ----------------------
snake_head = turtle.Turtle()
snake_head.speed(0)
snake_head.shape("circle")            
snake_head.color("darkgreen")         
snake_head.shapesize(stretch_wid=1.3, stretch_len=1.3)  
snake_head.penup()
snake_head.goto(0, 0)
snake_head.direction = "stop"


snake_body = []

# ----------------------
# FOOD AREA
# ----------------------
food = turtle.Turtle()
food.speed(0)
food.shape("circle")           
food.color("red")             
food.shapesize(stretch_wid=1.0, stretch_len=1.0) 
food.penup()
food.goto(0, 100)

# ----------------------
# SCORE AREA
# ----------------------
pen_score = turtle.Turtle()
pen_score.speed(0)
pen_score.color("black")
pen_score.penup()
pen_score.hideturtle()
pen_score.goto(0, 260)


pen_message = turtle.Turtle()
pen_message.speed(0)
pen_message.color("red")
pen_message.penup()
pen_message.hideturtle()

# ----------------------
# function AREA
# ----------------------
def go_up():
    if snake_head.direction != "down" and game_state == "play":
        snake_head.direction = "up"

def go_down():
    if snake_head.direction != "up" and game_state == "play":
        snake_head.direction = "down"

def go_left():
    if snake_head.direction != "right" and game_state == "play":
        snake_head.direction = "left"

def go_right():
    if snake_head.direction != "left" and game_state == "play":
        snake_head.direction = "right"

def try_again():
    global score, delay, game_state
    if game_state == "game_over": 
        pen_message.clear()
        pen_score.clear()
        
        snake_head.goto(0, 0)
        snake_head.direction = "stop"
        
        for segment in snake_body:
            segment.goto(1000, 1000)
        snake_body.clear()
        
        score = 0
        delay = 0.1
        
        pen_score.write(f"Score: {score}  |  Highest: {high_score}", align="center", font=("Arial", 18, "bold"))
        game_state = "play"

def exit_game():
    global game_running
    pen_message.clear() 
    pen_message.goto(0, 0)
    pen_message.color("darkgreen") 
    pen_message.write("THANK YOU FOR PLAYING!!", align="center", font=("Arial", 22, "bold"))
    wn.update() 
    time.sleep(2) 
    game_running = False
    wn.bye()

def move():
    if not game_running or game_state != "play":
        return

    
    for index in range(len(snake_body)-1, 0, -1):
        x = snake_body[index-1].xcor()
        y = snake_body[index-1].ycor()
        snake_body[index].goto(x, y)

    
    if len(snake_body) > 0:
        x = snake_head.xcor()
        y = snake_head.ycor()
        snake_body[0].goto(x, y)

    
    if snake_head.direction == "up":
        y = snake_head.ycor()
        snake_head.sety(y + 20)

    if snake_head.direction == "down":
        y = snake_head.ycor()
        snake_head.sety(y - 20)

    if snake_head.direction == "left":
        x = snake_head.xcor()
        snake_head.setx(x - 20)

    if snake_head.direction == "right":
        x = snake_head.xcor()
        snake_head.setx(x + 20)

# ----------------------
# CONTROL AREA
# ----------------------
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")
wn.onkeypress(try_again, "r")    
wn.onkeypress(exit_game, "e")    

# ----------------------
# GAME LOOP AREA
# ----------------------
try:
    
    pen_score.write("Score: 0  |  Highest: 0", align="center", font=("Arial", 18, "bold"))

    while game_running:
        wn.update()

        
        if game_state == "play" and (abs(snake_head.xcor()) > 290 or abs(snake_head.ycor()) > 290):
            winsound.Beep(250, 300)
            game_state = "game_over"

            pen_message.goto(0, 50)
            pen_message.write("GAME OVER GG!!", align="center", font=("Arial", 40, "bold"))
            pen_message.goto(0, -20)
            pen_message.color("black")
            pen_message.write("Click [ R ] TRY AGAIN", align="center", font=("Arial", 16, "bold"))
            pen_message.goto(0, -50)
            pen_message.write("Click [ E ]  EXIT", align="center", font=("Arial", 16, "bold"))

        
        if game_state == "play" and snake_head.distance(food) < 20:
            winsound.Beep(700, 120)

            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x, y)

            
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("circle")            
            new_segment.color("limegreen")          
            new_segment.shapesize(stretch_wid=1.1, stretch_len=1.1)
            new_segment.penup()
            snake_body.append(new_segment)

            
            delay -= 0.001
            score += 10
            if score > high_score:
                high_score = score
            
            pen_score.clear()
            pen_score.write(f"Score: {score}  |  Highest: {high_score}", align="center", font=("Arial", 18, "bold"))

        
        for segment in snake_body:
            if game_state == "play" and segment.distance(snake_head) < 20:
                winsound.Beep(200, 400)
                game_state = "game_over"

                pen_message.goto(0, 50)
                pen_message.color("red")
                pen_message.write("GAME OVER GG!!", align="center", font=("Arial", 40, "bold"))
                pen_message.goto(0, -20)
                pen_message.color("black")
                pen_message.write("Click [ R ]  TRY AGAIN", align="center", font=("Arial", 16, "bold"))
                pen_message.goto(0, -50)
                pen_message.write("Click [ E ]  EXIT", align="center", font=("Arial", 16, "bold"))

        move()
        time.sleep(delay)

except turtle.Terminator:
    pass 
except Exception as e:
    if game_running:
        print("SAINT XII", e)