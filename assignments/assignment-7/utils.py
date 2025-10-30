# utils.py
from database import add_student_record, get_all_students, find_student_by_roll


def add_student():
    name = input("Enter student name: ").strip()
    roll = input("Enter roll number: ").strip()
    course = input("Enter course: ").strip()

    # Check for duplicate roll numbers
    if find_student_by_roll(roll):
        print("❌ Student with this roll number already exists!\n")
        return

    student = {"name": name, "roll": roll, "course": course}

    add_student_record(student)
    print("✅ Student added successfully!\n")


def view_students():
    students = get_all_students()
    if not students:
        print("📭 No students found!\n")
        return

    print("\n=== Student List ===")
    for s in students:
        print(f"Name: {s['name']}, Roll: {s['roll']}, Course: {s['course']}")
    print()


def search_student():
    roll = input("Enter roll number to search: ").strip()
    student = find_student_by_roll(roll)

    if student:
        print("\n🎯 Student Found:")
        print(f"Name: {student['name']}")
        print(f"Roll: {student['roll']}")
        print(f"Course: {student['course']}\n")
    else:
        print("❌ Student not found!\n")
