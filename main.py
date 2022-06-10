from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

snake = Snake()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake.create_snake()
food = Food()
score= Scoreboard()


screen.listen()
screen.onkey(key='Up',fun=snake.up)
screen.onkey(key='Down',fun=snake.down)
screen.onkey(key='Right',fun=snake.right)
screen.onkey(key='Left',fun=snake.left)

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    snake.move_snake()
    screen.update()



    if snake.turtles[0].distance(food) < 10:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.turtles[0].xcor()>280 or snake.turtles[0].xcor()<-300 or snake.turtles[0].ycor()>270 or snake.turtles[0].ycor()<-280:
        score.high_score()
        snake.reset()

    for i in snake.turtles[1:]:
        if snake.turtles[0].distance(i)<5:
            score.high_score()
            snake.reset()

screen.exitonclick()


