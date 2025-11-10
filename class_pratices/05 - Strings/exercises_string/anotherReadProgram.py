text = input("Digite uma frase: ")
found_vowels = []
vowel_count = 0
for char in text:
    if char in "aeiou":
        found_vowels.append(char)
        vowel_count += 1
print("Vogais encontradas:", found_vowels)
print("Total de vogais:", vowel_count)