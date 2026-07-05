# ==========================================
# PERSONAL POCKET CGPA CALCULATOR (PPC)
# ==========================================

print("=" * 45)
print("     PERSONAL POCKET CGPA CALCULATOR")
print("=" * 45)

name = input("Enter your name: ")
matric = input("Enter your Matric Number: ")

total_points = 0
total_units = 0

courses = int(input("\nEnter the number of courses: "))

for i in range(courses):
    print(f"\nCourse {i+1}")

    course = input("Course Code: ")
    unit = int(input("Course Unit: "))
    score = float(input("Score (0 - 100): "))

    # Grade and Grade Point using selection statements
    if score >= 70:
        grade = "A"
        point = 5
    elif score >= 60:
        grade = "B"
        point = 4
    elif score >= 50:
        grade = "C"
        point = 3
    elif score >= 45:
        grade = "D"
        point = 2
    elif score >= 40:
        grade = "E"
        point = 1
    else:
        grade = "F"
        point = 0

    quality_point = point * unit

    total_points += quality_point
    total_units += unit

    print("Grade:", grade)
    print("Grade Point:", point)
    print("Quality Point:", quality_point)

# GPA Calculation
gpa = total_points / total_units

print("\n" + "=" * 45)
print("STUDENT RESULT")
print("=" * 45)
print("Name:", name)
print("Matric Number:", matric)
print("Total Credit Units:", total_units)
print("Total Quality Points:", total_points)
print("GPA: {:.2f}".format(gpa))

# GPA Classification
if gpa >= 4.50:
    print("Class of Degree: First Class")
elif gpa >= 3.50:
    print("Class of Degree: Second Class Upper")
elif gpa >= 2.40:
    print("Class of Degree: Second Class Lower")
elif gpa >= 1.50:
    print("Class of Degree: Third Class")
elif gpa >= 1.00:
    print("Class of Degree: Pass")
else:
    print("Class of Degree: Fail")

print("=" * 45)

# Save CGPA Option
choice = input("\nDo you want to calculate another semester? (Y/N): ")

if choice.upper() == "Y":
    previous_cgpa = float(input("Enter your previous CGPA: "))
    previous_units = int(input("Enter previous total credit units: "))

    overall_points = (previous_cgpa * previous_units) + total_points
    overall_units = previous_units + total_units

    cgpa = overall_points / overall_units

    print("\nYour New CGPA is: {:.2f}".format(cgpa))
else:
    print("\nThank you for using the Personal Pocket CGPA Calculator.")