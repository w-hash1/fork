# Dictionary example
my_dict = {'name': 'John', 'age': 25, 'city': 'Adama'}

# Using items() to get key-value pairs
key_value_pairs = my_dict.items()

# Printing the key-value pairs
print(key_value_pairs)  # Output: dict_items([('name', 'John'), ('age', 25), ('city', 'Adama')])

# Iterating through the key-value pairs
for key, value in my_dict.items():
    print(f"{key}: {value}")
# Output:
# name: John
# age: 25
# city: Adama
