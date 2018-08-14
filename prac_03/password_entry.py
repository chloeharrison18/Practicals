""" Chloe Harrison """

MIN_LENGTH = 5


def main():
    password = get_password()

    print_password(password)


def print_password(password):
    print("*" * len(password))


def get_password():
    password = input("Enter password: ")
    while len(password) < MIN_LENGTH:
        print("Needs 5 characters")
        password = input("Enter password: ")
    return password


main()
