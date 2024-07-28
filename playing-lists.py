# * Playing with lists

numbers = [1,2,3,4, "five"]
print(numbers)
print(type(numbers))
mix  = ["one", 2, 3.14, True, [1,2,3]]
print(mix)
print("Length of mix list: ", len(mix))
print("First element of mix list: ", mix[0])
print("Second element of mix list: ", mix[1])
print("Last element of mix list: ", mix[-1])
# Excluding the index 2
print(mix[0:2])
print(mix[2:-2])
new_length = mix.append("23")
print(new_length) # None
print(mix)

# * List comprehension
numbers = [1,2,3,4,5]
squares_of_numbers = [x**2 for x in numbers]

print(numbers)
print(squares_of_numbers)
numbers = squares_of_numbers
print(numbers)
print(squares_of_numbers)
print(f"{id(numbers)} {id(squares_of_numbers)}")
# It makes a shallow copy of the original list (copia superficial)
new_squares = squares_of_numbers.copy()
print(f"{id(squares_of_numbers)} {id(new_squares)}")

# * Creating shallow copies of lists

letters = list(("a", "b", "c", "d", "e", "f", ["g", "h", "i", "j"]))
letters_2 = letters[:] # Shallow copies just copies the outer list
print(id(letters)) 
print(id(letters_2)) # It has a different id from the copy but ...

# It will change the [6][0] position in both places letters and letters_2
letters_2[6][0] = "abc"
letters_2[2] = "def" # It will work just fine for an outer elements

print(letters)
print(letters_2)
