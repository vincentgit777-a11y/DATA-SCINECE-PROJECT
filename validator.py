
def validate_contact(name, phone, email):

    # check name
    if not name or name.strip() == "":
        return False, "Name is empty"

    # check phone number
    phone = phone.strip()

    if len(phone) != 10:
        return False, "Phone must contain 10 digits"

    if not phone.isdigit():
        return False, "Phone must contain only digits"

    if phone[0] not in "6789":
        return False, "Phone must start with 6, 7, 8 or 9"

    # check email
    email = email.strip()

    if email.count("@") != 1:
        return False, "Email must contain one @ symbol"

    if " " in email:
        return False, "Email must not contain spaces"

    local, domain = email.split("@")

    if local == "":
        return False, "Email username is missing"

    if "." not in domain:
        return False, "Email domain must contain a dot"

    if domain.startswith(".") or domain.endswith("."):
        return False, "Invalid email domain"

    return True, "Valid contact"
