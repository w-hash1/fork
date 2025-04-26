# Using fromkeys to create a dictionary
keys = ['name', 'age', 'city']
default_value = None

new_dict = dict.fromkeys(keys, default_value)

# Print the new dictionary
print(new_dict)  # Output: {'name': None, 'age': None, 'city': None}
