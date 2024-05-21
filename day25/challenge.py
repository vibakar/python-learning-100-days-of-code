import pandas

fur_color = ["Cinnamon", "Black", "Gray"]
count = []

data = pandas.read_csv("squirrel_count.csv")
for color in fur_color:
    color_data = data[data["Primary Fur Color"] == color]
    count.append(len(color_data))

data_dict = {
    "Fur Color": fur_color,
    "Count": count
}

df = pandas.DataFrame(data_dict)
df.to_csv('output.csv') 