numbers = [10, 20, 30, 40]
element = int(input("Enter element to insert: "))
position = int(input("Enter position (0-based index): "))
numbers.insert(position, element)
print("Updated list:", numbers)
