text = input("Enter a string: ")
char = input("Enter a character: ")
if char in text:
    print("First occurrence:", text.find(char))
    print("Last occurrence:", text.rfind(char))
else:
    print("Character not found")
