# define
# arguments (tham so dau vao)
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
    # after return, program ends. 

# call:
# result = calc(3, 6, "-")
# print(result)

