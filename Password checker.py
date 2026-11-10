
import re

COMMON_PASSWORDS = {
    "password", "password123", "123456",
    "12345678", "qwerty", "admin",
    "admin123", "welcome", "iloveyou",
    "abc123", "123456789"
}


def check_password(password):

    score = 0
    suggestions = []

    # Check minimum length
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    # Check recommended length
    if len(password) >= 12:
        score += 1
    else:
        suggestions.append("Use at least 12 characters for better security.")

    # Check uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Include at least one uppercase letter.")

    # Check lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Include at least one lowercase letter.")

    # Check numbers
    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Include at least one number.")

    # Check special characters
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        suggestions.append("Include at least one special character.")

    # Check common passwords
    if password.lower() in COMMON_PASSWORDS:
        return "WEAK", 0, ["This is a commonly used password. Choose a unique password."]

    # Check repeated characters
    if re.search(r"(.)\1\1", password):
        score = max(0, score - 1)
        suggestions.append("Avoid repeating the same character three or more times.")

    # Determine strength
    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    return strength, score, suggestions


def main():

    print("=" * 50)
    print("          PASSWORD STRENGTH CHECKER")
    print("=" * 50)

    # Password input is visible
    password = input("\nEnter your password: ")

    if not password:
        print("\nError: Password cannot be empty.")
        return

    strength, score, suggestions = check_password(password)

    print("\n" + "-" * 50)
    print("             PASSWORD REPORT")
    print("-" * 50)

    print("Password          :", password)
    print("Password Length   :", len(password))
    print("Security Score    :", str(score) + "/6")
    print("Password Strength :", strength)

    print("-" * 50)

    if strength == "STRONG":
        print("Excellent! Your password has good strength.")
    else:
        print("\nSuggestions to improve your password:")

        for suggestion in suggestions:
            print("*", suggestion)

    print("-" * 50)
    print("Thank you for using Password Strength Checker!")
    print("=" * 50)


if __name__ == "__main__":
    main()
