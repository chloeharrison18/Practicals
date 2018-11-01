from prac_08.silver_service_taxi import SilverServiceTaxi

taxi = SilverServiceTaxi("Silver", 100, 2)
taxi.drive(18)
print(taxi)
print("${:.2f}".format(taxi.get_fare()))