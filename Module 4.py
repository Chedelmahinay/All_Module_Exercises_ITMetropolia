#Module 4
#Exercise 1
#Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000.

i = 3
while i <= 1000:
    if not i % 3:
        print(f"the value {i} is divisible by three")
    i += 3

#Exercise 2
#Write a program that converts inches to centimeters until the user inputs a negative value. Then the program ends.
# 1 inch = 2.54 cm

while True:
    inches = float(input("What inches do you want to write?: "))
    inch_to_centi = ((inches) * 2.54)
    if inches > 0:
        print(f"the {inches} converted to Centimeter is {inch_to_centi}")
    else:
        print("Program ended due to invalid integer sign ")
        break


#Exercise 3
#Write a program that asks the user to enter numbers until they enter an empty string to quit.
#Finally, the program prints out the smallest and largest number from the numbers it received.

int_list = []

while True:
    Number = (input("Enter a number: "))
    int_list.append(Number)
    int_list.sort()

    if Number == "":
        print(f"the smallest you typed is {min(int_list[1])} and the largest is {max(int_list)}")
        break


#Exercise 4
#Write a game where the computer draws a random integer between 1 and 10.
#The user tries to guess the number until they guess the right number.
#After each guess the program prints out a text: Too high, Too low or Correct.
#Notice that the computer must not change the number between guesses.

import random
Guess = random.randint(1,10)
player = int(input("Guess a number between 1 to 10: "))
while Guess != player:
    if player < Guess:
        print("too low")
    elif player > Guess:
        print("too high")
    player = int(input("Guess a number between 1 to 10: "))
else:
    print("Correct")



#Exercise 5

#Write a program that asks the user for a username and password.
#If either or both are incorrect, the program ask the user to enter the username and password again.
#This continues until the login information is correct or wrong credentials have been entered five times.
#If the information is correct, the program prints out Welcome.
#After five failed attempts the program prints out Access denied. The correct username is python and password rules.


type_username = str(input("write your username: "))
type_password = str(input("write your password: "))
tries = 5

while type_username != "test" and type_password != "check":
    if tries != 0:
        tries -= 1
        print("\nWrong username and/or password")
        type_username = str(input("write your username: "))
        type_password = str(input("write your password: "))
    else:
        exit("Access denied")


print("WELCOME!")


#Exercise 6

import random

integer = int(input("Type an integer amount of points. (ex. 1 million): "))
Points_in_square = list(range(2))
Points_in_circle = int()

for i in range(0, integer):
    Points_in_square = [random.uniform(-1, 1), random.uniform(-1, 1)]
    if (Points_in_square[0] ** 2 + Points_in_square[1] ** 2) < 1:
        Points_in_circle += 1

print("The estimated pi value is:", 4 * Points_in_circle / integer)
