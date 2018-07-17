height = int(input("Your height = "))/100
weight = int(input("Your weight = "))

bmi = weight/ (height * height )

if bmi < 16:
    print (" Severely underweight ")
elif bmi < 18.5:
    print (" Underweight ")
elif bmi < 25:
    print (" Normal ")
elif bmi < 30:
    print (" Overweight ")
else:
    print (" Obese ")
