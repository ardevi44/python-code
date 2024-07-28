directory = {
    "carla": {
        "name": "carla",
        "last-name": "florida",
        "height": 1.60,
        "age": 29,
        "genre": "F"
    },
    "diego": {
        "name": "diego",
        "last-name": "artezana",
        "height": 1.80,
        "age": 32,
        "genre": "M"
    },
    "ardevi44": {
        "name": "ardevi",
        "last-name": "44",
        "height": 1.90,
        "age": 23,
        "genre": "M",
        "job": "programmer"
    }
}

# * First function


def print_description(person_name):
    person = directory[person_name]
    message1 = f"\n{(person["name"]).capitalize()} {
        (person["last-name"]).capitalize()} has {person["age"]} years old"
    message2 = f"and {"She" if person["genre"] ==
                      "F" else "He"} is {person["height"]} meters tall\n"
    print(f"{message1} {message2}")


# print_description("carla")
# print_description("ardevi44")

# * Second function

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def calculator():
    calc_running = True
    iteration = 1
    print("Welcome to the calculator program!")
    while calc_running:
        option = int(input(
            "\n1 => Add\n2 => subtract\n3 => Multiply\n4 => Divide\n5 => Exit the app\n\nSet an option to execute: "))
        if option == 5 or option > 5:
            calc_running = False
        else:
            print("\nEnter two numbers above:")
            num1 = float(input())
            num2 = float(input())

            if option == 1:
                print(f"\nSum: {add(num1, num2)}")
            elif option == 2:
                print(f"\nSubtraction: {subtract(num1, num2)}")
            elif option == 3:
                print(f"\nMultiplication: {multiply(num1, num2)}")
            elif option == 4:
                print(f"\nDivision: {divide(num1, num2)}")


calculator()
