def find_first_2_word (xs):
    for wd in xs:
        if len(wd) == 2:
            return wd
    return " "

list1 = ["This", "us", "is", "me"]
print (find_first_2_word (list1))