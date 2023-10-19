# # Module 8
# #
# # Exercise 1
# #
# # Write a program that asks the user to enter the ICAO code of an airport.
# # The program fetches and prints out the corresponding airport name and location
# # (town) from the airport database used on this course.
# # The ICAO codes are stored in the ident column of the airport table.
#
# import mysql.connector
#
# connection=mysql.connector.connect(
#     host= '127.0.0.1',
#     port=3306,
#     database='first_flight_game',
#     user='dbuser',
#     password='pass_word',
#     autocommit=True
# )
#
# def getICAOairport(ident):
#     sql = "SELECT name, municipality FROM airport"
#     sql += " WHERE ident ='" + ident + "'"
#     print(sql)
#     cursor = connection.cursor()
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     if cursor.rowcount > 0:
#         for row in result:
#             print(f"The Airport name is: {row[0]} and municipality is: {row[1]}")
#     return
#
#
# ident = input("Enter the ICAO: ")
# getICAOairport(ident)
#
#
# # Exercise 2
#
# # Write a program that asks the user to enter the area code (for example FI)
# # and prints out the airports located in that country ordered by airport type.
# # For example, Finland has 65 small airports, 15 helicopter airports and so on.
#
# import mysql.connector
# connection=mysql.connector.connect(
#     host= '127.0.0.1',
#     port=3306,
#     database='first_flight_game',
#     user='dbuser',
#     password='pass_word',
#     autocommit=True
# )
#
# def airport(iso_country):
#     sql="select name from airport"
#     sql=sql+ " Where iso_country='"+ iso_country +" '"+"order by type "
#     print(sql)
#     cursor = connection.cursor()
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     if cursor.rowcount > 0:
#         for row in result:
#             print(f"the name of airport {row[0]}")
#     return
# user=input("enter area code:")
# airport(user)
#
# # Exercise 3
# # Write a program that asks the user to enter the ICAO codes of two airports.
# # The program prints out the distance between the two airports in kilometers.
# # The calculation is based on the airport coordinates fetched from the database.
# # Calculate the distance using the geopy library: https://geopy.readthedocs.io/en/stable/. Install the
# # library by selecting View / Tool Windows / Python Packages in your PyCharm IDE, write geopy into the search field and finish the installation.
# # each airport is one function
# # 1st print the longitude and latitude of 1st airport
#
# import mysql.connector
# from geopy.distance import geodesic
#
# connection=mysql.connector.connect(
#     host= '127.0.0.1',
#     port=3306,
#     database='first_flight_game',
#     user='dbuser',
#     password='pass_word',
#     autocommit=True
# )
# def distance_1(ident):
#     sql ="select latitude_deg, longitude_deg from airport"
#     sql=sql+" Where ident='"+ident+"'"
#     print(sql)
#     cursor = connection.cursor()
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     print(result)
#     a=result
#     if cursor.rowcount > 0:
#         for row in result:
#             print(f"the latitude is {row[0]} and the longitude is {row[1]}")
#     return a
#
# user_a=input("enter ICAO")
# distance_1(user_a)
#
# def distance_2(ident):
#     sql="select latitude_deg, longitude_deg from airport"
#     sql=sql+" Where ident='" +ident+"'"
#     print(sql)
#     cursor = connection.cursor()
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     print(result)
#     b=result
#     if cursor.rowcount > 0:
#         for row in result:
#             print(f"the latitude is {row[0]} and the longitude is {row[1]}")
#     return b
# user_b=input("enter ICAO")
# distance_2(user_b)
#
# result_a=distance_1(user_a)
# result_b=distance_2(user_b)
# print(f"total distance is: " ,geodesic(result_a,result_b).km)


# def greeting(name):
#     return f"Hello, {name}"
# name = input("Enter your name: ")
# print(greeting(name))
#
# import random
# def rollanddice(a,b):
#     total = 0
#     for i in range(1,a+1):
#         number = random.randint(1, b)
#         total= total+number
#     return total
# roll= int(input("How many roll do you want to have: "))
# dice= int(input("How many face do you want to have: "))
# result= rollanddice(roll, dice)
# print(result)