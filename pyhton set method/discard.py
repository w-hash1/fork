# Define a set
my_set = {1, 2, 3, 4, 5}

# Remove an element using discard()
my_set.discard(3)
print("Set after discard(3):", my_set)

# Trying to discard an element that does not exist does not raise an error
my_set.discard(10) 
 print("Set after trying to discard(10):", my_set) #output Set after discard(3): {1, 2, 4, 5 } Set after trying to discard(10): {1, 2, 4, 5}
 
