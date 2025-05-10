# Define two sets
set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7}

# Get the symmetric difference between set_A and set_B
# It returns a new set containing elements that are in either set but not in both
sym_diff = set_A.symmetric_difference(set_B)

print("Symmetric Difference:", sym_diff) #output Symmetric Difference: {1, 2, 3, 6, 7}
