# 1.. write a programe to take a string input from the user and print it in reverse.

# s = input("Enter a string: ")
# rev = s[::-1]
# print("Reversed string:", rev)



# 2..write a programe to count the number of uppercase and lowercase characters in a string.

# s = input("Enter a string: ")
# upper = 0
# lower = 0
# for ch in s:
#     if ch.isupper():
#         upper += 1
#     elif ch.islower():
#         lower += 1
# print("Uppercase letters:", upper)
# print("Lowercase letters:", lower)



# 3..write a programe to check whether a given string contains only digits.

# s = input("Enter a string: ")
# if s.isdigit():
#     print("The string contains only digits")
# else:
#     print("The string does not contain only digits")



# 4..wap to replacce all spaces in a string with underscore(_).

# s = input("Enter a string: ")
# result = s.replace(" ", "_")
# print("Modified string:", result)


# 5..write a programe to count the frequency of each character in a string.

# s = input("Enter a string: ")
# freq = {}
# for ch in s:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] = 1
# print("Character frequency:")
# for k, v in freq.items():
#     print(k, ":", v)



# 6..wap to find the first and last occurence of a character in a string.

# s = input("Enter a string: ")
# ch = input("Enter a character: ")
# first = -1
# last = -1
# for i in range(len(s)):
#     if s[i] == ch:
#         if first == -1:
#             first = i
#         last = i
# print("First occurrence:", first)
# print("Last occurrence:", last)


# 7..wap to remove all vowels from agiven string.

# s = input("Enter a string: ")
# result = ""
# for ch in s:
#     if ch.lower() not in "aeiou":
#         result += ch
# print("String without vowels:", result)



# 8..wap to check whether two string are anagrams of each other.

# s1 = input("Enter first string: ")
# s2 = input("Enter second string: ")
# if sorted(s1) == sorted(s2):
#     print("Strings are anagrams")
# else:
#     print("Strings are not anagrams")



# 9..wap to capitalized the first leater of each word in a string.

# s = input("Enter a string: ")
# words = s.split()
# result = ""
# for w in words:
#     result += w[0].upper() + w[1:] + " "
# print("Capitalized string:", result.strip())



# 10..wap to check whether a given string is a palindrome without using built in reverse functions.
# s = input("Enter a string: ")
# rev = ""
# for ch in s:
#     rev = ch + rev
# if s == rev:
#     print("String is a palindrome")
# else:
#     print("String is not a palindrome")