sentence = input("Enter a sentence: ")

cleaned = "".join(ch.lower() for ch in sentence if ch.isalnum())
freq = {}

for ch in cleaned:
    freq[ch] = freq.get(ch, 0) + 1

print("Characters that appear only once:")
for ch, count in freq.items():
    if count == 1:
        print(ch, end=" ")
print()
