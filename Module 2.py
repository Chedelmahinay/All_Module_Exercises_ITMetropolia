###Module 2

#exercise number 2.1

Name = str(input("what is your name?:"))
print("Hello," +(Name))

#exercise number 2.2

Circle_rad = float(input("What is the radius of the circle?:"))
answer = 3.14*(Circle_rad**2)
print("The area of the circle is:"+ str(answer))


#exercise number 2.3 program that prints the area and perimeter of the rectangle

length = float(input("what is the length?: "))
width = float(input("what is the width?: "))

Per = ((length*2)+(width*2))
Area = (length*width)

print(f"The perimiter is: {Per}" )
print(f"The area is: {Area}")

#exercise number 2.4 program that asks the user for
# three integer numbers. The program prints out the sum, product, and
# average of the numbers.

one = float(input("what is the first integer?: "))
two = float(input("what is the second integer?: "))
three = float(input("what is the third integer?:"))

print(f"The Sum of the integers are {one+two+three}")
print(f"The Product of the integers are {one*two*three}")
print(f"The Average of the integers are {(one+two+three)/3}")


# exercise number 2.5
# Write a program that asks the user to enter a mass in medieval units:
# talents (leiviskä), pounds (naula), and lots (luoti).
# The program converts the input to full kilograms and grams and
# outputs the result to the user:
# ----------------------------------
# One talent is 20 pounds.
# One pound is 32 lots.
# One lot is 13,3 grams


import math

talents = float(input("what is the talent?: "))
pound = float(input("what is the pounds?: "))
lot = float(input("what is the lot?: "))

# One talent is 20 pounds.
# One pound is 32 lots.
# One lot is 13,3 grams

pound_per_talent = 20
lot_per_pound = 32
grams_per_lot = 13.3

computation_to_lot = ((pound_per_talent*talents+pound)*lot_per_pound+lot)

Kilogram = (computation_to_lot*grams_per_lot)/1000
Gram = Kilogram * 1000%1000

print(f"The units to Kilogram is {math.trunc(Kilogram):3.0f} & \n The units to gram is {Gram:5.2f}")

#exercise number 2.6
#Write a program that draws two random combinations of numbers for a combination lock:
#a 3-digit code where each number is between 0 and 9.
#a 4-digit code where each number is between 1 and 6.

import random

three_randoms = ''.join([str(random.randint(0, 9)) for _ in range(3)])
print(f"3-digit code: {three_randoms}")

four_randoms =''.join([str(random.randint(1, 6)) for _ in range(4)])
print(f"4-digit code: {four_randoms}")

