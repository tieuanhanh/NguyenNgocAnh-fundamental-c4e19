from ex7 import remove_dollar_sign

string_with_no_dollar = remove_dollar_sign("$80% percent of $life is to show $up")

if string_with_no_dollar == "80% percent of life is to show up":
    print ("Your function is correct")
else:
    print ("Oops")