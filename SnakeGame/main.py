from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake")

# Creating the three initial segments for the snake

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for positions in starting_positions:
    snake_segment = Turtle()
    snake_segment.pendown()
    snake_segment.color("white")
    snake_segment.shape("square")
    snake_segment.penup()
    snake_segment.goto(positions)
    segments.append(snake_segment)

screen.tracer(0, 0)

game_start = True
while game_start:
    screen.update()
    time.sleep(0.1)
    for seg in segments:
        seg.forward(20)



