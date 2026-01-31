s = "programming"
count = 0
for ch in s:
    if ch in "aeiou":
        count += 1
print(count)

"""
s = "programming"
vowels = "aeiouAEIOU"
v = c = 0

for ch in s:
    if ch.isalpha():
        if ch in vowels:
            v += 1
        else:
            c += 1

print("Vowels:", v)
print("Consonants:", c)

"""