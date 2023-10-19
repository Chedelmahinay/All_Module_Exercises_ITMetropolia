
# module 6

#exercise 1

#Write a function that returns a random dice roll between 1 and 6.
#The function should not have any parameters. Write a main program that rolls the dice until the result is 6.
#The main program should print out the result of each roll.

import random
def dice():
    return random.randint(1,6)


def roll():
    attempts = dice()
    print(f"you got the number: {attempts}")
    if attempts == 6:
        print("you got six now, thanks for playing")
        exit()
    else:
        roll()

roll()

#Exercise 2

#Modify the function above so that it gets the number of sides on the dice as a parameter.
#With the modified function you can for example roll a 21-sided role-playing dice.
#The difference to the last exercise is that the dice rolling in the main program continues until the
#program gets the maximum number on the dice, which is asked from the user at the beginning.


import random

def dice():
    return random.randint(1, sides)


def roll():
    attempts = dice()
    print(f"you got the number: {attempts}")
    if attempts == sides:
        print("you got six now, thanks for playing")
        exit()
    else:
        roll()

sides = int(input("how many sides do you want in the dice: "))
roll()

import random


def dice_roll():
    return random.randint(1, faces)


def main():
    num = dice_roll()
    print(f"The result is {num}.")
    if num == faces:
        exit()
    else:
        main()


faces = int(input("Insert the maximum amount of faces in the dice: "))
main()



#Exercise 3

# Write a function that gets the quantity of gasoline in American gallons and returns the number converted to litres.
# Write a main program that asks for a volume in gallons from the user and converts the value to liters.

# The conversion must be done by using the function.
# Conversions continue until the user inputs a negative value.


def convert():
    first_input = int(input("write your gas in gallons: "))
    while first_input > 0:
        print(first_input * 3.78541178)
        first_input = int(input("write another gas volume in gallons: "))

    else:
        print("program ended due to negative integer")
        exit
    return

convert()



#Exercise 4
#Write a function that gets a list of integers as a parameter.
#The function returns the sum of all the numbers in the list.
#For testing, write a main program where you create a list, call the function, and print out the value it returned.

my_list = []

def summation(integral):
    return sum(integral)

def ask_number():
    while True:
        input_str = input("Write a number (or leave it empty to calculate sum): ")
        if input_str.strip() == "":
            print(f"Here is the sum of all numbers: {summation(my_list)}")
            break
        try:
            number = int(input_str)
            if number > 0:
                my_list.append(number)
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")




ask_number()

#Exercise 5

#Write a function that gets a list of integers as a parameter.
#The function returns a second list that is otherwise the same as the original list except that all uneven numbers have been removed.
#For testing, write a main program where you create a list, call the function,
#And then print out both the original as well as the cut-down list.


int_nums = []

def even_tester(integer):
    even_num = []
    for i in integer:
        if i % 2 == 0:
            even_num.append(i)
    return even_num

def printing_test():
    while True:
        numerical = int(input("type any non-decimal number: "))
        if numerical > 0:
            int_nums.append(numerical)
            printing_test()
        else:
            print("The numbers in the list are:", int_nums, '\n' +
                  f" The even numbers inside the list are: {even_tester(int_nums)}")
            quit()

printing_test()


#Exercise 6

#Write a function that receives two parameters: the diameter of a round pizza in centimeters and the price of the pizza in euros.
#The function calculates and returns the unit price of the pizza per square meter.
#The main program asks the user to enter the diameter and price of two pizzas and
#tells the user which pizza provides better value for money (which of them has a lower unit price).
#You must use the function you wrote for calculating the unit prices.


import math


def unit_price(length, cost):
    return cost / (math.pi * (length / 200) ** 2)



def main():
    diameter, price, value = list(range(2)), list(range(2)), list(range(2))

    for i in range(2):
        diameter[i] = float(input(f"\nInsert the diameter of pizza Nº{i + 1} (cm): "))
        price[i] = float(input(f"Insert the price of pizza Nº{i + 1} (€): "))
        value[i] = unit_price(diameter[i], price[i])

    print(f"\nThe pizza with the best value is: Nº{value.index(min(value)) + 1}, costing {min(value):.2f} €/m2\n"
          f"The other pizza is: Nº{value.index(max(value)) + 1}, costing {max(value):.2f} €/m2")


main()


