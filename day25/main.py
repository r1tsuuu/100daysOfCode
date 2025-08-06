# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#
# print(data)

# import csv
#
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperature = []
#     for row in data:
#         if row[1] == 'temp':
#             continue
#         temperature.append(int(row[1]))
#
#     print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")

# print(data.temp.mean())
# print(data.temp.max())
#
# #getting data in a row
# print(data[data.temp == data.temp.max()])
print(data[data.day == "Monday"]["temp"] * 9/5 + 32)