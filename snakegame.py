from turtle import *
from random import randrange

food = (0, 0)
snake = [(10, 0)]
aim = (0, -10)

def change(x, y):
    global aim
    aim = (x, y)

def inside(head):
    return -200 < head[0] < 190 and -200 < head[1] < 190

def draw_square(x, y, size, color):
    up()
    goto(x, y)
    down()
    begin_fill()
    fillcolor(color)
    for _ in range(4):
        forward(size)
        right(90)
    end_fill()

def move():
    global food
    head = snake[-1]
    x, y = head[0] + aim[0], head[1] + aim[1]

    if not inside((x, y)) or (x, y) in snake:
        draw_square(x, y, 9, 'red')
        update()
        return

    snake.append((x, y))

    if (x, y) == food:
        print('Snake length:', len(snake))
        food = (randrange(-15, 15) * 10, randrange(-15, 15) * 10)
    else:
        snake.pop(0)

    clear()

    for body in snake:
        draw_square(body[0], body[1], 9, 'green')

    draw_square(food[0], food[1], 9, 'red')
    update()
    ontimer(move, 100)

hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

move()
done()
