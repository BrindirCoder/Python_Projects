import subprocess
import time

def get_signal_strength():
    result = subprocess.check_output(
        ["netsh", "wlan", "show", "interfaces"]
    ).decode()

    for line in result.split("\n"):
        if "Signal" in line:
            return line.split(":")[1].strip()
        
while True:
    strength = get_signal_strength()

    print("WiFi Signal Strength:", strength)

    time.sleep(2)

    # befor run the code run this command 
    # netsh wlan show interfaces
    # and open your location 
    # setting => security & privacy => location => turn on
