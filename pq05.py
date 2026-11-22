text = input("Enter a string: ")
normalized = text.lower().replace(" ", "")
if normalized == normalized[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
