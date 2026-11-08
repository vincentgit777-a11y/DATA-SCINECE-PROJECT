
from collections import Counter


def generate_report(students, total_records, rejected_records):

    print("\n========== STUDENT ANALYTICS ==========")

    accepted = len(students)

    if total_records == 0:
        acceptance_rate = 0
    else:
        acceptance_rate = (accepted / total_records) * 100

    print("\nDATA QUALITY REPORT")
    print("Total records:", total_records)
    print("Accepted records:", accepted)
    print("Rejected records:", rejected_records)
    print("Acceptance rate:", round(acceptance_rate, 2), "%")

    # Phone prefix distribution
    prefixes = Counter(student["phone"][0] for student in students)

    print("\nPHONE PREFIX DISTRIBUTION")

    for prefix in ["6", "7", "8", "9"]:
        print(prefix, ":", prefixes[prefix])

    # Email domain breakdown
    domains = Counter(
        student["email"].split("@")[1]
        for student in students
    )

    print("\nEMAIL DOMAIN BREAKDOWN")

    for domain, count in domains.items():
        print(domain, ":", count)

    print("\n=======================================")

