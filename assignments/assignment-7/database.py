# database.py

# Our in-memory "database"
students_db = []


def add_student_record(student):
    """Add a new student record to the database."""
    students_db.append(student)


def get_all_students():
    """Return all students."""
    return students_db


def find_student_by_roll(roll_no):
    """Find a student by roll number."""
    for student in students_db:
        if student["roll"] == roll_no:
            return student
    return None
