from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.update_score()
    
    def update_score(self):
        self.write(f"{self.score}", font=("arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
