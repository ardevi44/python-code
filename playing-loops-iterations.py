# example list data - 1: "a", "b", "c", "d", "e", "f"

# * Simple loop in python with for in

# numbers = [1,2,3,4,5,6]
# for i in numbers:
#   print(f"i is equal to {i}")
  
# print("\nSome other example\n")

# The max value is not included, is one less before the max value
# Show the count 1 to 10 but if we find with 5 we break the loop
# for i in range(1,11):
#   print(i)
#   if i == 5:
#     break

# print("\n\nAnother example.")

# If we find 5 we continue to the next evaluation loop the code bellow will not executed
# for i in range(1,11):
#   if i == 5:
#     continue
#   print(i)

# * Working with iterators example

# alphabet = ["a", "b", "c", "d", "e", "f"];
# get the iterator
# iterator = iter(alphabet)
# print(type(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# try:
#   while True:
#     print(next(iterator))
# except StopIteration:
#   print("The iteration is done")

# * String iterator
# text = "Hello world"

# iter_text = iter(text)

# for character in iter_text:
#   print(character)


# * Create an odd numbers iterator

# limit = 10 + 1
# # The last parameter is how many jumps we'll take inside the range
# odd_iter = iter(range(1, limit, 2))

# for number in odd_iter:
#   print(number)

# # * Iterator Generators

# def new_generator():
#   yield 1
#   yield 2
#   yield 3

# for value in new_generator():
#   print(value)

# # * Fibonacci series with generators

# def fibonacci(limit):
#   a, b = 0, 1
#   while a <= limit:
#     yield a
#     a, b = b, a+b

# for number in fibonacci(10):
#   print(number)