def is_inside (point_position, rectangle_position):
    if rectangle_position[0] <= point_position[0] <= (rectangle_position[0] + rectangle_position[2]) and rectangle_position[1] <= point_position[1] <= (rectangle_position[1] + rectangle_position[3]):
        return True
    else:
        return False

if is_inside ([100, 120], [140, 60, 100, 200]) == False:
    print ("Well done")
else:
    print ("Oops")

