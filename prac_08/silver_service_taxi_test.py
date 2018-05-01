from prac_08.silver_service_taxi import SilverServiceTaxi

a_taxi = SilverServiceTaxi("wawa", 100, 0.2)
a_taxi.drive(100)
print(a_taxi)
print("${:.2f}".format(a_taxi.get_fare()))