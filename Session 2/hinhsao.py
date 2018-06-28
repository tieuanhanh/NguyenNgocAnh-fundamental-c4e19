# for i in range (3):
#     # draw 1 line *******
#     for j in range(7):
#         print("* ", end="")
#         # print ("* ", end="------")
    
#     print()

#     # neslod loop


# for i in range (1,6):
#     for j in range (i):
#         print("* ", end="")

#     print()

n = 10

for i in range (n):
    for j in range (n):
        if (j < n - i - 1):
            print("  ", end="")
        else:
            print("* ", end="")

    print()
