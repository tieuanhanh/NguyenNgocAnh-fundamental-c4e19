ini_bacteria_number = int (input ("How many B bacterias are there? "))

time = int (input ("How much time in minutes will we wait? "))

periods = time//2

total_bacteria = ini_bacteria_number * 2 ** periods

print ("After {0} minutes, we would have {1} bacterias.".format(time, total_bacteria))