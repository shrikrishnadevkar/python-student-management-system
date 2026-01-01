# Student Management System
# Author: Shrikrishna Devkar

students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")

    student = {
        "name": name,
        "roll": roll,
        "marks": marks
    }

    students.append(student)
    print("✅ Student added successfully!\n")

def view_students():
    if not students:
        print("⚠ No students found.\n")
        return

    print("\n--- Student List ---")
    for i, s in enumerate(students, start=1):
        print(f"{i}. Name: {s['name']}, Roll: {s['roll']}, Marks: {s['marks']}")
    print()

def delete_student():
    roll = input("Enter roll number to delete: ")

    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("🗑 Student deleted successfully!\n")
            return

    print("❌ Student not found.\n")

def menu():
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            print("👋 Exiting program.")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

menu()
