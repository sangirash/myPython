import scrabble

longestword = ""

for word in scrabble.wordlist:
    if list(word) == list(reversed(word)) and len(word) > len(longestword):
        longestword = word
print(longestword)