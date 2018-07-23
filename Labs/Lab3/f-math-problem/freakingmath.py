from random import *

def calc (x, y, op):

    res = 0
    if op == '+':
        res = x + y
    elif op == '-':
        res = x - y
    elif op == '*':
        res = x * y
    elif op == '/':
        res = x / y
    return res

def generate_quiz():
    # Hint: Return [x, y, op, display_result]
    x = randint(1, 10)
    y = randint(1, 10)
    op = choice (['+', '-', '*', '/'])
    error = choice ([-1, 0, 1])
    result = calc(x, y, op)
    display_result = result + error
    return [x, y, op, display_result]

def check_answer(x, y, op, result, user_choice):
    # User_choice: T/F
    res = calc (x, y, op)
    if res == result:
        if user_choice == 'T':
            return True
        else:
            return False
    else:
        if user_choice == 'T':
            return False
        else:
            return True

# res = check_answer(1, 10, "+", 11, "T")  
# print (res)
# res = check_answer(1, 10, "+", 11, "F")  
# print (res)
# res = check_answer(1, 10, "+", 12, "T")  
# print (res)
# res = check_answer(1, 10, "+", 12, "F")  
# print (res)