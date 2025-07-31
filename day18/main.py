import turtle
from turtle import Turtle, Screen
from random import uniform, choice
import colorgram

tim = Turtle()
tim.shape("turtle")
tim.color("pink")

# turtle challenge #1
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# turtle challenge #2
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# turtle challenge #3
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# lowest_sided_shape = 3
# highest_sided_shape = 10
# for n_sided_shape in range(lowest_sided_shape, highest_sided_shape + 1):
#     draw_shape(n_sided_shape)
#     tim.color(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))

# turtle challenge #4
#def random_color(turtle_object: Turtle):
#   turtle_object.color(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
#
# def random_walk(steps: int) -> None:
#     for _ in range(random.randint(0, steps)):
#         n = random.randint(0, 100)
#
#         if n % 4 == 0:
#             tim.right(90)
#         elif n % 4 == 1:
#             tim.right(90)
#             tim.right(90)
#         elif n % 4 == 3:
#             tim.left(90)
#         else:
#             tim.forward(15)
#         tim.forward(15)
#
#         random_color(tim)
#
# tim.pensize(5)
# tim.speed("fastest")
# random_walk(random.randint(300, 500))

# turtle challenge #5
# tim.speed("fastest")
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.circle(100)
#         tim.right(size_of_gap)
#         tim.color(uniform(0, 1), uniform(0, 1), uniform(0, 1))
#
# n = uniform(1, 50)
# draw_spirograph(n)
screen = Screen()
screen_width = screen.window_width()
screen_height = screen.window_height()

bottom_left_x = -screen_width // 2
bottom_left_y = -screen_height // 2

# turtle challenge #6
tim.speed("fastest")
turtle.colormode(255) 
colors = colorgram.extract('hirst_color_painting.jpg', 50)


def get_rgb_colors(color_list):
    rgb_colors = []
    for color in color_list:
        r = color.rgb.r 
        g = color.rgb.g
        b = color.rgb.b
        rgb_colors.append((r, g, b))
    return rgb_colors

def random_color():
    rgb_colors = get_rgb_colors(colors)
    return choice(rgb_colors)

def create_dots(num_dots: int) -> None:
    gap_size = screen_width // num_dots
    for r in range (num_dots):
        r = bottom_left_x + (r * gap_size)
        for c in range(num_dots):
            tim.penup()
            tim.setpos(r, bottom_left_y + (c * gap_size))
            tim.pendown()

            tim.begin_fill()
            tim.circle(7)
            tim.end_fill()

            tim.color(random_color())

create_dots(3)

screen.exitonclick()