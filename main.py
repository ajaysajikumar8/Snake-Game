from turtle import Screen
from snake import Snake
from food import Food
import time

my_screen = Screen()
my_screen.setup(height=600, width= 600)
my_screen.bgcolor("black")
my_screen.title("Snake Game")
my_screen.tracer(0)

snake = Snake()
food = Food()

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

my_screen.exitonclick()