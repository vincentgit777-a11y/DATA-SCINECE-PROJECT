
import csv
from validator import validate_contact


def load_contacts():

    valid_students = []
    rejected_count = 0
    duplicate_count = 0

    phone_numbers = set()
    email_addresses = set()

    with open("contacts.csv", "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:

            name = row["name"]
            phone = row["phone"]
            email = row["email"]

            is_valid, reason = validate_contact(name, phone, email)

            if not is_valid:
                rejected_count += 1
                print("Rejected:", name, "-", reason)
                continue

            if phone in phone_numbers:
                duplicate_count += 1
                print("Rejected:", name, "- Duplicate phone number")
                continue

            if email.lower() in email_addresses:
                duplicate_count += 1
                print("Rejected:", name, "- Duplicate email")
                continue

            phone_numbers.add(phone)
            email_addresses.add(email.lower())

            student = {
                "name": name.strip(),
                "phone": phone.strip(),
                "email": email.strip()
            }

            valid_students.append(student)

    with open("students_clean.csv", "w", newline="") as file:
        fieldnames = ["name", "phone", "email"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(valid_students)

    print("\n----- INGESTION REPORT -----")
    print("Total records:", len(valid_students) + rejected_count + duplicate_count)
    print("Accepted records:", len(valid_students))
    print("Invalid records:", rejected_count)
    print("Duplicate records:", duplicate_count)
    return valid_students


if __name__ == "__main__":
    load_contacts()