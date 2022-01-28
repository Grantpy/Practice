grade1 = float(input("Type grade of first test:"))
grade2 = float(input("Type grade of second test:"))
absences = int(input("Type total number of absences:"))
total_classes = int(input("Type total number of classes:"))

avg_grade = (grade1 + grade2) / 2
attendance = (total_classes - absences) / total_classes

print("Average grade: ", round(avg_grade,2))
print("Attendance rate: ", str(round((attendance * 100),2))+'%')

if (avg_grade >= 6):
    if(attendance >= 0.8):
        print("Passed")
    else:
        print("failed attendance lower than 80%")
elif(attendance >= 0.8):
    print("Failed due to grade lower than 6.2")
else:
    print("Failed grade lower than 6.2 and attendance lower than 80%")

               
