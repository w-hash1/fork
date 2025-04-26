# Dictionary example
my_dict = {'name': 'John', 'age': 25, 'city': 'Adama'}

# Using pop() to remove a key and get its value
removed_value = my_dict.pop('age')
print(removed_value)  # Output: 25

# Dictionary after using pop()
print(my_dict)  # Output: {'name': 'John', 'city': 'Adama'}

# Using pop() with a default value for a non-existent key
removed_value = my_dict.pop('country', 'Not Found')
print(removed_value)  # Output: Not Found

# Using pop() without a default value for a non-existent key will raise an error
# my_dict.pop('hobby')  # KeyError: 'hobby'
