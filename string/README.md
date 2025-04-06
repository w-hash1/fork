# str.swapcase
This method returns a new string where all uppercase letters are converted to lowercase, and all lowercase letters are converted to uppercase.
# str.find()
This method searches for the first occurrence of a specified substring () within a string and returns its index. If the substring is not found, it returns -1 .
# str.index()
Similar to str.find(), this method return the index of the first occurrence of a substring () in a string. However, if the substring is not found, it raises a value error instead of returning -1.
# str.lstrip()
  Removes leading characters (from the left side) of the string. 
# str.rstrip()
  Removes trailing characters (from the right side) of the string.
# str.split()
This  method in Python splits a string into a list of substrings based on a specified delimiter. By default, it splits at whitespace.
# str.join()
The  method in Python is used to join elements of an iterable (like a list or tuple) into a single string, with a specified separator between each element.
# str.isalpha()
The  method in Python checks if all the characters in a string are alphabetic (letters). It returns True  if the string contains only letters and is non-empty, otherwise False .
This method is useful for validating inputs that should only contain alphabetic characters, such as names
 # str.isdigit()
The  method checks whether all the characters in a string are numeric digits (0-9). It returns True  if the string contains only digits and is non-empty; otherwise, it returns False .
This method is perfect for validating numeric inputs. 
# str.isalnum()
The  method checks whether all characters in a string are alphanumeric (letters or numbers). It returns True  if the string contains only letters and/or digits, and it is non-empty; otherwise, it returns False 
This method is perfect for validating strings that should only include letters and numbers, such as usernames.  
# str.isspace()
The  method checks whether all the characters in a string are whitespace characters (spaces, tabs, newlines, etc.). It returns   True if the string contains only whitespace and is not empty; otherwise, it returns False  .
This method is useful when you want to validate or filter strings based on whitespace content. 
# str.format()
The  method in Python allows you to format strings by inserting values into placeholders defined in the string. It’s a powerful and versatile tool for creating dynamic, readable strings.
This method makes it easy to format strings with dynamic values. 
# f-strings
F-strings (formatted string literals) are a concise and readable way to format strings in Python. They were introduced in Python 3.6 and allow you to embed expressions directly within curly braces  in a string, prefixed with the letter  f .
# len()
The  function in Python is used to determine the length of an object, such as a string, list, tuple, or dictionary. For strings, it returns the number of characters, including spaces and special symbols.
This example counts all the characters in the string Hello, World, including spaces and punctuation marks
# str.encode
The  method in Python is used to encode a string into bytes using a specified encoding 
This method is useful for working with text in specific encodings or preparing data for storage or transmission.
# str.islower
The  method checks whether all the characters in a string are lowercase letters. It returns True  if the string contains only lowercase letters and is not empty; otherwise, it returns False.
# str.isupper()
The  method checks whether all the alphabetic characters in a string are uppercase letters. It returns True  if the string contains only uppercase letters and is not empty; otherwise, it returns False
# str.startswith()
This method checks whether the string begins with the specified prefix ("Pyhton" in this case). You can also specify a starting position if needed! 
# str.endswith()
This method checks if the string ends with the specified suffix ( in this case). It's a handy tool for validation tasks or filtering strings. 
# str.count() 
This method counts the number of occurrences of the substring "Programming"   in the string. Note that it is case-sensitive. 
# str.replace
This method replaces all occurrences of the substring "coffee" with "tea" in the given string. 