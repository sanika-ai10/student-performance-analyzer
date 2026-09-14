# Student Performance Analyzer

# Get student information
name = input("Enter the student's name: ")

# Get number of subjects
number_of_subjects = int(input("How many subjects? "))

# Create an empty dictionary
marks = {}
failed_subject = False

# Get subject names and marks
for i in range(number_of_subjects):
    subject = input(f"Enter subject {i + 1}: ")
    while True:
        try:
            mark = int(input(f"Enter marks for {subject}: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if 0 <= mark <= 100:
             break

        print("Please enter a mark between 0 and 100.")
    if mark < 40:
        failed_subject = True
    marks[subject] = mark

# Calculate total and average
total = sum(marks.values())
average = total / len(marks)

# Calculate grade
if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

# Find highest and lowest subjects
highest = max(marks, key=marks.get)
lowest = min(marks, key=marks.get)

# Display overall report
print("\n========== STUDENT PERFORMANCE REPORT ==========")

print("Student:", name)
print("Total Marks:", total)
print("Average:", round(average, 2))
print("Grade:", grade)
if failed_subject:
    print("Overall Result: FAIL")
else:
    print("Overall Result: PASS")

print("\nHighest:", highest, "-", marks[highest])
print("Lowest:", lowest, "-", marks[lowest])

# Display individual subject performance
print("\n---------- Subject Performance ----------")

for subject, mark in marks.items():
    if mark >= 40:
        print(subject, ":", mark, "→ Pass")
    else:
        print(subject, ":", mark, "→ Fail")

print("==============================================")
