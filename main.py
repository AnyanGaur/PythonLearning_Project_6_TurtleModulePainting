from turtle import Turtle , Screen

turtle_object=Turtle()
user_input = int(input("How many moves do you want the turtle to make "))


turtle_object.shape("circle")
turtle_object.color("red", "green")
def design ():
    turtle_object.forward(i)
    turtle_object.right(90)
    turtle_object.forward(i)
    turtle_object.right(90)
    turtle_object.forward(i)
    turtle_object.right(90)
    turtle_object.forward(i)
    turtle_object.forward(i)
    turtle_object.right(90)

for i in range (user_input):
    design()
    
    



screen=Screen()
screen.exitonclick()

#screen.exitonclick()
