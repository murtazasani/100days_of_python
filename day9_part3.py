# Error Handling and Data Validation in order to calculate grade and attendance of Students.

data_valid = False
while not data_valid:
    grade1 = input("Type the grade of first test: ")

    try:
        grade1 = float(grade1)
    except:
        print("Invalid Input. Only numbers are accepted. Decimels Should be separated with a dot.")
        continue

    if grade1 < 0 or grade1 > 10:
        print("The Number of grade should be between 0 to 10.")
        continue
    else:
        data_valid = True

data_valid = False
while not data_valid:
    grade2 = input("Type the grade of second test: ")

    try:
        grade2 = float(grade2)
    except:
        print("Invalid Input. Only numbers are accepted. Decimels Should be separated with a dot.")
        continue

    if grade2 < 0 or grade2 > 10:
        print("The Number of grade should be between 0 to 10.")
        continue
    else:
        data_valid = True

data_valid = False
while not data_valid:
    grade3 = input("Type the grade of third test: ")

    try:
        grade3 = float(grade3)
    except:
        print("Invalid Input. Only numbers are accepted. Decimels Should be separated with a dot.")
        continue

    if grade3 < 0 or grade3 > 10:
        print("The Number of grade should be between 0 to 10.")
        continue
    else:
        data_valid = True

data_valid = False
while not data_valid:
    grade4 = input("Type the grade of fourth test: ")

    try:
        grade4 = float(grade4)
    except:
        print("Invalid Input. Only numbers are accepted. Decimels Should be separated with a dot.")
        continue

    if grade4 < 0 or grade4 > 10:
        print("The Number of grade should be between 0 to 10.")
        continue
    else:
        data_valid = True

data_valid = False
while not data_valid:
    total_classes = input("Type the total number of classes: ")

    try:
        total_classes = float(total_classes)
    except:
        print("Invalid Input. Only numbers are accepted. Decimels Should be separated with a dot.")
        continue

    if total_classes <= 0:
        print("The Number of total classes can't be 0.")
        continue
    else:
        data_valid = True

data_valid = False
while not data_valid:
    absence = input("Enter total Number of absences: ")

    try:
        absence = float(absence)
    except:
        print("Invalid Input. Only numbers are accepted. Decimels Should be separated with a dot.")
        continue

    if absence < 0 or absence > total_classes:
        print("The Number of can't be less than 0 and greater than total number of Classes.")
        continue
    else:
        data_valid = True

avg_grade = (grade1 + grade2 + grade3 + grade4) / 4

attendance = (total_classes - absence) / total_classes

if (avg_grade < 6) and (attendance < 0.8):
    print("Student has failed due to both low grade and attendance of less than 80%.")
elif (avg_grade >= 6) and (attendance >= 0.8):
    print("The Student has been Passed.")
elif (avg_grade < 6) and (attendance >= 0.8):
    print("The Student has failed due to low grades.")
else:
    print("The Student has failed due to attendance rate lower than 80%.")

print("Average Grades: ", round(avg_grade, 2))
print("Average Attendance Rate:", str(round((attendance * 100), 2)), "%.")
