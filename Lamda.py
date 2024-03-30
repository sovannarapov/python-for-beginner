# Lamda function is a small, annonymous function defined with lamda keyword
# They can have any arguments but only one expression
# Perfect when you need a simple function for a short period

ls = [
    {'id': 1, 'name': 'Vuthy', 'age': 33},  # Capital letter is smaller than lower case
    {'id': 2, 'name': 'java', 'age': 70},
    {'id': 3, 'name': 'c#', 'age': 55},
    {'id': 4, 'name': 'vichet', 'age': 22},
]

ls.sort(key=lambda people: people['name'].lower())  # reverse default is False
# ls.sort(key=lambda people: people['age'], reverse=True)

for person in ls:
    print(person)
