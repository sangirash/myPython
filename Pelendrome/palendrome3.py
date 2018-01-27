import scrabble

longestword = ""

for word in scrabble.wordlist:
    if word == word[::-1] and len(word) > len(longestword):
        longestword = word
print(longestword)