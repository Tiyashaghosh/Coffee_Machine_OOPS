# from turtle import Turtle , Screen
# tom = Turtle()
# tom.shape("turtle")
# tom.color("Black")
# tom.forward(100)
# tom.left(120)
# tom.forward(100)
# tom.left(120)
# tom.forward(100)
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon",["Pikachu","Squirtle","Charmander"],"l")
table.add_column("Types",["Electric","Water","Fire"])
print(table)

