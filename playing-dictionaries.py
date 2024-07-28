# First example

numbers = {
    1: "one",
    2: "two",
    3: "three"
}

print(numbers)
print(numbers[2])

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

carla = directory["carla"]
diego = directory["diego"]

print(f"{(carla["name"]).capitalize()} {(carla["last-name"]).capitalize()} has {carla["age"]
                                                                                } years old, and {"She" if carla["genre"] == "F" else "He"} is {carla["height"]} meters tall")

print(f"{(diego["name"]).capitalize()} {(diego["last-name"]).capitalize()} has {diego["age"]
                                                                                } years old, and {"She" if diego["genre"] == "F" else "He"} is {diego["height"]} meters tall")

# deleting info in a dictionary

ardevi44 = directory["ardevi44"]

del ardevi44["job"]

print(ardevi44)

# getting keys

ardevi_keys = ardevi44.keys()

print(ardevi_keys)
