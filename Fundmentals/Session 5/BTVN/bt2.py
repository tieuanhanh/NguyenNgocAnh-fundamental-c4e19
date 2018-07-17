number = [1, 6, 8, 1, 2, 5, 6]

# cach 1:

n = int(input("Enter a number? "))

count_n = number.count(n)

print ("{0} appear {1} times in my list. ".format(n, count_n))

# cach 2:

count_n = {}

for n in number:
    count_n[n] = count_n.get(n, 0) + 1

ans = int(input("Enter a number? "))

if ans in count_n:
    print ( ans, 'appear', count_n[ans], 'times in my list.')

else:
    print ('Your number is not in the list.')