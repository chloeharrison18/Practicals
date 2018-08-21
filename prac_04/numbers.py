list_of_numbers = []

for i in range(1, 6):
    number_input = int(input("Number: "))
    list_of_numbers.append(number_input)

print("The first number is {}".format(list_of_numbers[0]))
print("The last number is {}".format(list_of_numbers[4]))
print("The smallest number is {}".format(min(list_of_numbers)))
print("The largest number is {}".format(max(list_of_numbers)))
print("The average of the numbers is {}".format(sum(list_of_numbers) / len(list_of_numbers)))