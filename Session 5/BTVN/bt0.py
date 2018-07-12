sentence = input ("Enter a sentence? ")

sentence = "".join(sentence.split())

sentence = sentence.lower()

count_letter = {}

for letter in sentence:
    count_letter[letter] = count_letter.get(letter, 0) + 1

for k in count_letter.keys():
    print (k, count_letter[k] )

