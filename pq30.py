numbers = [10, 15, 22, 33, 40, 51]
even = sum(1 for number in numbers if number % 2 == 0)
odd = len(numbers) - even
print("Even elements:", even)
print("Odd elements:", odd)
