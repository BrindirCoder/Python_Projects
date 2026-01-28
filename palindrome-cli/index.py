text = input("Enter a word or sentence: ")

clean_text = text.lower().replace(" ", "")

if clean_text == clean_text[::-1]:
    print("✅ It's a palindrome!")
else:
    print("❌ Not a palindrome.")
