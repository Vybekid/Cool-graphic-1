from turtle import *
import colorsys

bgcolor("black") 
tracer(5)

h = 0

for i in range(200):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    h += 0.008
    
    pencolor('black') 
    fillcolor(c)
    
    begin_fill()
    
    forward(i)
    right(68)
    forward(i)
    right(30)
    circle(i, 50)
    forward(i)
    right(289)
    
    end_fill()
    
    forward(i)
    left(90)
    forward(i)
    left(20)
    forward(i)
    left(80)

done()