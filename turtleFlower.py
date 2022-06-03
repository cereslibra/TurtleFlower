'''
作者：咕小头
代码中的主要函数逻辑是flower，功能是绘制繁花曲线
输入的参数依次为
R：大圆半径
r:小圆半径
dis:画笔在小圆中距离边缘的距离
w:画图精度（推荐0.02以下，可缺省）
color:画笔颜色（默认红色，可缺省）
size:画笔尺寸（默认为1像素，可缺省）

新增函数逻辑rainbowflower，功能是用渐变色的画笔绘制繁花曲线
输入的参数依次为
R：大圆半径
r:小圆半径
dis:画笔在小圆中距离边缘的距离
w:画图精度（推荐0.02以下，可缺省）
times:颜色渐变的速度（默认为1，可缺省）
size:画笔尺寸（默认为1像素，可缺省）
'''

import turtle
import math
import colorsys

pie = math.pi
turtle.colormode(1.0)  #设置颜色计量方式

def lcm(a,b):
    for i in range(min(a,b),0,-1):
        if a % i == 0 and b % i == 0:
            return math.ceil(a*b/i)

def flower(R,r,dis,w=0.02,color='red',size=1):
    turtle.color(color)
    turtle.pensize(size)
    turtle.penup()
    T = math.ceil(lcm(R,r)/w/R)
    M = R-r
    m = r-dis
    for t in range(T+1):
        x = M*math.cos(2*pie*w*t)-m*math.cos(2*pie*w*t*R/r)
        y = M*math.sin(2*pie*w*t)+m*math.sin(2*pie*w*t*R/r)
        turtle.goto(x, y)
        turtle.pendown()

def rainbow_flower(R,r,dis,w=0.02,size=1,times= 1):
    turtle.pensize(size)
    turtle.penup()
    T = math.ceil(lcm(R,r)/w/R)
    M = R-r
    m = r-dis
    for t in range(T+1):
        x = M*math.cos(2*pie*w*t)-m*math.cos(2*pie*w*t*R/r)
        y = M*math.sin(2*pie*w*t)+m*math.sin(2*pie*w*t*R/r)
        turtle.goto(x, y)
        color_R, color_G, color_B = colorsys.hsv_to_rgb(times*t/T,1.0,1.0)
        turtle.color((color_R, color_G, color_B))
        turtle.pendown()
# flower(200,110,20,color="#154279",size=3)
# flower(200,130,110,0.01,'red',1)
# flower(140,85,5,0.01,'blue',1)
rainbow_flower(200,110,20,size=3,times=60)
# 保存图片
img = turtle.getscreen()
img.getcanvas().postscript(file='012.eps')