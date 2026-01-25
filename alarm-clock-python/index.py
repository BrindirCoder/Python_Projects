import time
from datetime import datetime

print("⏰ Simple Alarm Clock ⏰")

alarm_hour = int(input("Set hour (0-23): "))
alarm_minute = int(input("Set minute (0-59): "))

print("\nAlarm is set...")
print("Waiting...\n")

while True:
    now = datetime.now()
    current_hour = now.hour
    current_minute = now.minute

    if current_hour == alarm_hour and current_minute == alarm_minute:
        print("⏰⏰⏰ ALARM! TIME IS UP! ⏰⏰⏰")
        break

    time.sleep(30)
