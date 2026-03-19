# def reverse_string(s):
#     return s[::-1]


# def is_palindrome(s):
#     return s == s[::-1]


# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)

# def count_vowels(s):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in s:
#         if char in vowels:
#             count += 1
#     return count

# def find_largest(lst):
#     largest = lst[0]
#     for num in lst:
#         if num > largest:
#             largest = num
#     return largest


# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def sum_of_digits(n):
#     total = 0
#     while n > 0:
#         total += n % 10
#         n //= 10
#     return total

# def fibonacci(n):
#     fib = []
#     a, b = 0, 1
#     for _ in range(n):
#         fib.append(a)
#         a, b = b, a + b
#     return fib

# def remove_duplicates(lst):
#     result = []
#     for item in lst:
#         if item not in result:
#             result.append(item)
#     return result


# def string_length(s):
#     count = 0
#     for _ in s:
#         count += 1
#     return count