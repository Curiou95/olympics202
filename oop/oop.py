import turtle

tr = turtle.Turtle()
tr.pensize(5)



# defined functions for all the five colors
def blue():
    list1 = [
        tr.color("blue"),
        tr.penup(),
        tr.goto(-110,-25),
        tr.pendown(),
        tr.circle(45)
    ]
    return list1

def black():
    list2 = [
        tr.color("black"),
        tr.penup(),
        tr.goto(0,-25),
        tr.pendown(),
        tr.circle(45)
    ]
    return list2

def red():
    list3 = [
        tr.color("red"),
        tr.penup(),
        tr.goto(110,-25),
        tr.pendown(),
        tr.circle(45)
    ]
    return list3

def yellow():
    list4 = [
        tr.color("yellow"),
        tr.penup(),
        tr.goto(-55,-75),
        tr.pendown(),
        tr.circle(45)
    ]
    return list4

def green():
    list5 = [
        tr.color("green"),
        tr.penup(),
        tr.goto(55,-75),
        tr.pendown(),
        tr.circle(45)
    ]
    return list5

# assigned all the functions to new variables and created a list of colors 
blue2 = blue()
black2 = black()
red2 = red()
yellow2 = yellow()
green2 =green()


# final function
colors = [blue2, black2, red2, yellow2,green2]

# here I iterated over the list of colors and returned the logo
def olympic_logo(colors):
    for i in colors:
        return i
    

print(olympic_logo(colors))
