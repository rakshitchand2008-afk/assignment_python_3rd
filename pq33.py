numbers = [10, 20, 30, 40, 50]
element = int(input("Enter element to remove: "))
if element in numbers:
    numbers.remove(element)
else:
    print("Element not found")
print("Updated list:", numbers)
