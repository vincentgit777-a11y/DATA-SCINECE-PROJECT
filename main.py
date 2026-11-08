import csv
from validator import validate_contact
from loader import load_contacts
from analytics import generate_report


def view_students(students):
    print("\n----- STUDENT RECORDS -----")

    if not students:
        print("No student records found.")
        return

    for student in students:
        print(student["name"], "|", student["phone"], "|", student["email"])


def search_student(students):
    search = input("Enter name, phone or email: ").strip().lower()

    found = False

    for student in students:
        if (search == student["name"].lower()
                or search == student["phone"]
                or search == student["email"].lower()):

            print(student)
            found = True

    if not found:
        print("Student not found.")


def register_student(students):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    is_valid, reason = validate_contact(name, phone, email)

    if not is_valid:
        print("Registration failed:", reason)
        return

    for student in students:
        if student["phone"] == phone.strip():
            print("Phone number already exists.")
            return

        if student["email"].lower() == email.strip().lower():
            print("Email already exists.")
            return

    students.append({
        "name": name.strip(),
        "phone": phone.strip(),
        "email": email.strip()
    })

    print("Student registered successfully.")


def update_student(students):
    phone = input("Enter phone number of student to update: ").strip()

    for student in students:
        if student["phone"] == phone:

            name = input("Enter new name: ")
            new_phone = input("Enter new phone: ")
            email = input("Enter new email: ")

            is_valid, reason = validate_contact(name, new_phone, email)

            if not is_valid:
                print("Update failed:", reason)
                return

            for other in students:
                if other != student:
                    if other["phone"] == new_phone.strip():
                        print("Phone number already exists.")
                        return
                    if other["email"].lower() == email.strip().lower():
                        print("Email already exists.")
                        return

            student["name"] = name.strip()
            student["phone"] = new_phone.strip()
            student["email"] = email.strip()

            print("Student updated successfully.")
            return

    print("Student not found.")


def delete_student(students):
    phone = input("Enter phone number to delete: ").strip()

    for student in students:
        if student["phone"] == phone:
            students.remove(student)
            print("Student deleted successfully.")
            return

    print("Student not found.")


def save_students(students):
    with open("students_clean.csv", "w", newline="") as file:
        fieldnames = ["name", "phone", "email"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(students)

    print("Student records saved successfully.")


def main():

    students = load_contacts()

    while True:

        print("\n====== STUDENT REGISTRATION SYSTEM ======")
        print("1. View Students")
        print("2. Search Student")
        print("3. Register Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Analytics Report")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_students(students)

        elif choice == "2":
            search_student(students)

        elif choice == "3":
            register_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            delete_student(students)

        elif choice == "6":
            generate_report(
                students,
                len(students),
                0
            )

        elif choice == "7":
            save_students(students)
            print("Thank you for using the system!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

