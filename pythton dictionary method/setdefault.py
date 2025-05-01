# Dictionary example
my_dict = {'name': 'John', 'age': 25}

# Using setdefault() for an existing key
value = my_dict.setdefault('age', 30)
print(value)  # Output: 25
print(my_dict)  # Output: {'name': 'John', 'age': 25'}

# Using setdefault() for a non-existent key
value = my_dict.setdefault('city', 'Adama')
print(value)  # Output: Adama
print(my_dict)  # Output: {'name': 'John', 'age': 25, 'city': 'Adama'}
