# example list data - 1: "a", "b", "c", "d", "e", "f"

# numbers = [1,2,3,4,5,6]
# # Where i is 0
# for i in numbers:
#   print(f"i is equal to {i}")
  
# print("\nSome other example\n")

# The last value is not included, is one before the value of the second parameter
# Show the count 1 to 10 but if we find with 5 we break
# for i in range(1,11):
#   print(i)
#   if i == 5:
#     break

# If we find 5 we continue to the next evaluation loop the code bellow will not executed
# print("\n\nAnother example.")
# for i in range(1,11):
#   if i == 5:
#     continue
#   print(i)

# * Iterators example

alphabet = ["a", "b", "c", "d", "e", "f"];
# get the iterator
iterator = iter(alphabet)
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


# Create an odd numbers iterator

# limit = 10 + 1
# # The 2 parameter is how many jumps we'll take inside the range
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