fruits = ["apple", "banana", "cherry"]
for x, y in enumerate(fruits):
    print(x, y)


number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_square =[num*2 for num in number if num % 2 == 0]
print(even_square)

score = 60
status = "pass" if score > 50 else "fail"
print(status)


country = ["Nigeria", "Ghana", "Kenya"]
capital = ["Abuja", "Accra", "Nairobi"]
country_capital = list(zip(country, capital))
print(country_capital)

# student report card

students = ["Truth", "Joy", "Ben", "Ada", "Tim"]
scores = [75, 45, 88, 39, 95]
student_score = list(zip(students, scores))
passed_student = [x for x in student_score if x[1] > 50]
graded_student = list(sorted(passed_student, key=lambda x: x[1], reverse=True))

for position, student in enumerate(graded_student):
    comment = "pass" if student[1] > 50 else "fail"
    if position == 0:
        print(f"{position + 1}st positon, {student[0]} with {student[1]} point {comment}")

    if position == 1:
        print(f"{position + 1}nd positon, {student[0]} with {student[1]} point {comment}")

    if position == 2:
        print(f"{position + 1}rd positon, {student[0]} with {student[1]} point {comment}")


# fruit inventory

fruits = ["Apple", "Banana", "Cherry", "Pawpaw", "Orange", "Coconut", "Bread fruit", "Avocado"]
quantities = [5, 1, 12, 3, 0, 6, 20, 15]
fruit_quantity = list(zip(fruits, quantities))
fruit_in_stock = [fruit for fruit in fruit_quantity if fruit[1] > 0]
for quantity, fruit in enumerate(fruit_in_stock):
    in_stock = "In stock" if fruit[1] > 0 else "out of stock"
    if fruit[1] == 1:
        print(f"{quantity}, {fruit[0]} - {fruit[1]} one unit left")

    elif fruit[1] == 2:
        print(f"{quantity}, {fruit[0]} - {fruit[1]} two unit left")

    elif fruit[1] == 3:
        print(f"{quantity}, {fruit[0]} - {fruit[1]} three unit left")

    else:
        print(f"{quantity}, {fruit[0]} - {fruit[1]} {in_stock}")

