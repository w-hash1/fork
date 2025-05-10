# Define two sets
set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7}

# Update set_A with the symmetric difference of set_A and set_B
set_A.symmetric_difference_update(set_B)

print("set_A after symmetric_difference_update():", set_A) #output set_A after symmetric_difference_update(): {1, 2, 3, 6, 7}

