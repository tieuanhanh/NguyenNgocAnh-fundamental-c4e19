numb = input ("Enter your balance: ")

currency = int(numb)

print ( 'Your updated balance : ${:0,.2f}'.format(currency).replace ('$-','-$'))

