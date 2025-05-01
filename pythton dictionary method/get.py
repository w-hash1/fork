# Dictionary example
my_dict = {'name': 'John', 'age': 25, 'city': 'Adama'}

# Get a value for an existing key
age = my_dict.get('age')
print(age)  # Output: 25

# Get a value for a non-existent key with a default value
country = my_dict.get('country', 'Ethiopia')
print(country)  # Output: Ethiopia

# Get a value for a non-existent key without a default value
hobby = my_dict.get('hobby')
print(hobby)  # Output: None
