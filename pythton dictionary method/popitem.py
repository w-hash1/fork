# Dictionary example
my_dict = {'name': 'John', 'age': 25, 'city': 'Adama'}

# Using popitem() to remove the last key-value pair
removed_item = my_dict.popitem()
print(removed_item)  # Output: ('city', 'Adama')

# Dictionary after using popitem()
print(my_dict)  # Output: {'name': 'John', 'age': 25'}
