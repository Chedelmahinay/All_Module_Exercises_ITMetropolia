
#Exercise 1

# Write a program that asks the user how many dice to roll.
# The program rolls all the dice once and
# prints out the sum of the numbers. Use a for loop.

import random
def roll_die():
    return random.randint(1, 6)
num_dice = int(input("How many dice do you want to roll? "))

total_sum = 0

for i in range(num_dice):
    roll_result = roll_die()
    total_sum += roll_result
    print(f"Roll { i + 1 }: {roll_result}")

print(f"Total sum of {num_dice} dice rolls: {total_sum}")

#Exercise 2

# Write a program that asks the user to enter numbers until they input an empty string to quit.
# At the end, the program prints out the five greatest numbers sorted in descending order.
# Hint: You can reverse the order of sorted list items by using the sort method with the reverse=True argument.
# Initialize an empty list to store numbers

numbers = []

while True:
    user_input = input("Enter a number (or press Enter to quit): ")
    if user_input == '':
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

numbers.sort(reverse=True)

print("The five greatest numbers are:")
print(numbers[:5])







#Exercise 3

#Write a program that asks the user for an integer and tells if the number is a prime number.
#Prime numbers are number that are only divisible by one or the number itself.

#For example, 13 is a prime number as it can only be divided by 1 or 13 so that the result is an integer.
#On the other hand, 21 is not a prime number as it is divisible by 3 and 7.

inp=int(input())
count=0
for i in range(1,inp+1):2
  if inp%i==0:
    count+=1
if count>2:
      print("Not a prime Number")
else:
      print('Prime Number')



#Exercise 4

# Write a program that asks the user to enter the names of five cities one by on (use a for loop for reading the names) and
# stores them into a list structure. Finally, the program prints out the names of the cities one by one, one city per line, in
# the same order they were read as input.
# Use a for loop for asking the names and a for/in loop to iterate through the list.

cities = []

for i in range(5):
    city_name = input("Enter the name of city {}: ".format(i + 1))
    cities.append(city_name)

print("City names entered by the user:")
for city in cities:
    print(city)
