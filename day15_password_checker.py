
def check_password(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        suggestions.append("Add an uppercase letter.")

    if any(char.islower() for char in password):
        score += 1
    else:
        suggestions.append("Add a lowercase letter.")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append("Add a number.")

    if any(not char.isalnum() for char in password):
        score += 1
    else:
        suggestions.append("Add a special character.")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, suggestions


password = input("Enter a password to check: ")

strength, suggestions = check_password(password)

print("\nPassword strength:", strength)

if suggestions:
    print("\nSuggestions to improve:")

    for suggestion in suggestions:
        print("-", suggestion)
else:
    print("Your password meets all five checks!")
