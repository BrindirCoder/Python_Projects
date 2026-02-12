import time

SESSION_DURATION = 10  # seconds

print("Login successful ✅")
start_time = time.time()

while True:
    current_time = time.time()
    elapsed = current_time - start_time

    if elapsed > SESSION_DURATION:
        print("\nSession expired ⏳❌")
        break

    print(f"Session active... {int(SESSION_DURATION - elapsed)}s left", end="\r")
    time.sleep(1)
