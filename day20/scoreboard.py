from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.filename = "highscore.txt"
        self.high_score = self.get_highscore()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))
        self.hideturtle()

    def get_highscore(self):
        self.high_score = 0
        with open(self.filename) as content:
            self.high_score = int(content.read())
        return self.high_score
    
    def record_highscore(self):
        with open(self.filename, 'w') as file:
            file.write(str(self.high_score))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.record_highscore()
        self.score = 0
        self.update_scoreboard()

    def calculate_score(self):
        self.score+= 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Arial", 24, "normal"))
