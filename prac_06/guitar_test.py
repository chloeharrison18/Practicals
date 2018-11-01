from prac_06.guitar import Guitar

if __name__ == "main":
    guitar1 = Guitar("1st Guitar", 2012, 1000)
    print("Guitar 1:")
    print(guitar1.get_age())
    print(guitar1.is_vintage())

    guitar2 = Guitar("2nd Guitar", 1800, 1200)
    print("Guitar 2:")
    print(guitar2.get_age())
    print(guitar2.is_vintage())