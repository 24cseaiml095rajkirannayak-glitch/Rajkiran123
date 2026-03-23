strings = ["apple pie", "bob", "level", "python programming", "noon"]

# Sort by length
sorted_by_len = sorted(strings, key=len)
print("Sorted by length:", sorted_by_len)

# Palindromes
palindromes = [s for s in strings if s.replace(" ", "").lower() == s.replace(" ", "").lower()[::-1]]
print("Palindromes:", palindromes)

# Replace spaces with hyphens using list comprehension
hyphenated = [s.replace(" ", "-") for s in strings]
print("Hyphenated list:", hyphenated)
