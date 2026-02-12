import secrets

# fake database
user_email = "admin@gmail.com"
user_password = "oldpassword"

print("=== Forgot Password ===")
email_input = input("Enter your email: ")

if email_input == user_email:
    reset_token = secrets.token_hex(3)
    print("Reset token sent:", reset_token)

    entered_token = input("Enter reset token: ")

    if entered_token == reset_token:
        new_password = input("Enter new password: ")
        user_password = new_password
        print("Password successfully updated ✅")
    else:
        print("Invalid token ❌")
else:
    print("Email not found ❌")
