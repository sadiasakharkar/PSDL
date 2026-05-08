import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'Sadia@700',
        database = 'student_info'
    )

def insert_records():
    conn = connect_db()
    cursor = conn.cursor()
    
    name = input("Enter name: ")
    marks = float(input("Enter marks: "))
    
    query = "INSERT INTO student_info(name , marks) VALUES (%s , %s)"
    cursor.execute(query, (name , marks))
    
    conn.commit()
    print("Record inserted successfully")
    conn.close()

def display_records():
    conn = connect_db()
    cursor = conn.cursor()
    
    query = "SELECT * FROM student_info"
    cursor.execute(query)
    
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)
    
    conn.commit()
    conn.close()

def update_records():
    conn = connect_db()
    cursor = conn.cursor()
    
    id = int(input('Enter ID which to update:'))
    marks = float(input("Enter new marks:"))
    
    query = "UPDATE student_info Set marks = %s where id = %s"
    cursor.execute(query,(marks , id))
    
    conn.commit()
    print("Record updated successfully")
    conn.close()

def delete_records():
    conn = connect_db()
    cursor = conn.cursor()
    
    id = int(input('Enter ID which to delete:'))
    query = "DELETE FROM student_info where id = %s"
    cursor.execute(query,(id,))
    
    conn.commit()
    print("Record deleted successfully")
    conn.close()

def search_records():
    conn = connect_db()
    cursor = conn.cursor()
    
    id = int(input('Enter ID which to search:'))
    query = "SELECT * FROM student_info where id = %s"
    cursor.execute(query, (id , ))
    
    rows = cursor.fetchall()
    
    for row in rows:
        print(rows)
    
    conn.commit()
    conn.close()

while True:
    print("1. Insert Record")
    print("2. Display Records")
    print("3. Update Record")   
    print("4. Delete Record")
    print("5. Search Record")
    print("6. Exit")    
    
    ch = int(input("Enter your choice:"))
    if ch == 1:
        insert_records()
    elif ch == 2:
        display_records()
    elif ch == 3:   
        update_records()
    elif ch == 4:
        delete_records()
    elif ch == 5:
        search_records()
    elif ch == 6:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.") 