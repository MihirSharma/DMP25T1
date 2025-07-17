VOWELS = "AEIOUaeiou"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"

sentence = input("Sentence: ")

vowelCount = 0
consonantCount = 0

for character in sentence:
    if character in VOWELS:
        vowelCount += 1
    elif character in CONSONANTS:
        consonantCount += 1
words = len(sentence.split(" "))

print ("Number of Words: " + str(words) + "\nNumber of vowels: " + str(vowelCount) + "\nNumber of consonants: " + str(consonantCount))