
# Module 7

# Exercise 1

# Write a program that asks the user for a number of a month and
# then prints out the corresponding season (spring, summer, autumn, winter).
# Save the seasons as strings into a tuple in your program.
# We can define each season to last three months, December being the first month of winter.

Month_list = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
Month_season = ("Winter", "Winter", "Spring", "Spring", "Spring", "Summer", "Summer", "Summer", "Fall", "Fall", "Fall", "Winter")

month_number = int(input("Know the season by typing the numerical month's order from 1-12: "))
if 1 <= month_number <= 12:
    Month = Month_list[month_number - 1]
    season = Month_season[month_number - 1]
    print(f"The month is {Month} and its season is {season}")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")


# Exercise 2

# Write a program that asks the user to enter names until he/she enters an empty string.
# After each name is read the program either prints out New name or
# Existing name depending on whether the name was entered for the first time.
# Finally, the program lists out the input names one by one, one below another in
# any order. Use the set data structure to store the names.

names_set = set()


while True:
    name = input("Enter a name (or press Enter to stop): ")
    if name == "":
        break

    if name in names_set:
        print("Existing name")
    else:
        print("New name")
        names_set.add(name)

print("\nList of input names:")
for name in names_set:
    print(name)



# Exercise 3

# Write a program for fetching and storing airport data.
# The program asks the user if they want to enter a new airport, fetch the information of an existing airport or quit.
# If the user chooses to enter a new airport, the program asks the user to enter the ICAO code and name of the airport.
# If the user chooses to fetch airport information instead, the program asks for the ICAO code of the airport and prints out the corresponding name.
# If the user chooses to quit, the program execution ends. The user can choose a new option as many times they want until they choose to quit.
# (The ICAO code is an identifier that is unique to each airport.
# For example, the ICAO code of Helsinki-Vantaa Airport is EFHK. You can easily find the ICAO codes of different airports online.)

# Dictionary to store airport data
airport_data = {
    'KAAA': 'Logan County Airport – Lincoln, Illinois',
    'KAAF': 'Apalachicola Regional Airport – Apalachicola, Florida',
    'KAAO': 'Colonel James Jabara Airport – Wichita, Kansas',
    'KAAS': 'Taylor County Airport – Campbellsville, Kentucky',
    'KAAT': 'Alturas Municipal Airport – Alturas, California',
    'KABE': 'Lehigh Valley International Airport – Allentown, Bethlehem and Easton, Pennsylvania',
    'KABI': 'Abilene Regional Airport – Abilene, Texas',
    'KABQ': 'Albuquerque International Sunport – Albuquerque, New Mexico',
    'KABR': 'Aberdeen Regional Airport – Aberdeen, South Dakota',
    'KABY': 'Southwest Georgia Regional Airport – Albany, Georgia',
    'KACB': 'Antrim County Airport – Bellaire, Michigan',
    'KACJ': 'Jimmy Carter Regional Airport (formerly Souther Field) – Americus, Georgia',
    'KACK': 'Nantucket Memorial Airport – Nantucket, Massachusetts',
    'KACP': 'Allen Parish Airport – Oakdale, Louisiana',
    'KACQ': 'Waseca Municipal Airport – Waseca, Minnesota',
    'KACT': 'Waco Regional Airport – Waco, Texas',
    'KACV': 'Arcata-Eureka Airport – Arcata, California',
    'KACY': 'Atlantic City International Airport – Atlantic City, New Jersey',
    'KACZ': 'Henderson Field – Wallace, North Carolina',
    'KADC': 'Wadena Municipal Airport – Wadena, Minnesota',
    'KADF': 'Dexter B. Florence Memorial Field – Arkadelphia, Arkansas',
    'KADG': 'Lenawee County Airport – Adrian, Michigan',
    'KADH': 'Ada Municipal Airport – Ada, Oklahoma',
    'KADM': 'Ardmore Municipal Airport – Ardmore, Oklahoma',
    'KADS': 'Addison Airport – Addison, Texas'
}

# Add function
def add_airport():
    icao_code = input("Enter ICAO code of the airport: ").strip().upper()
    airport_name = input("Enter name of the airport: ").strip()
    airport_data[icao_code] = airport_name
    print(f"A new airport with ICAO code {icao_code} and name {airport_name} has been added.")

# Fetch function
def fetch_airport():
    icao_code = input("Enter ICAO code of the airport to fetch information: ").strip().upper()
    airport_name = airport_data.get(icao_code)
    if airport_name:
        print(f"The airport with ICAO code {icao_code} is {airport_name}.")
    else:
        print("Airport not found.")

# Main loop
while True:
    print("Options:")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_airport()
    elif choice == "2":
        fetch_airport()
    elif choice == "3":
        print("Quitting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")




