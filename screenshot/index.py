import pyautogui  # pip install pyautogui

while True:
    key = input("Press 's' to take screenshot: ").lower()

    if key == "s":
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")
        print("Screenshot saved!")

    else:
        print("Screenshot saving failed.")
        break
