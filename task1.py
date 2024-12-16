from datetime import datetime
import uuid


def menu():
    print("Choose an option:")
    print("1. Import students from a file")
    print("2. Add a new student")
    print("3. Mark student attendance")
    print("4. Edit student attendance")
    print("5. Remove a student")
    print("6. Save student list to a file")
    print("7. Display student list")
    print("8. Exit")
    choice = input("Choose an option: ")
    return choice

# TODO: Nothing but testing how it works :S

def import_students(file_path):
    students_list = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Zakładamy, że każdy wiersz zawiera listę studentów oddzielonych przecinkami
                students = line.strip().split(',')
                for student in students:
                    student = student.strip()
                    # Dodajemy warunek, że każdy student musi mieć dokładnie dwie części (imię i nazwisko)
                    if student and len(student.split()) == 2:
                        student_id = str(uuid.uuid4())
                        students_list[student_id] = {"name": student, "attendance": False}
                    else:
                        # Ignorujemy niepoprawne wpisy
                        print(f"Invalid student format: {student}")
            # Jeżeli nie ma żadnych poprawnych wpisów
            if not students_list:
                print("No valid students imported. File might contain invalid formats.")
    except FileNotFoundError:
        print("File not found. Starting with an empty list.")
    return students_list


# TODO: And next one here
def add_student(students_list, name):
    student_id = str(uuid.uuid4())
    students_list[student_id] = {"name": name, "attendance": False}
    print(f"Student added successfully. ID: {student_id}")
    return students_list


def remove_student(students_list, student_id):
    if student_id in students_list:
        del students_list[student_id]
        print("Student removed successfully.")
    else:
        print("No student found with the given ID.")
    return students_list


def export_students(file_path, students_list):
    with open(file_path, "a") as file:
        file.write(str(datetime.now()) + "\n")
        for student_id, student_data in students_list.items():
            attendance = "present" if student_data["attendance"] else "absent"
            file.write(f"{student_data['name']} (ID: {student_id}) - {attendance}\n")
    print("Student list saved successfully.")


def check_students(students_list):
    for student_id, student_data in students_list.items():
        attendance = input(f"Is {student_data['name']} (ID: {student_id}) present? (Y/N): ").strip().upper()
        if attendance == 'Y':
            students_list[student_id]["attendance"] = True
        elif attendance == 'N':
            students_list[student_id]["attendance"] = False
        else:
            print("Invalid choice. Skipping.")
    return students_list


def edit_students(students_list, student_id, attendance):
    if student_id in students_list:
        if attendance.upper() == 'Y':
            students_list[student_id]["attendance"] = True
        elif attendance.upper() == 'N':
            students_list[student_id]["attendance"] = False
        else:
            print("Invalid attendance format. No changes made.")
    else:
        print("No student found with the given ID.")
    return students_list


def print_students(students_list):
    for student_id, student_data in students_list.items():
        attendance = "present" if student_data["attendance"] else "absent"
        print(f"{student_data['name']} (ID: {student_id}) - {attendance}")


# File paths
file_student_list = 'students.txt'
file_attendance = 'studentsAttendance.txt'
students_list = {}


if __name__ == "__main__":
    while True:
        choice = menu()
        if choice == '1':
            students_list = import_students(file_student_list)
        elif choice == '2':
            name = input("Enter the name of the student to add: ").strip()
            students_list = add_student(students_list, name)
        elif choice == '3':
            students_list = check_students(students_list)
        elif choice == '4':
            student_id = input("Enter the student's ID: ").strip()
            attendance = input("Was the student present? (Y/N): ").strip()
            students_list = edit_students(students_list, student_id, attendance)
        elif choice == '5':
            student_id = input("Enter the ID of the student to remove: ").strip()
            students_list = remove_student(students_list, student_id)
        elif choice == '6':
            export_students(file_attendance, students_list)
        elif choice == '7':
            print_students(students_list)
        elif choice == '8':
            exit()
        else:
            print("Invalid choice.")
