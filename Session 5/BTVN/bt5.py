prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

merge = {}
for key in (prices.keys() | stock.keys()):
    if key in prices:
        merge.setdefault (key, []).append (prices [key])
    if key in stock:
        merge.setdefault (key, []). append (stock [key])

for key, value in merge.items():
    print (key)
    print ("price: ", merge[key][0])
    print ("stock: ", merge[key][1])
    print()

total = 0
for key, value in merge.items():
    total = total + merge[key][0] * merge[key][1]

print ("How much money would I make? ", total)