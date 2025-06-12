def get_suffix(index):
    if index == 0:
        return "st"

    elif index == 1:
        return "nd"

    elif index == 2:
        return "rd"
    
    else:
        return "th"
    



def student_management(student_name, score, num_top_student=3):
    student_score =  list(zip(student_name, score))
    student_score.sort(key=lambda x: x[1], reverse=True)
    top_student = student_score[:num_top_student]

    for index, student in enumerate(top_student):
        suffix = get_suffix(index)
        print(f"{index + 1}{suffix} - {student[0]} scored {student[1]}")
 

students = ["Truth", "Joy", "Ben", "Ada", "Tim", "Mosh"]
scores = [49, 90, 49, 89, 92, 49]

student_management(students, scores, )