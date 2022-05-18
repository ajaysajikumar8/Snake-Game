from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0,285)
        self.pendown()
        self.color("white")
        self.write("Scoreboard: ", align="center")
        
        
