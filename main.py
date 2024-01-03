import turtle
import random
import time

home_screen = turtle.Screen()
home_screen.bgpic("background_stewie_room.png")
home_screen.title("Catch Stewie")
score = 0
stewie_list = []
score_turtle = turtle.Turtle()
countdown_timer = turtle.Turtle()
game_over = False
def setup_score_turtle():

    score_turtle.hideturtle()
    score_turtle.color("red")
    score_turtle.penup()

    score_turtle.setposition(0,320)
    score_turtle.write("Score: 0",move=False, align="center",font=("Arial",25,"normal"))

grid_size = 15
def make_stewie(x,y):

    def on_click(x,y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write("Score: {}".format(score),move=False, align="center",font=("Arial",25,"normal"))


    little_stewie = "Adsız.gif"
    turtle.register_shape(little_stewie)
    stewie = turtle.Turtle()
    stewie.shape(little_stewie)
    stewie.penup()
    stewie.goto(x * grid_size, y * grid_size)
    stewie_list.append(stewie)
    stewie.onclick(on_click)



x_cordinates = [-20,-10,0,7,18]
y_cordinates = [-5,16,-10,-18]

def setup_stewie_co():
    for x in x_cordinates:
        for y in y_cordinates:
            make_stewie(x,y)

def hide_stewie():
    for stewie in stewie_list:
        stewie.hideturtle()

def random_show_stewie():
    if not game_over:
        hide_stewie()
        random.choice(stewie_list).showturtle()
        home_screen.ontimer(random_show_stewie,500)

def countdown(time):
    global game_over
    countdown_timer.hideturtle()
    countdown_timer.color("DarkBlue")
    countdown_timer.penup()

    countdown_timer.setposition(0, 350)

    if time > 0 :
        countdown_timer.clear()
        countdown_timer.write("Time left: {}".format(time), move=False, align="center", font=("Arial", 30, "normal"))
        home_screen.ontimer(lambda: countdown(time - 1),1000)
    else:
        game_over = True
        countdown_timer.clear()
        hide_stewie()
        countdown_timer.write("Game Over!", move=False, align="center", font=("Arial", 30, "normal"))


turtle.tracer(0)
time.sleep(1)
setup_score_turtle()
setup_stewie_co()
hide_stewie()
random_show_stewie()
countdown(15)
turtle.tracer(1)
turtle.mainloop()
turtle.done()