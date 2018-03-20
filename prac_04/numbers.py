def main():
    numbers =[]

    for i in range(1,5+1):
        number = int(input("Please enter number {:2} :".format(i)))
        numbers.append(number)

    print_numbers_report(numbers)

def print_numbers_report(numbers):
    print("The first number is:", numbers[0])
    print("The last number is:", numbers[-1])
    print("The smallest number is:", min(numbers))
    print("The largest number is:", max(numbers))
    print("The average of the numbers is:", sum(numbers)/len(numbers))


main()