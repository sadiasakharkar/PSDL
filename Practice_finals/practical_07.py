students = []

class Student:
    def __init__(self , name , rollno, marks):
        self.name = name ;
        self.rollno = rollno;
        self.marks = marks;
    
    def display(self):
        return f"Name:{self.name} , Roll No: {self.rollno} , Marks: {self.marks}"

def insert_student(name , rollno , marks):
    students.append(Student(name , rollno, marks))
    print("Student added successfully...")

def view_student():
    if not students:
        print("No students to display...")
        return
    
    for student in students:
        print(student.display())

def update_student():
    if not students:
        print("There is no students to update....")
        return
    
    rollno = int("Enter rollno of student to update:")
    
    for student in students:
        if students.rollno == rollno:
            name = input("Enter new name:")
            marks = int(input("Enter new marks:"))
            
            students.name = name
            students.marks = marks
            
def delete_student():
    sid = int(input("Enter id of student to delete:"))
    
    if sid in students:
        del students[sid]
        print("Student deleted successfully...")
    else:
        print("Student not found")

def search_student():
    sid = int(input("Enter id of student to search:"))
    
    if sid in students:
        print(students[sid].display())
    else:
        return None


while True:
    print("1. Insert Record")
    print("2. Display Records")
    print("3. Update Record")   
    print("4. Delete Record")
    print("5. Search Record")
    print("6. Exit")    
    
    ch = int(input("Enter your choice:"))
    if ch == 1:
        name = input("Enter name: ")
        rollno = int(input("Enter rollno: "))
        marks = float(input("Enter marks: "))
        insert_student(name , rollno , marks)
    elif ch == 2:
        view_student()
    elif ch == 3:   
        update_student()
    elif ch == 4:
        delete_student()
    elif ch == 5:
        search_student()
    elif ch == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")