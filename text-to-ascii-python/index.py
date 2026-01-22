#Install the library 
#pip install pyfiglet

import pyfiglet

text = input("✍️ Enter text to convert to ASCII art: ")

ascii_art = pyfiglet.figlet_format(text)

print("\n" + ascii_art)
