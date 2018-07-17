from random import choice

word = "champion"

list_1 = list (word)
list_2 = []

cou = len (list_1)

loop = True

while loop: 
        rand = random.choice(list_1)
        list_1.remove (rand)
        list_2.append (rand)
        if len (list_1) == 0:
            loop = False

print (*list_2)

looc = True
while looc:
    n = input (" Your answer: ")
    if n == word :
        print ("Hura")
        looc = False
    else:
        print (" :( ")


