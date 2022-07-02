from turtle import Turtle
import pandas


ALINGMENT = "center"

FONT = ("Arial", 18, "bold")

class Scoreboard(Turtle) :
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("scores.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score {self.highscore}", align=ALINGMENT, font=FONT)

    def increase_score(self, point):
        self.score += point
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("scores.txt", mode="w") as data:
                score = str(self.highscore)
                data.write(score)

        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.clear()
    #     self.write(f"Game Over !!!! Final Score : {self.score}", align=ALINGMENT, font=FONT)


