# Define two sets where one is a proper subset of the other
set_A = {1, 2, 3}
set_B = {1, 2, 3, 4, 5}

# Check if set_A is a subset of set_B
result = set_A.issubset(set_B)
print("Is set_A a subset of set_B?", result)  # Expected Output: True

# Define another set that is not entirely contained in set_B
set_C = {1, 6}
result2 = set_C.issubset(set_B)
print("Is set_C a subset of set_B?", result2)  # Expected Output: False
