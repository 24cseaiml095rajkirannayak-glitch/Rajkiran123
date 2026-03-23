sentence = input("Enter a sentence: ")

vowels_set = "aeiouAEIOU"
vowels = consonants = 0

for ch in sentence:
    if ch.isalpha():
        if ch in vowels_set:
            vowels += 1
        else:
            consonants += 1

reversed_sentence = sentence[::-1]
underscored = sentence.replace(" ", "_")
capitalized = " ".join(word.capitalize() for word in sentence.split())

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Reversed:", reversed_sentence)
print("Underscores:", underscored)
print("Capitalized:", capitalized)
