numbers = [10, 40, 20, 90, 70, 30]
unique_numbers = list(set(numbers))
unique_numbers.sort()
if len(unique_numbers) >= 2:
    print("Second largest:", unique_numbers[-2])
else:
    print("List does not have two distinct elements")
