
from prac_07.guitar import Guitar


def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2012, 0.00)
    guitars = [gibson, another_guitar]

    for guitar in guitars:
        print(guitar)

    print("{} get_age() - Expected {}. Got {}".format(gibson.name, 96, gibson.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(another_guitar.name, 6, another_guitar.get_age()))
    print("{} is_vintage() - Expected {}. Got {}".format(gibson.name, True, gibson.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(another_guitar.name, False, another_guitar.is_vintage()))

main()