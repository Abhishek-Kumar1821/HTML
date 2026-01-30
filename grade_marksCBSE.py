# Take input from user
name = input("Enter student's name: ")
roll_number = input("Enter student's roll number: ")

# Take marks of each subject
english = float(input("Enter marks in English: "))
hindi = float(input("Enter marks in Hindi: "))
maths = float(input("Enter marks in Maths: "))
science = float(input("Enter marks in Science: "))
social_science = float(input("Enter marks in Social Science: "))

# Calculate total marks
total_marks = english + hindi + maths + science + social_science

# Calculate percentage
percentage = (total_marks / 500) * 100

# Determine grade
if percentage >= 90:
    grade = "A1"
elif percentage >= 80 and percentage < 90:
    grade = "A2"
elif percentage >= 70 and percentage < 80:
    grade = "B1"
elif percentage >= 60 and percentage < 70:
    grade = "B2"
elif percentage >= 50 and percentage < 60:
    grade = "C1"
elif percentage >= 40 and percentage < 50:
    grade = "C2"
elif percentage >= 33 and percentage < 40:
    grade = "D"
else:
    grade = "E"

# Print the result
print(f"Name: {name}")
print(f"Roll Number: {roll_number}")
print(f"English: {english}")
print(f"Hindi: {hindi}")
print(f"Maths: {maths}")
print(f"Science: {science}")
print(f"Social Science: {social_science}")
print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage}%")
print(f"Grade: {grade}")
