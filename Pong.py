import turtle as t
import time
try:
    try:
        import tkinter as tk
        import tkinter.font

        root = tk.Tk()
        root.title("Menu")
        root.geometry("500x400")
        root.resizable(False, False)
        root.configure(bg="black")

        title_font =tk.font.Font(family="D2Coding", size=24, slant="roman")
        font =tk.font.Font(family="D2Coding", size=18, slant="roman")

        def game_start():
            root.destroy()

        tk.Label(root, text="", bg="black").pack()
        tk.Label(root, text="", bg="black").pack()
        tk.Label(root, text="", bg="black").pack()
        tk.Label(root, text="PING-PONG II", bg="black", fg='white', font=title_font).pack()
        tk.Label(root, text="", bg="black").pack()
        tk.Label(root, text="", bg="black").pack()
        tk.Label(root, text="", bg="black").pack()
        tk.Label(root, text="", bg="black").pack()
        tk.Button(root, text="Game Start", width=18, font=font, command=game_start).pack()
        tk.Label(root, text="", bg="black").pack()
        tk.Button(root, text="Exit", width=10, font=font, command=lambda:exit()).pack()

        root.mainloop()
    except:
        pass

    playing = True

    dx = 5
    dy = 5

    WIDTH = 800
    HEIGHT = 600

    score_A = 0
    score_B = 0

    screen = t.Screen()
    screen.title('PONG II')
    screen.bgcolor('black')
    screen.setup(WIDTH, HEIGHT)
    screen.tracer(0)


    #ball
    ball = t.Turtle()
    ball.penup()
    ball.speed(0)

    ball.color("red")
    ball.shape('circle')
    ball.shapesize(1)

    ball.goto(0, 0)

    #bar_A
    bar_A = t.Turtle()
    bar_A.penup()
    bar_A.speed(0)

    bar_A.color('white')
    bar_A.shape('square')
    bar_A.shapesize(7, 1)

    bar_A.goto(-WIDTH/2+50, 0)

    #bar_B
    bar_B = t.Turtle()
    bar_B.penup()
    bar_B.speed(0)

    bar_B.color('white')
    bar_B.shape('square')
    bar_B.shapesize(7, 1)

    bar_B.goto(WIDTH/2-50, 0)

    #score_writer
    score_writer = t.Turtle()
    score_writer.penup()
    score_writer.ht()
    score_writer.speed(0)

    def score_write():
        global score_A; global score_B
        score_writer.clear()

        score_writer.goto(0, HEIGHT/2-30)

        score_writer.color('white')
        score_writer.write('A: ' + str(score_A) + " "*5 + "B: " + str(score_B), False, 'center', ('', 12, 'bold'))
    score_write()

    #moving
    def up_A():
        y = bar_A.ycor()
        if y <= HEIGHT/2 - 100:
            bar_A.sety(y + 20)
    def down_A():
        y = bar_A.ycor()
        if y >= -HEIGHT/2 + 100:
            bar_A.sety(y - 20)

    def up_B():
        y = bar_B.ycor()
        if y <= HEIGHT/2 - 100:
            bar_B.sety(y + 20)
    def down_B():
        y = bar_B.ycor()
        if y >= -HEIGHT/2 + 100:
            bar_B.sety(y - 20)

    t.onkeypress(up_A, 'w')
    t.onkeypress(down_A, 's')
    t.onkeypress(up_B, 'Up')
    t.onkeypress(down_B, 'Down')
    t.listen()

    #gaming
    while playing:
        #ball_moving
        def ball_moving_distance():
            global dx; global dy
            nx = ball.xcor() + dx
            ny = ball.ycor() + dy
            ball.goto(nx, ny)
        
        def ball_clear():
            global dx; global dy
            dx = 5
            dy = 5
            ball.goto(0, 0)

        #U/D
        if ball.ycor() <= HEIGHT/2-15 and ball.ycor() >= -HEIGHT/2+15:
            ball_moving_distance()
        else:
            dy = -1 * dy
            ball_moving_distance()

        #LOSE
        if ball.xcor() >= WIDTH/2-15:
            score_A += 1
            score_write()
            ball_clear()
        elif ball.xcor() <= -WIDTH/2+15:
            score_B += 1
            score_write()
            ball_clear()

        #REFLACT
        if (bar_A.xcor() - 20 < ball.xcor() < bar_A.xcor() + 20) and\
            (bar_A.ycor()-70)< ball.ycor() < bar_A.ycor() + 70:
            dx = -1 * dx
            ball_moving_distance()
        elif (bar_B.xcor() - 20 < ball.xcor() < bar_B.xcor() + 20) and\
            (bar_B.ycor()-70)< ball.ycor() < bar_B.ycor() + 70:
            dx = -1 * dx
            ball_moving_distance()
        
        if dx < 0 :
            dx -= 0.01
        elif dx > 0:
            dx +=0.01
        dy += 0.01

        time.sleep(0.02)
        screen.update()


    t.mainloop()
except:
    pass