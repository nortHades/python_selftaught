# Create a password validation system that:
# 1. Asks user to create a password
# 2. Password must meet these criteria:
#    - At least 8 characters long
#    - Contains at least one uppercase letter
#    - Contains at least one lowercase letter
#    - Contains at least one digit
# 3. Give user maximum 3 attempts
# 4. If password is valid, print "Password accepted"
# 5. If user fails all attempts, print "Account locked"
# 6. Use break when password is accepted
# 7. Use continue if password doesn't meet criteria
counter = 0
is_valid = False
while counter < 3:
    counter += 1
    password = input("create a password: ")
    # validation
    # At least 8 characters long
    if len(password) < 8:
        continue
    # Contains at least one uppercase letter
    has_upper = any(c.isupper() for c in password)
    if not has_upper:
        continue
    # Contains at least one lowercase letter
    has_lower = any(c.islower() for c in password)
    if not has_lower:
        continue
    # Contains at least one digit
    has_digit = any(c.isdigit() for c in password)
    if not has_digit:
        continue

    print("Password accepted")
    is_valid = True
    break

if not is_valid and counter == 3:
    print("Account locked")
