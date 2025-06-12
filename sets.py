students = ["Truth", "Joy", "Ben", "Ada", "Tim", "Mosh"]
scores = [49, 90, 49, 89, 92, 49]

student_score = list(zip(students, scores))
student_score.sort(key=lambda x : x[1])
lowest_score = student_score[0][1]
lowest_score_student = list(filter(lambda x: x[1] == lowest_score, student_score))
print(lowest_score_student)
#lowest_score_student = [x for x in student_score if x[1] == lowest_score]

lowest_score_student.sort(key=lambda x : x[0])
if len(lowest_score_student) > 1:
    for score in lowest_score_student:
        print(f"{score[0]} - {score[1]}")

else:
    print(f"{lowest_score_student[0][0]} - {lowest_score_student[0][1]}")

