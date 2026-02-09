import secrets
import time

otp = secrets.randbelow(900000) + 100000  # 6-digit OTP

print("Your OTP is:", otp)

for i in range(10, 0, -1):
    print(f"Expires in {i} seconds...", end="\r")
    time.sleep(1)

print("\nOTP expired ❌")
