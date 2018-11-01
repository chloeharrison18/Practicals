from prac_06.guitar_test import Guitar


guitars = []

print("My guitars!")

name = input("Name: ")
while name != "":
    guitar_input = []
    year = input("Year: ")
    cost = input("Cost: ")
    guitar_input.append(name)
    guitar_input.append(year)
    guitar_input.append(cost)
    guitars.append(guitar_input)
    name = input("Name: ")

print("\n... snip ...\n"
      "These are my guitars:")

for guitar in guitars:
    if int(guitar[2]) > 50:
        print("Guitar {}: {} ({}), worth $ {} (vintage)".format())
    else:
        print("Guitar {}: {} ({}), worth $ {}")