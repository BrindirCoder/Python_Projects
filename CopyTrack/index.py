import pyperclip
import time

history = []

print("Clipboard Manager running...")

while True:
    text = pyperclip.paste()

    if not history or text != history[-1]:
        history.append(text)
        print(f"Copied: {text}")

    time.sleep(1)
