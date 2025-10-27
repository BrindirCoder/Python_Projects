import random
import string


length = int(input("How Long The Password You Want :"))

charecture = string.ascii_letters + string.digits + string.punctuation

password = []
for i in range(length):
    x = random.choice(charecture)
    password.append(x)

final_password = "".join(password)
print("The random password is :", final_password)

save_as_files = input("Do You Want Save It In File? :")

if save_as_files in ("Yes", "Y", "yes", "y"):
    with open("password.txt", "a", encoding="utf-8") as file:
        file.write(final_password)
else:
    print("Password Not Saved InTo File!")
