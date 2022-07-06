import turtle

n= 20 # number of iteractions
s = 10 # scaling the drawing

# constant 
ang = 90 # degrees

# turtle setup
window = turtle.Screen()
window.setup(1000,800)
# turtle object instance
t = turtle.Turtle()

# drawing funtion
def spiral_squares(dist, ang, t):
    # squares
    t.left(ang)
    t.pensize(1)
    t.pencolor('lightgray')
    for i in range(4):  
        t.forward(dist)
        t.right(ang)
    # spiral arcs
    t.right(ang)
    t.pensize(2)
    t.pencolor("black")
    t.circle(dist, ang)

# sequence loop  
for i in range(n):
    if  i == 0: # starting the sequence 
        a, b = 0, 1
        print('{}\n{}'.format(a,b))
    else: # updating the sequence
        a, b = b, a+b
        print('{}\t\t\t r = {}/{} = {}'.format(b, b,a, b/a))
    # drawing the spiral
    spiral_squares(b * s, ang, t)

window.exitonclick()