text = input("Enter a string: ")
char = input("Enter the character to check: ")
if text.startswith(char) and text.endswith(char):
    print("The string starts and ends with", char)
else:
    print("The string does not start and end with", char)
