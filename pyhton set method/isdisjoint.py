# Define two sets with no elements in common
set_A = {1, 2, 3}
set_B = {4, 5, 6}

# Check if set_A and set_B are disjoint
result = set_A.isdisjoint(set_B)
print("Are set_A and set_B disjoint?", result)  # Output: True

# Define two sets with some common elements
set_C = {1, 2, 3}
set_D = {3, 4, 5}

# Check if set_C and set_D are disjoint
result2 = set_C.isdisjoint(set_D)
print("Are set_C and set_D disjoint?", result2)  # Output: False
