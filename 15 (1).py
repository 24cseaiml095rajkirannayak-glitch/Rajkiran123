s = input("Enter a string: ")

# Palindrome check
clean = "".join(ch.lower() for ch in s if ch.isalnum())
is_pal = clean == clean[::-1]

vowels = consonants = digits = special = 0
vowels_set = "aeiouAEIOU"

for ch in s:
    if ch.isalpha():
        if ch in vowels_set:
            vowels += 1
        else:
            consonants += 1
    elif ch.isdigit():
        digits += 1
    else:
        special += 1

print("Palindrome:", is_pal)
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Special characters:", special)
