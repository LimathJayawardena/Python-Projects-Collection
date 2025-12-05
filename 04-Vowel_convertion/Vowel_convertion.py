word = input("Enter a word: ")
vowel_count = 0
A_letter = 0
E_letter = 0
I_letter = 0
O_letter = 0
U_letter = 0


for letter in word:
    if letter.lower() in 'aeiou':
        vowel_count += 1
for letter_A in word:
    if letter_A.lower() in 'a':
        A_letter += 1
for letter_E in word:
    if letter_E.lower() in 'e':
        E_letter += 1
for letter_I in word:
    if letter_I.lower() in 'i':
        I_letter += 1
for letter_O in word:
    if letter_O.lower() in 'o':
        O_letter += 1
for letter_U in word:
    if letter_U.lower() in 'u':
        U_letter += 1


print("Number of vowels in the word:", vowel_count)
print(f"There are {A_letter} A letters")
print(f"There are {E_letter} E letters")
print(f"There are {I_letter} I letters")
print(f"There are {O_letter} O letters")
print(f"There are {U_letter} U letters")
