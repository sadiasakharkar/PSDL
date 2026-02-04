r'''
Docstring for Assignment 04

Name        : Sadia Ansar Husain Sakharkar
UCE No      : UCE2025002
Subject     : PSDL
Assignment  : 04

Aim:
To understand the dictionary data type in Python.

Problem Statement:
A school wants a simple Student Management System to store and manage
student details such as name, age, class, and marks using Python dictionaries.

Each student record should contain:
- Student ID (unique key)
- Name
- Age
- Class
- Marks

Create a menu-driven program to perform the following operations:
- Add a new student
- View all students
- Search for a student by ID
- Update student details
- Delete a student record
- Display students who scored above a certain mark
- Find the student with the highest marks
'''

students = {}

students = {}

def get_int(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Value must be >= {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Value must be <= {max_val}")
                continue
            return value
        except ValueError:
            print("Please enter a valid integer.")

def get_float(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = float(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Value must be >= {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Value must be <= {max_val}")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")

def add_student():
    sid = get_int("Enter Student ID: ", min_val=1)
    if sid in students:
        print("Student ID already exists.")
        return

    name = input("Enter Name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    age = get_int("Enter Age: ", min_val=3, max_val=100)
    clas = input("Enter Class: ").strip()
    marks = get_float("Enter Marks: ", min_val=0, max_val=100)

    students[sid] = {
        "name": name,
        "age": age,
        "class": clas,
        "marks": marks
    }

    print("Student added successfully.")

def view_students():
    if not students:
        print("No student records available.")
        return

    for sid, d in students.items():
        print("\n-------------------")
        print(f"ID    : {sid}")
        print(f"Name  : {d['name']}")
        print(f"Age   : {d['age']}")
        print(f"Class : {d['class']}")
        print(f"Marks : {d['marks']}")

def search_student():
    if not students:
        print("No records to search.")
        return

    sid = get_int("Enter Student ID: ")
    if sid in students:
        d = students[sid]
        print("\nStudent Found")
        print(f"Name  : {d['name']}")
        print(f"Age   : {d['age']}")
        print(f"Class : {d['class']}")
        print(f"Marks : {d['marks']}")
    else:
        print("Student not found.")

def update_student():
    if not students:
        print("No records available.")
        return

    sid = get_int("Enter Student ID to update: ")
    if sid not in students:
        print("Student not found.")
        return

    print("Press Enter to keep existing value.")

    name = input("Enter Name: ").strip()
    if name:
        students[sid]["name"] = name

    age = input("Enter Age: ").strip()
    if age:
        try:
            age = int(age)
            students[sid]["age"] = age
        except ValueError:
            print("Invalid age skipped.")

    clas = input("Enter Class: ").strip()
    if clas:
        students[sid]["class"] = clas

    marks = input("Enter Marks: ").strip()
    if marks:
        try:
            marks = float(marks)
            if 0 <= marks <= 100:
                students[sid]["marks"] = marks
            else:
                print("Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid marks skipped.")

    print("Student details updated.")

def delete_student():
    if not students:
        print("No records available.")
        return

    sid = get_int("Enter Student ID to delete: ")
    if sid in students:
        del students[sid]
        print("Student record deleted.")
    else:
        print("Student not found.")

def students_above_marks():
    if not students:
        print("No records available.")
        return

    limit = get_float("Enter minimum marks: ", min_val=0, max_val=100)
    found = False

    for sid, d in students.items():
        if d["marks"] > limit:
            print(f"ID: {sid}, Name: {d['name']}, Marks: {d['marks']}")
            found = True

    if not found:
        print("No students found above given marks.")

def highest_marks():
    if not students:
        print("No records available.")
        return

    sid, d = max(students.items(), key=lambda x: x[1]["marks"])
    print("\nTop Scorer")
    print(f"ID    : {sid}")
    print(f"Name  : {d['name']}")
    print(f"Marks : {d['marks']}")

try:
    while True:
        print("\n==== Student Management System ====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by ID")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Students Above Certain Marks")
        print("7. Highest Marks")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            students_above_marks()
        elif choice == "7":
            highest_marks()
        elif choice == "8":
            print("Program terminated safely.")
            break
        else:
            print("Invalid choice.")

except KeyboardInterrupt:
    print("\nProgram interrupted by user. Exiting safely")


'''
==== Student Management System ====
1. Add Student
2. View All Students
3. Search Student by ID
4. Update Student
5. Delete Student
6. Students Above Certain Marks
7. Highest Marks
8. Exit
Enter your choice (1-8): 1

Enter Student ID: 101
Enter Name: Ayaan Khan
Enter Age: 16
Enter Class: 10th
Enter Marks: 89
Student added successfully.


==== Student Management System ====
Enter your choice (1-8): 1

Enter Student ID: 102
Enter Name: Sara Ali
Enter Age: 15
Enter Class: 9th
Enter Marks: 94
Student added successfully.


==== Student Management System ====
Enter your choice (1-8): 2

-------------------
ID    : 101
Name  : Ayaan Khan
Age   : 16
Class : 10th
Marks : 89

-------------------
ID    : 102
Name  : Sara Ali
Age   : 15
Class : 9th
Marks : 94


==== Student Management System ====
Enter your choice (1-8): 3

Enter Student ID: 102

Student Found
Name  : Sara Ali
Age   : 15
Class : 9th
Marks : 94


==== Student Management System ====
Enter your choice (1-8): 4

Enter Student ID to update: 101
Press Enter to keep existing value.
Enter Name: 
Enter Age: 17
Enter Class: 
Enter Marks: 91
Student details updated.


==== Student Management System ====
Enter your choice (1-8): 6

Enter minimum marks: 90
ID: 101, Name: Ayaan Khan, Marks: 91
ID: 102, Name: Sara Ali, Marks: 94


==== Student Management System ====
Enter your choice (1-8): 7

Top Scorer
ID    : 102
Name  : Sara Ali
Marks : 94


==== Student Management System ====
Enter your choice (1-8): 5

Enter Student ID to delete: 101
Student record deleted.


==== Student Management System ====
Enter your choice (1-8): 2

-------------------
ID    : 102
Name  : Sara Ali
Age   : 15
Class : 9th
Marks : 94


==== Student Management System ====
Enter your choice (1-8): 8
Program terminated safely.

'''