from plyer import notification  #pip install plyer
import time

title = "Reminder"
message = "Time to take a break!"

seconds = 5  # change this time

print("Reminder started...")

time.sleep(seconds)

notification.notify(
    title=title,
    message=message,
    timeout=5
)

print("Notification sent!")
