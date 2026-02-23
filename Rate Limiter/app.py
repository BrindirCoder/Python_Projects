import time
from collections import deque

MAX_REQUESTS = 5   # allowed requests
TIME_WINDOW = 10  # seconds

requests = deque()

while True:
    input("Press Enter to make a request...")

    now = time.time()
    requests.append(now)

    # Remove old requests outside the time window
    while requests and now - requests[0] > TIME_WINDOW:
        requests.popleft()

    if len(requests) > MAX_REQUESTS:
        print("🚫 Too many requests! Slow down.")
    else:
        print("✅ Request allowed.")
