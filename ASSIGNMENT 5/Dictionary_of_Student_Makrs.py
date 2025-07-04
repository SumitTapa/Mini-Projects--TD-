students_marks={
    'Emma Johnson': 78,
    'Liam Smith': 92,
    'Olivia Brown': 65,
    'Noah Wilson': 43,
    'Ava Taylor': 87,
    'William Davis': 56,
    'Sophia Martinez': 95,
    'James Anderson': 72,
    'Isabella Thomas': 81,
    'Benjamin Lee': 67,
    'Mia White': 59,
    'Lucas Harris': 91,
    'Charlotte Clark': 76,
    'Henry Lewis': 88,
    'Amelia Walker': 63,
    'Alexander Hall': 49,
    'Harper Young': 97,
    'Michael Allen': 75,
    'Evelyn King': 84,
    'Daniel Scott': 71
}
student_name= input("Enter the student's name:")
if student_name in students_marks:
    print("The student has a mark of", students_marks[student_name])
else:
    print("The student named '{}', does not exist in our records.".format(student_name))