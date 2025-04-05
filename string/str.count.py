text = "Hello, samuel! Welcome, samuel!"
result = text.startswith("samuel")  # Checks if the text starts with "samuel"
print(result)  # Output: False

# If you'd like to specify starting positions:
result = text.startswith("samuel", 7)  # Starts checking at index 7
print(result)  # Output: True
