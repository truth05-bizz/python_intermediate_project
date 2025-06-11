# Shipping Label

def shipping_label(*name, street="N/A", city="N/A", zip="N/A", POB="N/A", Country="N/A", apt="N/A"):
    for nam in name:
        print(nam, end="")
    print()
    print(f"Street: {street}")
    print(f"City: {city}")
    print(f"Zip: {zip}")
    print(f"POB: {POB}")
    print(f"Apartment: {apt}")
    print(f"Country: {Country}")

shipping_label("MR.", "Truth",
            street= "45 King str",
            city= "Ibadon",
            zip= "220102",
            Country= "Nigeria",)


# Score Evaluator

def score_converter(score):
    score_to_percentage = list(map(lambda x : (x*100)//10, score))
    threshold = list(filter(lambda x: x > 70, score_to_percentage))
    sorted_score = sorted(threshold)
    return sorted_score

scores = [3.7, 6.7, 8.9, 5.6, 7.0, 7.3]
print(score_converter(scores))



# Student Grade Summary

students = [("Truth", 100), ("Joy", 98.6), ("Ben", 88), ("mosh", 107), ("Tim", 82.4)]
curve_square = list(map(lambda x: (x[0], x[1]/2), students))
print(curve_square)
passed_student = list(filter(lambda x: x[1]>=50, sorted(curve_square, key=lambda x: x[1], reverse=True)))
print(passed_student)


class_student = [("Truth", 100),("Tim", 98.6), ("Mosh", 107)]

# Same output different code

def process_student(student_list):
    curve_score = []
    pass_student = []
    for x in student_list:
        name = x[0]
        score = x[1]
    
        curve = score/2
        curve_score.append((name, curve))

        curve_score.sort(key=lambda x: x[1], reverse=True)

    for y in curve_score:
        if y[1] >= 50:
            pass_student.append(y)

    return pass_student


student = [("Truth", 100), ("Joy", 98.6), ("Ben", 88), ("mosh", 107), ("Tim", 82.4)]
print(process_student(student))