from random import *
from ex11 import is_inside

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
    # text_list = []
    # color_list = []
    # for shape in shapes:
    #     text_list.append(shape['text'].upper())
    #     color_list.append(shape['color'])
    # text = choice(text_list)
    # color = choice(color_list)
    # quiz_type = randint(0,1)
    return [
                choice(shapes)['text'],
                choice(shapes)['color'],
                randint(0,1) # 0 : meaning, 1: color
            ]

def mouse_press(x, y, text, color, quiz_type):
    if quiz_type == 0:    # meaning
        for i in range(len(shapes)):
            if text == shapes[i]['text'].lower():
                check = is_inside([x,y],shapes[i]['rect'])
    else:
        for i in range(len(shapes)):
            if color == shapes[i]['color']:
                check = is_inside([x,y], shapes[i]['rect'])

    if check:
        return True
    else:
        return False

    # blue_rect = shapes[0]['rect']
    # red_rect = shapes[1]['rect']
    # yellow_rect = shapes[2]['rect']
    # green_rect = shapes[3]['rect']
    # point = [x, y]
    # if quiz_type == 0:
    #     if text == 'BLUE':
    #         n = is_inside (point, blue_rect)
    #         if n == True:
    #             return True
    #         else:
    #             return False
    #     elif text == 'RED':
    #         n = is_inside (point, red_rect)
    #         if n == True:
    #             return True
    #         else:
    #             return False
    #     elif text == 'YELLOW':
    #         n = is_inside (point, yellow_rect)
    #         if n == True:
    #             return True
    #         else:
    #             return False
    #     elif text == 'GREEN':
    #         n = is_inside (point, green_rect)
    #         if n == True:
    #             return True
    #         else:
    #             return False
    # else:
    #     if color == '#3F51B5':
    #         n = is_inside (point, blue_rect)
    #         if n == True:
    #             return True
    #         else:
    #             return False
    #     elif color == '#C62828':
    #         n = is_inside (point, red_rect)
    #         if n == True:
    #             return True
    #         else:
    #             return False
    #     elif color == '#FFD600' :
    #         n = is_inside (point, yellow_rect)
    #         if n == True:
    #             return True
    #         else:
    #             return False
    #     elif color == '#4CAF50':
    #         n = is_inside (point, green_rect)
    #         if n == True:
    #             return True
    #         else:
    #             return False
    
