from tkinter import * 

tk = Tk()
tk.title('Bouncing ball')
tk.resizable(False, False)

WIDTH, HEIGHT = 400, 300
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
canvas.pack()

ball = canvas.create_oval(10, 10, 50, 50, fill='black')
xspeed = yspeed = 5

def moveBall():

    global xspeed, yspeed

    canvas.move(ball, xspeed, yspeed)

    (leftPos, topPos, rightPos, bottomPos) = canvas.coords(ball)

    if leftPos <= 0 or rightPos >= WIDTH:
        xspeed = -xspeed
    if topPos <= 0 or bottomPos >= HEIGHT:
        yspeed = -yspeed

    canvas.after(30, moveBall)

canvas.after(30, moveBall)
tk.mainloop()
