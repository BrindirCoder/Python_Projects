import psutil  #pip install psutil
import time
import os
while True:
    os.system("cls" if os.name == "nt" else "clear")

    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    print("=== System Monitor ===")
    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory}%")
    print(f"Disk Usage: {disk}%")

    time.sleep(1)
