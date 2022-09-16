import turtle as trt
import random as r
size = 31
lanes = 5
center_error = 11
lanes_up = {}
for i in range(lanes):
    lanes_up[i] = []
class car:
    def __init__(self, lane, up, speed):
        self.car = trt.Turtle()
        self.car.penup()
        self.car.shape('car')
        self.car.color('red')
        self.lane = lane
        self.speed = speed
        self.car.speed(0)
        self.car.seth(180*up)
        self.car.setpos(r.randint(-1000,1000),(up*2-1)*(lane*size*1.5 + size*.75) - center_error)
        if up:
            lanes_up[lane].append(self)
            self.cars = lanes_up[lane]

    def find_closest_dist(self):
        min = 1000000
        c = self
        for car in self.cars:
            if car.car.xcor() > self.car.xcor() and car.car.xcor() - self.car.xcor() < min:
                min = car.car.xcor() - self.car.xcor()
                c = car
        if (min-size*2) < 0:
            min = size*2+.01
        return (c.speed - self.speed) - 100/((min-size*2)**2)

    def move(self):
        accl = ((20-self.speed)*.2 + self.find_closest_dist())
        self.speed += accl
        if self.speed < 0:
            self.speed = 0
        self.car.fd(self.speed)
        if self.car.xcor() > screen.canvwidth:
            self.car.goto(-screen.canvwidth, self.car.ycor())
        if self.car.xcor() < -screen.canvwidth:
            self.car.goto(screen.canvwidth, self.car.ycor())
        
screen = trt.getscreen()
trt.begin_poly()
trt.penup()
trt.speed(0)
trt.goto(-size/2,-size)
trt.pendown()
for i in range(2):
    trt.fd(size)
    trt.left(90)
    trt.fd(2*size)
    trt.left(90)
trt.home()
trt.end_poly()
rect = trt.get_poly()

trt.speed(0)

trt.screensize(1000,500)
trt.clearscreen()
screen.bgpic("road.gif")

    
screen.register_shape("car", rect)

cars = []
for j in range(lanes):
    for i in range(4):
        cars.append(car(j, True, r.randint(1,10)))

while True:
    for car in cars:
        car.move()
    trt.delay(10)
    
