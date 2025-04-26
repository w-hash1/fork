# Original dictionary
my_dict = {'name': 'John', 'age': 25}

# Update with another dictionary
new_data = {'city': 'Adama', 'age': 26}  # Note: 'age' key will be updated
my_dict.update(new_data)
print(my_dict)  # Output: {'name': 'John', 'age': 26, 'city': 'Adama'}

# Update with an iterable of key-value pairs (e.g., list of tuples)
more_data = [('country', 'Ethiopia'), ('name', 'Jack')]
my_dict.update(more_data)
print(my_dict)  # Output: {'name': 'Jack', 'age': 26, 'city': 'Adama', 'country': 'Ethiopia'}
