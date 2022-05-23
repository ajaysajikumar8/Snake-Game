from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

my_screen = Screen()
my_screen.setup(height=600, width= 600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    
    snake.move()

    #detect collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 270 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    #detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            

my_screen.exitonclick()