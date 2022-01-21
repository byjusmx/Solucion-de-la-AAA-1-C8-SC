import turtle

wn = turtle.Screen()
wn.bgcolor("light green")

turtle.color("blue")

def sqrfunc(size,speed):
    for i in range(4):
        size,speed = size+5,speed+5
        turtle.speed(speed)
        turtle.fd(size)
        turtle.left(90)

sqrfunc(6,2)
sqrfunc(26,5)
sqrfunc(46,7)
sqrfunc(66,10)
sqrfunc(86,15)
sqrfunc(106,20)
sqrfunc(126,25)
sqrfunc(146,30)
