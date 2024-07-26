# * F-String in Python

# score = 0
# height = 1.8
# isWining = True
# print(f"Your score: {score}\n" +
#        f"Your height: {height}\n" +
#        f"You are wining: {str(isWining)}");

# * Weeks of life left mini-project

# How many weeks we have left if we live until 90 years old
# This return a string
# age = input("What's your age? ");
# print(f"\nYou have {str(52 * 90 - int(age) * 52)} weeks left.")

# * Tip calculator mini-project

# bill = float(input("What's the bill? => $"))
# tip = float(input("How much tip would you like to give? 10, 12, or 15? => "))
# tip = (tip / 100) + 1
# bill_parts = int(input("How many people to split the bill? => "))
# bill_p_person = round(((bill / bill_parts) * tip), 2)
# print("Each person should pay: $" + "{:.2f}".format(bill_p_person))


# * Odd or even exercise
# number_test = 34

# if number_test % 2 == 0:
#   print(f"{number_test} is an even number")
# else:
#   print(f"{number_test} is an odd number")

# * BMI 2.0
# print("Welcome to the BMI calculator!\n");

# user_weight = float(input("Write your weight in Kilograms => "));
# user_height = float(input("Write your height in meters => "));

# BMI_result = float("{:.2f}".format(user_weight / user_height**2))

# print("BMI result: ", BMI_result)

# if BMI_result < 18.5:
#   print(f"You have an underweight signal")
# elif BMI_result < 25:
#   print(f"Nothing to worry about, you're in normal weight")
# elif BMI_result < 30:
#   print(f"You're slightly overweight!! Be careful for what you eat")
# elif BMI_result < 35:
#   print(f"You're obese, you're in trouble, try to eat more healthy and do exercise very often")
# else:
#   print(f"WARNING! go to hospital to be treated immediately");


# * Decides when a year is a leap year

# year = 2019
# message = f"{year} is a leap year."
  
# if (year % 4 == 0):
#   if (year % 100 == 0):
#     if (year % 400 == 0):
#       print(message)
#     else:
#       print(f"{year} is not a leap year");
#   else:
#     print(message)
# else:
#   print(f"{year} is not a leap year");

# * another great solution with logical operators

# if (year % 4 == 0) and (not (year % 100 == 0)) or (year % 400 == 0):
#   print(f"{year} is a leap year!");
# else:
#   print(f"{year} is not a leap year!");

# * Roller-coaster mini-project

# print("Welcome to the rollercoaster!\n\n")
# height = 100 * float(input("What is your height in meters? "))
# bill = 0

# if height >= 120:
#   print("You can ride the roller coaster!\n")
#   age = int(input("What's your age? "))
#   if age < 12:
#     print("Child tickets are $5.")
#     bill = 5
#   elif age <= 18:
#     print("Young tickets are $7.")
#     bill = 7
#   else:
#     print("Adult tickets are $12.")
#     bill = 12
#   wants_photo = input("\n\nDo you want a photo taken? Y or N: ")
#   if wants_photo == "Y" or wants_photo == "y":
#     bill += 3
#   print(f"\n\nYour final bill is $" + "{:.2f}".format(bill))
# else:
#   print("\n\nSorry, you have to grow taller before you can ride.")

# * Pizza Order practice

# message = "Thank you for choosing Python Pizza Deliveries!"

# print("Thank you for choosing Python Pizza Deliveries!")

# size = input("\n\nWhat size pizza do you want? S, M, or L: ").lower()
# total_bill = 0

# if size == "s":
#   total_bill = 15
# elif size == "m":
#   total_bill = 20
# elif size == "l":
#   total_bill = 25

# add_pepperoni = input("\n\nDo you want pepperoni? Y or N? ").lower()

# if add_pepperoni == "Y" or add_pepperoni == "y":
#   if size == "s":
#     total_bill += 2
#   if size == "m" or size == "l":
#     total_bill += 3

# extra_cheese = input("\n\nDo you want extra cheese? Y or N? ").lower()

# if extra_cheese == "y":
#   total_bill += 1

# print(f"\n\nYour final bill is: $" + "{:.2f}".format(total_bill) + ".")


# * Love calculator mini-project

name1 = input()
name2 = input()

# TRUE words occurs
true_word_occurs = 0
love_word_occurs = 0

true_word_occurs += name1.count("t") + name2.count("t")
true_word_occurs += name1.count("r") + name2.count("r")
true_word_occurs += name1.count("u") + name2.count("u")
true_word_occurs += name1.count("e") + name2.count("e")

love_word_occurs += name1.count("l") + name2.count("l");
love_word_occurs += name1.count("o") + name2.count("o");
love_word_occurs += name1.count("v") + name2.count("v");
love_word_occurs += name1.count("e") + name2.count("e");

# print("results: ", "For the true word: ", true_word_occurs, "For the love word: ", love_word_occurs)

love_score = int(f"{true_word_occurs}{love_word_occurs}")

# print(love_score, type(love_score))

print("The Love Calculator is calculating your score...")

if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mint.")
elif love_score >= 40 and love_score <= 50:
  print(f"Your score is {love_score}, you are alright together.");
else:
  print(f"Your score is {love_score}.")






  
    
    
  

   

