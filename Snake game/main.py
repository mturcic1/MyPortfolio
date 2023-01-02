from turtle import Screen
import time
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)


segments = []

snake = Snake()
food_token = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    # Detect food collision
    if snake.head.distance(food_token) < 15:
        food_token.refresh_food()
        snake.extend()
        scoreboard.increase_score()

    # Detect wall collision
    if snake.head.xcor() == 280 or snake.head.xcor() == -280 or snake.head.ycor() == 280 or snake.head.ycor() == -280:
        scoreboard.reset()
        snake.reset()
        #game_is_on = False
        #scoreboard.game_over()

    # Detect collision with tail.
    for segment in snake.segments[1::]:
        if snake.head.distance(segment) < 1:
            #game_is_on = False
            #scoreboard.game_over()
            scoreboard.reset()
            snake.reset()




    snake.snake_movement()

screen.exitonclick()
