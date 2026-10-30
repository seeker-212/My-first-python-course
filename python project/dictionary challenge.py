student_grade = {}

off = False

while not off:
    name = input("Enter your name: ")
    grade = input("Enter student grade: ")
    student_grade[name] = grade

    print("Student added successfully")
    print(student_grade)

    add_another = input("would you like to add another student Y or N ").lower()
    if add_another == "y":
        pass
    else:
        off = True