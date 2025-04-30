# import csv


# with open("./weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temps = []
#     for row in data:
#         if row[1] != "temp":
#             temps.append(int(row[1]))
#     print(temps)


## using pandas pack

import pandas

data = pandas.read_csv("./weather_data.csv")

# print(data)
# print("\n" *2)
# print(data["temp"])

# data_dict = data.to_dict()
# print (data_dict)

##for list
# temp_list = data["temp"].to_list()
# print(temp_list)


# temps_list = data["temp"].to_list()
#  ## avg value
# print(data["temp"].mean())
# ## maximum value
# print(data["temp"].max()) 
# ## get data in colums
# print(data.condition) 

# get data in row
print(data[data.day == "Monday"])

#print(data[data.temp == data.temp.max()])

# fer = data[data.day == "Monday"]
# value = (fer.temp* 9/5) + 32 

# print(value)


          #Create the datafraem from scratch

# data_dist = {
#     "student":["Ram", "Sham", "Jodu", "Modu"],
#     "score" : [76, 80, 40, 95]
# }

# data = pandas.DataFrame(data_dist)
# print(data)
#       ## create new csv file
# data.to_csv("student_scor.csv")


     ##

# squirrel_data = pandas.read_csv("Squirrel_Census_Data.csv")
# colors = list(set(squirrel_data["Primary Fur Color"]))
# squirrel_color = [] 
# color_count = []

# for color in colors:
#     squirrel_color.append(color)
#     lenth_s =len(squirrel_data[squirrel_data["Primary Fur Color"] == color])
#     color_count.append(lenth_s)

# squirrel_data_count = {
#     "Fur Color":squirrel_color,
#     "Count":color_count,
# }

# data = pandas.DataFrame(squirrel_data_count)
# data.to_csv("squirrel_data_count.csv")