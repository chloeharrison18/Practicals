def main():
    for i in range(1, 21, 2):
        print(i, end= ' ')
    print()

    for a in range(0, 101, 10):
        print(a, end= ' ')
    print()

    for b in range(20, 0, -1):
        print(b, end= ' ')
    print()

    stars = int(input("Number of stars: "))
    for s in range(0, stars):
        print("*", end= ' ')

    stars_2 = int(input("\nNumber of stars: "))
    for s in range(0, stars_2):
        print("*" * s)

main()
