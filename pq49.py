original = (10, 20, 30)
print("Original tuple:", original)
# Tuples cannot be changed directly. Create a modified tuple using concatenation.
modified = original[:1] + (25,) + original[2:]
print("Modified tuple:", modified)
