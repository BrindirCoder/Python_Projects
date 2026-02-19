import time
import sys

total = 30  # length of the loading bar

print("Loading...")

for i in range(total + 1):
    percent = int((i / total) * 100)
    bar = "█" * i + "-" * (total - i)
    sys.stdout.write(f"\r[{bar}] {percent}%")
    sys.stdout.flush()
    time.sleep(0.05)

print("\nDone ✅")
