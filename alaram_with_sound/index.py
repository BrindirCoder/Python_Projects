import time
import winsound

alarm_time = input("Set alarm time (HH:MM:SS): ")

print("Alarm set for", alarm_time)

while True:
    current_time = time.strftime("%H:%M:%S")
    print(current_time)

    if current_time == alarm_time:
        print("Wake up!")

    # Play sound
        winsound.Beep(1000, 1000)   #(Works on Windows. On other systems, you can use playsound instead.)
        break
    time.sleep(1)
    
