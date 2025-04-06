# Encoding a string to bytes
text = "Hello, World!"
encoded_text = text.encode()  # Default encoding is UTF-8
print(encoded_text)  # Output: b'Hello, World!'

# Encoding with a specific encoding (e.g., ASCII)
encoded_text = text.encode("ascii")
print(encoded_text)  # Output: b'Hello, World!'

# Example with error handling
text = "Café"
encoded_text = text.encode("ascii", errors="replace")  # Replace unsupported characters
print(encoded_text)  # Output: b'Caf?'
