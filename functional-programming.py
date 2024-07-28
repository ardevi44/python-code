add = lambda a, b: a + b

multiply = lambda a, b: a * b

print(add(10, 4))
print(multiply(23, 56))


# Square of each number
numbers = range(1, 10 + 1)
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)
