### LIST
names = ["John", "Bob", "Bill", "Jens"]
new_names = [item for item in names if len(item) <= 4]
big_names = [name.upper() for name in names if len(name) > 4]
print(big_names)

# exercise 1
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num * num for num in numbers]
print(squared_numbers)

# exercise 2
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num for num in numbers if num % 2 == 0]
print(result)

# exercise 3
with open("num1.txt") as file_1:
    list_1 = file_1.readlines()

with open("num2.txt") as file_2:
    list_2 = file_2.readlines()

result = [int(item.strip()) for item in list_1 if item in list_2]
print(result)

### DICTIONARY
import random

names = ["John", "Bob", "Bill", "Jens"]
student_scores = {
    name: random.randint(1, 100) for name in names
}
print(student_scores)
passed_students = {
    name: grade for (name, grade) in student_scores.items() if grade >= 50
}
print(passed_students)

# exercise 1
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {
    word: len(word) for word in sentence.split()
}
print(result)

# exercise2
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {
    day: value * 1.8 + 32 for (day, value) in weather_c.items()
}
print(weather_f)

# PANDAS DATAFRAME

student_scores = {
    "student": ["John", "Bob", "Bill", "Jens"],
    "score": [1, 2, 3, 4]
}
import pandas

student_grades = pandas.DataFrame(student_scores)
for (index, row) in student_grades.iterrows():
    print(row.student)
