import json
import os

FILE_NAME = "students.json"

# ---------------- Utility functions ----------------
def load_students():
    """Load existing students from JSON file."""
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_students(students):
    """Save all students to JSON file."""
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(students, f, indent=2)

def show_students(students):
    """Display all students in a table-like format."""
    if not students:
        print("\n No students found.\n")
        return
    print("\n🎓 Student Records")
    print("-" * 100)
    for s in students:
        print(f"ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Course: {s['course']}")
    print("-" * 100)

# ---------------- Core operations ----------------
def add_student(students):
    print("\n Add New Student")
    sid = input("Enter student ID: ").strip()
    if any(s["id"] == sid for s in students):
        print(" ID already exists!")
        return
    name = input("Enter full name: ").strip().title()
    age = input("Enter age: ").strip()
    course = input("Enter course: ").strip().title()

    if not sid or not name or not age or not course:
        print("⚠️ All fields are required!")
        return

    try:
        age = int(age)
    except ValueError:
        print("⚠️ Age must be a number!")
        return

    students.append({"id": sid, "name": name, "age": age, "course": course})
    save_students(students)
    print(f" Student {name} added successfully!\n")

def search_student(students):
    sid = input("\n Enter student ID to search: ").strip()
    found = next((s for s in students if s["id"] == sid), None)
    if not found:
        print(" Student not found.\n")
        return
    print(f"Found: {found['name']} | Age: {found['age']} | Course: {found['course']}\n")

def update_student(students):
    sid = input("\n Enter student ID to update: ").strip()
    for s in students:
        if s["id"] == sid:
            print(f"Updating {s['name']}...")
            new_name = input(f"Enter new name ({s['name']}): ").strip().title() or s["name"]
            new_age = input(f"Enter new age ({s['age']}): ").strip() or s["age"]
            new_course = input(f"Enter new course ({s['course']}): ").strip().title() or s["course"]
            try:
                new_age = int(new_age)
            except ValueError:
                print("⚠️ Age must be numeric!")
                return
            s.update({"name": new_name, "age": new_age, "course": new_course})
            save_students(students)
            print(" Student updated successfully!\n")
            return
    print(" Student not found.\n")

def delete_student(students):
    sid = input("\n Enter student ID to delete: ").strip()
    for s in students:
        if s["id"] == sid:
            confirm = input(f"Are you sure you want to delete {s['name']}? (y/n): ").lower()
            if confirm == "y":
                students.remove(s)
                save_students(students)
                print(" Student deleted successfully!\n")
            else:
                print(" Deletion cancelled.\n")
            return
    print("⚠️ Student ID not found.\n")

# ---------------- Main Menu ----------------
def main():
    students = load_students()
    while True:
        print("\n📚 STUDENT MANAGEMENT SYSTEM")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Select an option: ").strip()
        if choice == "1":
            add_student(students)
        elif choice == "2":
            show_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("👋 Exiting system. Goodbye!\n")
            break
        else:
            print("⚠️ Invalid option, try again.\n")

if __name__ == "__main__":
    main()
