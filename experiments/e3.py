import csv

with open("../files/weather.csv", "r") as file:
    data = list(csv.reader(file))

city = input("Enter a city: ")

for row in data[1:]:
    if row[0] == city:
        print(f"The current temperature in {city} is {float(row[1])}")