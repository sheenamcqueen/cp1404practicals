from prac_08.car import Car
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    menu_selection = input("q)uit, c)hoose taxi, d)rive")
    chosen_taxi = 0
    while menu_selection != "q":
        if menu_selection == "c":
            choose_taxi(taxis)
        elif menu_selection == "d":
            drive_taxi(chosen_taxi)
        menu_selection = input("q)uit, c)hoose taxi, d)rive")
    print("Total trip cost: ${:.2f}")

def choose_taxi(taxis):
    count = 0
    for taxi in taxis:
        print("{} - {}".format(count, taxi))
        count += 1
    chosen_taxi = input(taxis[])
    return chosen_taxi

def drive_taxi(chosen_taxi):
    distance = input("Drive how far?")
    chosen_taxi.drive(distance)
    print ("Bill to date: ${:.2f}".format(chosen_taxi.get_fare()))

main()