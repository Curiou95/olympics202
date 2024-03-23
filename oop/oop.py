# Olympic logo
import turtle

tr = turtle.Turtle()
tr.pensize(5)


def draw(kolor, width, height):
    tr.color(kolor)
    tr.penup()
    tr.goto(width, height)
    tr.pendown()
    tr.circle(45)


draw("blue", -110, -25)
draw("black", 0, -25)
draw("red", 110, -25)
draw("yellow", -75, -55)
draw("green", 55, -75)


# input biodata
def Bio_data2(name,age,email,gender):
    name = input("Write your name: ")
    age = int(input("Write your age: "))
    email = input("Write your email: ")
    gender = input("Write your gender: ")
    return [name,age,email,gender]

Bio_data2('name','age','email','gender')



# calculate netpay
def netpay(paye,nssf,total_pay):
    paye = int(input("Paye: "))
    nssf = int(input("NSSF: "))
    total_pay = int(input("Total pay: "))
    paye1 = (paye/100)*total_pay
    nssf1 = ((nssf/100)*total_pay)
    total_taxes = paye1 + nssf1
    net = total_pay - total_taxes
    return(net)

print(netpay('paye','nssf','totalpay'))