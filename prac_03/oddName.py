"""Sheena"""
name = input("Please enter your name.")
print(name[::2])
while name =='':
    name = input("Invalid name. Please enter your name.")