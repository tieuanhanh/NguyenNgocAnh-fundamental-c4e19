ini_bacteria_number = int (input ("How many B bacteria are there? "))

time = int (input ("How much time in minutes will we wait? "))

total_bacteria = ini_bacteria_number * 2 ** (time/2)

print ("After {0} minutes, we would have {1} bacteria.".format(time, total_bacteria))