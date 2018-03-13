#creating a file
out_file = open("name.txt", 'w')
name = input("Please enter your name:")
print(name, file=out_file)
out_file.close()

#reading a file
in_file = open("name.txt", 'r')
name =  in_file.read().strip()
print("Your name is:",name)
in_file.close()

#adding 2 numbers
in_file = open("numbers.txt",'r')
number1 = int(in_file.readline())
number2 = int(in_file.readline())
result = number1+number2
print(result)

#solution for any number of numbers
in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
print(total)
in_file.close()