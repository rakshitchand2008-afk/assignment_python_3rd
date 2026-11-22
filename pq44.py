original = [1, 2, 3]
assigned = original
copied = original.copy()
original.append(4)
print("Original:", original)
print("Direct assignment:", assigned)
print("copy() result:", copied)
print("copy() creates an independent list, while direct assignment refers to the same list.")
