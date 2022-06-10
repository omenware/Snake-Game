from turtle import Turtle
ALLIGNMENT='center'
FONT=('Arial',25,'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super(). __init__()
        self.color('white')
        self.score=0
        with open('data.txt') as data:
           self.hscore = int(data.read())
        # self.hscore=0
        self.penup()
        self.goto(0,270)
        self. write(f'Score={self.score}   High Score={self.hscore}',align=ALLIGNMENT,font=FONT)
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score={self.score}   High Score={self.hscore}', align=ALLIGNMENT, font=FONT)

    def high_score(self):
        if self.score > self.hscore:
            self.hscore = self.score
            with open('data.txt',mode='w') as data:
                data.write(f'{self.hscore}')
        self.score=0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self. write('GAME OVER',align=ALLIGNMENT,font=FONT)

    def increase_score(self):
        self.score+=1
        self.update_scoreboard()

