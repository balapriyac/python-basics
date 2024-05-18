# takes in an arg that's never used!
def process_student_grades(student_id, grades, course_name, instructor='Jane Lee'):
    average_grade = sum(grades) / len(grades)
    return f"Student {student_id} achieved an average grade of {average_grade:.2f} in {course_name} taught by {instructor}."


# better version!
def process_student_grades(student_id: int, grades: list, course_name: str) -> str:
    average_grade = sum(grades) / len(grades)
    return f"Student {student_id} achieved an average grade of {average_grade:.2f} in {course_name}."

# Usage
student_id = 12345
grades = [85, 90, 75, 88, 92]
course_name = "Mathematics"
result = process_student_grades(student_id, grades, course_name)
print(result)
