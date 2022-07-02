import random
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("Black")
screen.title("My Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #collison
    if snake.head.distance(food) < 15:
        if random.randint(0, 6) == 1:
            food.super_food()
            snake.extend()
            score.increase_score(2)
        else:
            food.refresh()
            snake.extend()
            score.increase_score(1)

    #wall_collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # game_is_on = False
        # score.game_over()
        score.reset()
        snake.reset()
    #tale_collision
    for segment in snake.snake_segments[1:]:
        # if segment == snake.head :
        #     pass
        if snake.head.distance(segment) < 10:
            # is_game_on = False
            # score.game_over()
            score.reset()
            snake.reset()

screen.exitonclick()
