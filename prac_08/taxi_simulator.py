from prac_08.car import Car
from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    chosen_taxi = taxis[0]
    total_cost = 0
    print("Current taxi: {}".format(chosen_taxi.name))
    menu_selection = input("q)uit, c)hoose taxi, d)rive").lower()
    while menu_selection != "q":
        if menu_selection == "c":
            chosen_taxi = taxis[choose_taxi(taxis)]
        elif menu_selection == "d":
            total_cost += drive_taxi(chosen_taxi)
        print("Bill to date: ${:.2f}".format(total_cost))
        print("Current taxi: {}".format(chosen_taxi.name))
        menu_selection = input("q)uit, c)hoose taxi, d)rive").lower()
    print("Total trip cost: ${:.2f}\nTaxis are now:".format(total_cost))
    count = 0
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(count, taxi))
        count += 1



def choose_taxi(taxis):
    count = 0
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(count, taxi))
        count += 1
    chosen_taxi = int(input())
    return chosen_taxi

def drive_taxi(chosen_taxi):
    chosen_taxi.start_fare()
    distance = int(input("Drive how far?"))
    chosen_taxi.drive(distance)
    cost = chosen_taxi.get_fare()
    print("Your {} trip cost you ${:.2f}".format(chosen_taxi.name, cost))
    return cost

main()