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

try:
  while True:
    print(next(iterator))
except StopIteration:
  print("The iteration is done")