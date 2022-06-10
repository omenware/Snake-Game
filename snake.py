from turtle import Turtle,Screen
STARTING_POSITIONS= [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE=10
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake:

    def __init__(self):
        self.turtles=[]
        self.create_snake()
        self.move_snake()

    def create_snake(self):
        for i in STARTING_POSITIONS:
            self.add_turtle(i)

    def add_turtle(self,i):
        tim = Turtle('square')
        tim.shapesize(stretch_len=0.5, stretch_wid=0.5)
        tim.color('white')
        tim.penup()
        tim.goto(i)
        self.turtles.append(tim)

    def reset(self):
        for i in self.turtles:
            i.goto(1000,1000)
        self.turtles.clear()
        self.create_snake()

    def extend(self):
        self.add_turtle(self.turtles[-1].position())

    def move_snake(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[i - 1].xcor()
            new_y = self.turtles[i - 1].ycor()
            self.turtles[i].goto(new_x, new_y)
        self.turtles[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.turtles[0].heading() != DOWN:
            self.turtles[0].setheading(UP)

    def down(self):
        if self.turtles[0].heading() != UP:
            self.turtles[0].setheading(DOWN)

    def right(self):
        if self.turtles[0].heading() != LEFT:
            self.turtles[0].setheading(RIGHT)

    def left(self):
        if self.turtles[0].heading() != RIGHT:
            self.turtles[0].setheading(LEFT)




