from prac_08.car import Car
from prac_08.unreliable_car import UnreliableCar


unreliable_car = UnreliableCar("Brom", 100, 0.5)
reliable_car = UnreliableCar("Brom", 100, 1)
unreliable_car.drive(100)
print(unreliable_car)