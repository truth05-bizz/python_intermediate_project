def student_management(student_name, score, num_top_student=3):
    student_score =  list(zip(student_name, score))
    student_score.sort(key=lambda x: x[1], reverse=True)
    top_student = student_score[:3]
    if num_top_student == 2:
        called_student = top_student[:2]
        print(called_student)
        for index, student in enumerate(called_student):
            if index == 0:
                print(f"{index + 1}st {student[0]} {student[1]}")
            else:
                 print(f"{index + 1}nt {student[0]} {student[1]}")

    elif num_top_student == 1:
        called_student = top_student[:1]
        for index, student in enumerate(called_student):
            if index == 0:
                print(f"{index + 1}st {student[0]} {student[1]}")

    

    else:
        for index, student in enumerate(top_student):
            if index == 0:
                print(f"{index + 1}st {student[0]} {student[1]}")
            elif index == 1:
                 print(f"{index + 1}nt {student[0]} {student[1]}")
            else: 
                print(f"{index + 1}rd {student[0]} {student[1]}")


students = ["Truth", "Joy", "Ben", "Ada", "Tim", "Mosh"]
scores = [49, 90, 49, 89, 92, 49]

student_management(students, scores, 1)