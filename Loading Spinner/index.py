import sys
import time
import itertools

NEON_GREEN = "\033[92m"
NEON_PINK = "\033[95m"
NEON_BLUE = "\033[94m"
RESET = "\033[0m"

spinner = itertools.cycle(["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"])
colors = itertools.cycle([NEON_GREEN, NEON_PINK, NEON_BLUE])

for _ in range(200):
    char = next(spinner)
    color = next(colors)
    sys.stdout.write(f"\r{color}Loading {char}{RESET}")
    sys.stdout.flush()
    time.sleep(0.05)

print("\nDone ✅")
