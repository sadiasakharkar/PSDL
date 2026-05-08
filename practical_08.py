import mysql.connector

# ---------- CONNECT ----------
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sadia@700",        
        database="student_db"
    )

# ---------- INSERT ----------
def insert_record():
    conn = connect_db()
    cursor = conn.cursor()

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    marks = float(input("Enter marks: "))

    query = "INSERT INTO students (name, age, marks) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, age, marks))
    conn.commit()

    print("Inserted successfully")

    conn.close()

# ---------- DISPLAY ----------
def display_records():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()

# ---------- UPDATE ----------
def update_record():
    conn = connect_db()
    cursor = conn.cursor()

    sid = int(input("Enter ID: "))
    marks = float(input("Enter new marks: "))

    query = "UPDATE students SET marks=%s WHERE id=%s"
    cursor.execute(query, (marks, sid))
    conn.commit()

    print("Updated successfully")

    conn.close()


# ---------- DELETE ----------
def delete_record():
    conn = connect_db()
    cursor = conn.cursor()

    sid = int(input("Enter ID to delete: "))
    query = "DELETE FROM students WHERE id=%s"
    cursor.execute(query, (sid,))
    conn.commit()

    print("Deleted successfully")

    conn.close()


# ---------- SEARCH ----------
def search_record():
    conn = connect_db()
    cursor = conn.cursor()

    sid = int(input("Enter ID: "))
    query = "SELECT * FROM students WHERE id=%s"
    cursor.execute(query, (sid,))
    row = cursor.fetchone()

    if row:
        print(row)
    else:
        print("Not found")

    conn.close()


# ---------- MENU ----------
while True:
    print("\n1.Insert 2.Display 3.Update 4.Delete 5.Search 6.Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        insert_record()
    elif ch == "2":
        display_records()
    elif ch == "3":
        update_record()
    elif ch == "4":
        delete_record()
    elif ch == "5":
        search_record()
    elif ch == "6":
        print("Program ended")
        break
    else:
        print("Invalid choice")