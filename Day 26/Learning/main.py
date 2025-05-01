# list and dict comprehenstion

#        list comprehenstion

import random
import pandas

number = [1, 2, 3, 4, 5]
new_list=[n + 1 
          for n in number]
# print(new_list)

name_list = "sudarsan"
new_name = [latter for latter in name_list]
# print(new_name)

range_number=  [i+1 for i in range(1,5)]
# print(range_number)

##       condutional list comprehenstion

names = ["Alex", "jiya", "rohit", "raju", "chandan", "sky"]

##only add 4 latter names in the list
short_name = [name for name in names if len(name) <5 ]

## all names go to upper case latter
short_name_uppercase = [name.upper() for name in names if len(name) >5 ]
# print(short_name_uppercase)


## dict comprehenstion

student_names= ["Alex", "jiya", "rohit", "raju", "chandan", "sky"]

student_score = {student:random.randint(1,100) for student in student_names}

pass_student = {student:"pass" for (student, score) in student_score.items() if score >= 50 }

# print(student_score)
# print(pass_student)


student_dict = {
    "student":["Sky", "James", "Bond", "kajal", "Susmita"],
    "score":[98, 56, 40, 80, 10]
}


student_data_fran = pandas.DataFrame(student_dict)

# for (index, row) in student_data_fran.iterrows():
#     ##print(index)
#     if (row.score) <= 50:
#         print(f"{row.student} : Fall")


#1 Qustion
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day:(temp * 9/5) + 32 for (day, temp) in weather_c.items() }

print(weather_f)