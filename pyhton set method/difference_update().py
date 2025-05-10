# Define two sets
set_A = {1, 2, 3, 4, 5}
set_B = {3, 4, 5, 6, 7}

# Update set_A by removing elements found in set_B
set_A.difference_update(set_B)

print("set_A after difference_update():", set_A) 
