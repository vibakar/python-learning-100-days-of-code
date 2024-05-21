# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))

# print(temperature)


import pandas

data = pandas.read_csv("weather_data.csv")
average = data["temp"].mean()
max = data["temp"].max()

# print(f"Average: {average}")
# print(f"Max: {max}")
# print(data[data.temp == max])
monday = data[data.day == "Monday"]
c = monday.temp[0]
f = (c*9 / 5) + 32
print(f)