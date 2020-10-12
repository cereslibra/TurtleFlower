import turtle
import math

pie = math.pi

def lcm(a,b):
    for i in range(min(a,b),0,-1):
        if a % i == 0 and b % i == 0:
            return math.ceil(a*b/i)

def flower(R,r,dis,w,color='red',size=1):
    turtle.color(color)
    turtle.pensize(size)
    turtle.penup()
    t = math.ceil(lcm(R,r)/w/R)
    M = R-r
    m = r-dis
    for t in range(t+1):
        x = M*math.cos(2*pie*w*t)-m*math.cos(2*pie*w*t*R/r)
        y = M*math.sin(2*pie*w*t)+m*math.sin(2*pie*w*t*R/r)
        turtle.goto(x,y)
        turtle.pendown()

flower(200,110,20,0.1,'#465829',1)
# flower(200,130,110,0.01,'red',1)
# flower(140,85,5,0.01,'blue',1)
img = turtle.getscreen()
img.getcanvas().postscript(file='007.eps')