# def mouse_press(x, y, text, color, quiz_type):
#     return True

from random import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]

blue_rect = shapes[0]['rect']
red_rect = shapes[1]['rect']
yellow_rect = shapes[2]['rect']
green_rect = shapes[3]['rect']
print (blue_rect)

quiz_type = randint (0,1)


def is_inside (point_position, rectangle_position):
    if rectangle_position[0] <= point_position[0] <= (rectangle_position[0] + rectangle_position[2]) and rectangle_position[1] <= point_position[1] <= (rectangle_position[1] + rectangle_position[3]):
        return True
    else:
        return False

def mouse (point):
    if quiz_type == 0:
        text = input ('text')
        if text == 'BLUE':
            # n = is_inside (point, blue_rect)
            return "b"
        elif text == 'RED':
            return 'r'
            # n = is_inside (point, red_rect)
        elif text == 'YELLOW':
            # is_inside (point, yellow_rect)
            return 'y'
        elif text == 'GREEN':
            return 'g'
            # is_inside (point, green_rect)
    else:
        color = input ('color')
        if color == '#3F51B5':
            # is_inside (point, blue_rect)
            return 'b'
        elif color == '#C62828':
            # is_inside (point, red_rect)
            return 'r'
        elif color == '#FFD600' :
            # is_inside (point, yellow_rect)
            return 'y'
        elif color == '#4CAF50':
            # is_inside (point, green_rect)
            return 'g'

res = mouse ([100,200])
print (res)


        