def main():
    price = 0
    number_of_items = int(input("Number of items: "))

    while number_of_items < 0:
        print("Invalid numbers of items!")
        number_of_items = int(input("Number of items: "))

    for i in range(number_of_items):
        price_of_item = float(input("Price of item: "))

        price += price_of_item
    print("Total price for", number_of_items, "items is $", price)


main()
