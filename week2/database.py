students = {}

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")
    
    students[name] = {'Age': age, 'Grade': grade}
    print("Student added successfully!")

def view_student():
    name = input("Enter student name: ")
    
    if name in students:
        student = students[name]
        print("Name:", name)
        print("Age:", student['Age'])
        print("Grade:", student['Grade'])
    else:
        print("Student not found!")

def list_students():
    if students:
        for name, details in students.items():
            print("Name:", name)
            print("Age:", details['Age'])
            print("Grade:", details['Grade'])
            print("--------------------------")
    else:
        print("No students in the database!")

def update_student():
    name = input("Enter student name: ")
    
    if name in students:
        print("Enter the new information for the student:")
        age = int(input("Enter student age: "))
        grade = input("Enter student grade: ")
        
        students[name]['Age'] = age
        students[name]['Grade'] = grade
        print("Student information updated successfully!")
    else:
        print("Student not found!")

def delete_student():
    name = input("Enter student name: ")
    
    if name in students:
        del students[name]
        print("Student deleted successfully!")
    else:
        print("Student not found!")

def menu():
    print("Welcome to the Student Database Program!")
    print("1. Add Student")
    print("2. View Student")
    print("3. List All Students")
    print("4. Update Student Information")
    print("5. Delete Student")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        add_student()
    elif choice == 2:
        view_student()
    elif choice == 3:
        list_students()
    elif choice == 4:
        update_student()
    elif choice == 5:
        delete_student()
    elif choice == 6:
        print("Goodbye!")
        return
    else:
        print("Invalid choice! Please try again.")
    
    print("\n")
    menu()

menu()
