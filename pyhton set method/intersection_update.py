# Define two sets
set_A = {1, 2, 3, 4, 5}
set_B = {3, 4, 5, 6, 7}

# Update set_A by keeping only elements that are common with set_B
set_A.intersection_update(set_B)

print("set_A after intersection_update():", set_A) #output set_A after intersection_update(): {3, 4, 5}
