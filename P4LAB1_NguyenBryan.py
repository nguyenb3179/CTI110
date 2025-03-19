# Bryan Nguyen  
# #03/19/2025
# P4LAB1
# Turtle graphics program to draw triangle and square.

import turtle
win = turtle.Screen()
t = turtle.Turtle()
win.bgcolor('black')

#Set the way the turle looks
t.pensize(6)
t.pencolor('yellow')
t.shape('turtle')

# Test
# t.forward(100)

# for loop that runs 4 times
for i in range(4):
    t.forward(100)
    t.right(90)

# while loop that runs 3 times
this_run = 0

while this_run < 3:
    t.forward(100)
    t.left(120)
    this_run += 1

            
    














# End command - keeps the window open after shape is drawn
win.mainloop()