# id name std english maths
students ={}

def add_student():
    sid = int(input("Enter id : "))
    if sid in students:
        print("Student with this id already exists...")
        return 

    name = input("Enter student name :")
    std = input("Enter class of student:")
    english = float(input("Enter marks of english:"))
    maths = float(input("Enter marks of maths:"))
    
    students[sid] = {
        "name" : name, 
        "std": std,
        "english": english,
        "maths": maths
    }
    print("Student added successfully...")

def delete_student():
    sid = int(input("Enter id to delete: "))
    if sid not in students:
        print("Student with this id doesn't exists...")
        return 

    del students[sid]
    print("Students deleted successfully...")

def update_student():
    sid = int(input("Enter id to update : "))
    if sid not in students:
        print("Student with this id doesn't exists...")
        return 
    english = float(input("Enter new marks of english:"))
    maths = float(input("Enter new marks of maths:"))
    
    students[sid]['english'] = english
    students[sid]['maths'] = maths
    print("Student updated successfully...")

def display_one():
    sid = int(input("Enter id to display : "))
    if sid not in students:
        print("Student with this id doesn't exists...")
        return 
    print(f"Id : {sid} , Name: {students[sid]['name']} , Class: {students[sid]['std']} , English: {students[sid]['english']} , Maths: {students[sid]['maths']}")

def display_all():
    if None in students:
        print("No students to display...")
        return 
    for sid , d in students.items():
        print(f"Id : {sid} , Name: {d['name']} , Class: {d['std']} , English: {d['english']} , Maths: {d['maths']}")

def sort_students():
    if None in students:
        print("No students to display...")
        return
    
    sorted_students = dict(
        sorted(
            students.items(),
            key =lambda x: x[1]["name"]
        )
    )
    
    for sid , d in sorted_students.items():
        print(f"Id : {sid} , Name: {d['name']} , Class: {d['std']} , English: {d['english']} , Maths: {d['maths']}")

while True:
    print("1. Add student")
    print("2. Delete student")
    print("3. Update student")
    print("4. Display one student")
    print("5. Display all students")
    print("6. Sort students")
    print("7. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_student()
    elif choice == 2:
        delete_student()
    elif choice == 3:
        update_student()
    elif choice == 4:
        display_one()
    elif choice == 5:
        display_all()
    elif choice == 6:
        sort_students()
    elif choice == 7:
        print("Exiting...")
        break