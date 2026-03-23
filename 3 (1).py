mixed = (1, "hello", 3.5, 20, True, 7, "abc")
t2 = (100, 200)

# Filter numeric values
numeric_values = tuple(x for x in mixed if isinstance(x, (int, float)) and not isinstance(x, bool))
print("Numeric values:", numeric_values)

# Attempt modification
try:
    mixed[0] = 99
except TypeError as e:
    print("Error (tuples are immutable):", e)

# Concatenate tuples
concatenated = mixed + t2
print("Concatenated tuple:", concatenated)
