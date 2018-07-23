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


def get_shapes():
    return shapes


def generate_quiz(): 
    text_list = []
    color_list = []
    for shape in shapes:
        text_list.append(shape['text'].upper())
        color_list.append(shape['color'])
    text = choice(text_list)
    color = choice(color_list)
    quiz_type = randint(0,1)
    return [
                text,
                color,
                quiz_type # 0 : meaning, 1: color
            ]

def is_inside (point_position, rectangle_position):
    if rectangle_position[0] <= point_position[0] <= (rectangle_position[0] + rectangle_position[2]) and rectangle_position[1] <= point_position[1] <= (rectangle_position[1] + rectangle_position[3]):
        return True
    else:
        return False

def mouse_press(x, y, text, color, quiz_type):
    blue_rect = shapes[1]['rect']
    red_rect = shapes[1]['rect']
    yellow_rect = shapes[2]['rect']
    green_rect = shapes[3]['rect']
    point = [x, y]
    if quiz_type == 0:
        if text == 'BLUE':
            is_inside (point, blue_rect)
        elif text == 'RED':
            is_inside (point, red_rect)
        elif text == 'YELLOW':
            is_inside (point, yellow_rect)
        elif text == 'GREEN':
            is_inside (point, green_rect)
    else:
        if color == '#3F51B5':
            is_inside (point, blue_rect)
        elif color == '#C62828':
            is_inside (point, red_rect)
        elif color == '#FFD600' :
            is_inside (point, yellow_rect)
        elif color == '#4CAF50':
            is_inside (point, green_rect)
    