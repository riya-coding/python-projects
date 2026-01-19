while True:
    print("\n==================================")
    print("Password Strength Checker")
    print("====================================")


    password=input("Enter your password: ")
    length=len(password)

    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False

    for char in password:
        if char.isupper():
            has_uppercase=True
        if char.islower():
            has_lowercase=True
        if char.isdigit():
            has_digit =True
        if not char.isalnum():
            has_special = True

    print("\n--- Password Analysis ---")
    print(f"Length: {length} characters")

    if length<6:
        print("\nResult: WEAK PASSWORD")
        print("Reason: Your password is too short (minimum 6 characters are required)")
    elif has_uppercase and has_lowercase and has_digit and has_special:
        print("\nResult: STRONG PASSWORD")
        print("Reason: Your password has uppercase, lowercase, digits and special characters")
    else:
        print("\nResult: Acceptable password")
        print("Suggestions to improve your password:")

        if not has_uppercase:
            print("-Add at least one uppercase letter")
        if not has_lowercase:
            print("-Add at least one lowercase letter")
        if not has_digit:
            print("-Add at least one digit")
        if not has_special:
            print("-Add at least one special character (@ # $ etc..)")

    retry=input("Do you want to try another strong password? (yes/no): ").lower()
    if retry != "yes":
        print("\nThank you for using Password Strength Checker.")
        break