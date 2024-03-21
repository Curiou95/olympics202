import turtle

tr = turtle.Turtle()
tr.pensize(5)


def blue():
    list1 = [
        tr.color("blue"),
        tr.penup(),
        tr.goto(-110,-25),
        tr.pendown(),
        tr.circle(45)
    ]
    return list1

blue2 = blue()



def black():
    list1 = [
        tr.color("black"),
        tr.penup(),
        tr.goto(0,-25),
        tr.pendown(),
        tr.circle(45)
    ]
    return list1

black2 = black()

def red():
    list1 = [
        tr.color("red"),
        tr.penup(),
        tr.goto(110,-25),
        tr.pendown(),
        tr.circle(45)
    ]
    return list1
red2 = red()

def yellow():
    list1 = [
        tr.color("yellow"),
        tr.penup(),
        tr.goto(-55,-75),
        tr.pendown(),
        tr.circle(45)
    ]
    return list1
yellow2 = yellow()

def green():
    list1 = [
        tr.color("green"),
        tr.penup(),
        tr.goto(55,-75),
        tr.pendown(),
        tr.circle(45)
    ]
    return list1
green2 =green()


# final function

def olympic_logo(colors):
    colors = [blue2, black2, red2, yellow2,green2]
    for i in colors:
        return i
    

print(olympic_logo())
