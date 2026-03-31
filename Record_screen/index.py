import cv2    # pip install opencv-python 
import numpy as np # pip install numpy
import pyautogui # pip install pyautogui

screen_size = pyautogui.size()

fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("screen_record.avi", fourcc, 10.0, screen_size)

print("Recording... Press Ctrl+C to stop")

try:
    while True:
        screenshot = pyautogui.screenshot()
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        out.write(frame)

except KeyboardInterrupt:
    print("Recording stopped")

out.release()
cv2.destroyAllWindows()





