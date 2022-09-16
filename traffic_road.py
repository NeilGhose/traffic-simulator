import turtle as trt
#from Tkinter import *
size = 10
lanes = 5

        
screen = trt.getscreen()

trt.speed(0)

trt.screensize(1000,500)

trt.clearscreen()
trt.bgcolor('gray')

trt.begin_fill()
trt.goto(screen.canvwidth, size*lanes*1.5)
trt.seth(180)
for i in range(2):
    trt.fd(screen.canvwidth*2)
    trt.left(90)
    trt.fd(size*lanes*3)
    trt.left(90)
trt.end_fill()

for lane in range(lanes):
    for i in range(int(screen.canvwidth/5)):
        trt.color('white')
        trt.fd(5)
        trt.color('black')
        trt.fd(5)
    
    func = (trt.left, trt.right)[lane%2]
    func(90)
    trt.fd(size*1.5)
    func(90)

trt.color('yellow')
trt.fd(screen.canvwidth*2)

for lane in range(lanes):
    func = (trt.left, trt.right)[func == trt.left]
    func(90)
    trt.fd(size*1.5)
    func(90)
    for i in range(int(screen.canvwidth/5)):
        trt.color('white')
        trt.fd(5)
        trt.color('black')
        trt.fd(5)

screen.getcanvas().postscript(file="road.eps")
