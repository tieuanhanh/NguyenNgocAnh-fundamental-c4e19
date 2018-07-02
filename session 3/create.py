print( "hi there, here your favorite things so far ")
favs = ["death note", "netflix", "teaching"]

# print (*favs, sep = ", ")

# new_fav = input ("Name one thing you want to add: ")
# favs.append(new_fav)

# print (*favs, sep =", ")

for index, fav in enumerate(favs):
    print (index+1 , fav, sep =". ")

print("*" * 40)

pos = int(input("The position you want to update? "))
update_fav = input ("Your replacing fav = ")

print(pos, update_fav)

favs[pos-1] = update_fav
print(*favs)

