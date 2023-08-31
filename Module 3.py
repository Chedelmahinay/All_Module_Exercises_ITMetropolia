#Exercise 1

Fish_zander = 42.0
fish_length = float(input("What is the fish length in cm? Type: "))
if fish_length < Fish_zander:
    print(f"You can do bigger than that. {Fish_zander - fish_length} cm was the one you caught.")
else:
    print("Its time for fish barbecue BABY!")


#Exercise 2

cabin_class = str(input("\nEnter your cabin class: "))


if cabin_class == "LUX":
    (print("Cabin Class LUX:upper-deck cabin with a balcony."))
elif cabin_class == "A":
        print("Cabin Class A:above the car deck, equipped with a window.")
elif cabin_class == "B":
        print("Cabin Class B:windowless cabin above the car deck.")
elif cabin_class == "C":
        print("Cabin Class C:windowless cabin below the car deck.")
else:
        print("Invalid cabin class")


#Exercise 3

while True:
    gender = input("Enter your bio. m/f: ")
    if gender == "m" or gender == "f":
        break
    else:
        print("Invalid input. Please enter 'm' or 'f' for gender.")

while True:
    try:
        hemoglobin = int(input("Enter your g/l Hemoglobin value by numbers: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer for hemoglobin.")

if gender == "f":
    if hemoglobin < 117:
        print("Your hemoglobin value is low.")
    elif 117 <= hemoglobin <= 155:
        print("Your hemoglobin value is normal.")
    else:
        print("Your hemoglobin value is high.")
elif gender == "m":
    if hemoglobin < 134:
        print("Your hemoglobin value is low.")
    elif 134 <= hemoglobin <= 167:
        print("Your hemoglobin value is normal.")
    else:
        print("Your hemoglobin value is high.")
else:
    print("Invalid input. Please enter 'm' or 'f' for gender.")

#Exercise 4

try: year = int(input("Enter a year: "))
except: print("Not a number.");
if year % 4 == 0 or year % 400 == 0:
    print("It's a leap year")
else:
    print("Nahh bruhh, even Michael Jordan cannot leap this year")
