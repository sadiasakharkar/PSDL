students = {}

def add_student():
    sid = int(input("Enter ID of student:"))
    if  sid in students:
        print("Student with this id already exists...")
    
    name = input("Enter student name :")
    age = int(input("Enter age of student:"))
    std = int(input("Enter class of student:"))
    marks = float(input("Enter marks of students:"))
    
    students[sid] = {
        "name" : name, 
        "age": age,
        "std" : std,
        "marks": marks
    }
    print("Student added successfully...")

def view_students():
    if not students: 
        print("No students to display...")
        return 
    
    for sid , d in students.items():
        print(f" ID:{sid} , Name: {d['name']} , Age: {d['age']} , Class: {d['std']} , Marks:{d['marks']}")

def search_student():
    sid= int(input("Enter ID of student to search:"))
    if sid in students:
        print(f" ID:{sid} , Name: {students[sid]['name']} , Age: {students[sid]['age']} , Class: {students[sid]['std']} , Marks:{students[sid]['marks']}")
    else:
        print("Student not found...")

def update_student():
    sid = int(input("Enter ID of student to update:"))
    if sid not in students:
        print("not found")
        return 

    students[sid]['name'] = input("Enter new name of student:")
    students[sid]['age'] = int(input("Enter new age of student:"))
    students[sid]['std'] = int(input("Enter new class of student:"))
    students[sid]['marks'] = float(input("Enter new marks of student:"))
    print("Student updated successfully...")

def delete_student():
    sid = int(input("Enter id of student to delete:"))
    if sid in students:
        del students[sid]
        print("Student deleted successfully...")
    else:
        print("Student not found...")
def above_marks():
    if not students:
        print("No students to display...")
        return 
    m = float(input("Enter marks to filter students:"))
    for sid , d in students.items():
        if d['marks'] > m :
            print(f" ID:{sid} , Name: {d['name']} , Age: {d['age']} , Class: {d['std']} , Marks:{d['marks']}")

def highest_marks():
    if not students:
        print("No students to display...")
        return
    highest = max(students.items() , key = lambda x : x[1]['marks'])
    print(f" ID:{highest[0]} , Name: {highest[1]['name']}")
    
def main():
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
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == '__main__':
    main()