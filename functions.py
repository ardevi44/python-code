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

def print_description (person_name):
  person = directory[person_name]
  print(f"\n{(person["name"]).capitalize()} {(person["last-name"]).capitalize()} has {person["age"]} years old, and {"She" if person["genre"] == "F" else "He"} is {person["height"]} meters tall\n")


print_description("carla")
print_description("ardevi44")

