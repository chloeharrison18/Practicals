from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    current_taxi = None

    choice = menu_choice()

    while choice != "q":
        if choice == "c":
            show_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_choice - 1]
        elif choice == "d":
            current_taxi.start_fare()
            distance_to_drive = float(input("Drive how far? "))
            current_taxi.drive(distance_to_drive)
            trip_cost = current_taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name, trip_cost))
            total_bill += trip_cost
        else:
            print("Invalid option")
        print("Bill to date: ${:.2f}".format(total_bill))
        choice = menu_choice()

    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now:")
    show_taxis(taxis)


def menu_choice():
    user_choice = input("q)uit, c)hoose taxi, d)rive").lower()
    return user_choice


def show_taxis(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i + 1, taxi))


main()