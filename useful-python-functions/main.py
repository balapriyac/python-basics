# 1. bisect

from bisect import bisect_left, bisect_right, insort

# Let's create a grade tracking system
grades = [60, 70, 75, 85, 90, 95]

# Find where to insert a new grade while keeping the list sorted
new_grade = 82
position = bisect_left(grades, new_grade)
print(f"Insert 82 at position: {position}")

# Insert while maintaining sort order
insort(grades, new_grade)
print(f"Grades after insertion: {grades}")

# Find grade ranges
def grade_to_letter(score):
	breakpoints = [60, 70, 80, 90]  # F, D, C, B, A
	grades = 'FDCBA'
	position = bisect_right(breakpoints, score)
	return grades[position]

print(f"Score 82 gets grade: {grade_to_letter(82)}")
print(f"Score 75 gets grade: {grade_to_letter(75)}")

