mixed_tuple = (1, 5, 12, "hello", 8, 25, 3.14, 9)

lst = list(mixed_tuple)
lst = [x for x in lst if not (isinstance(x, int) and x < 10)]
result_tuple = tuple(lst)

print("Original tuple:", mixed_tuple)
print("Modified tuple:", result_tuple)
