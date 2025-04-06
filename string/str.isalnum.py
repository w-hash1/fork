text = "Python123"
result = text.isalnum()
print(result)  # Output: True

text = "Python 123"  # Contains a space
result = text.isalnum()
print(result)  # Output: False

text = "123!"
result = text.isalnum()
print(result)  # Output: False
