# Original dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'Adama'}

# Copy the dictionary
copied_dict = my_dict.copy()

# Print the copied dictionary
print(copied_dict)  # Output: {'name': 'John', 'age': 25, 'city': 'Adama'}

# Modify the original dictionary
my_dict['age'] = 30

# Verify that the copied dictionary remains unchanged
print(my_dict)      # Output: {'name': 'John', 'age': 30, 'city': 'Adama'}
print(copied_dict)  # Output: {'name': 'John', 'age': 25, 'city': 'Adama'}
