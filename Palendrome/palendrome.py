import scrabble

longestword = ""

for word in scrabble.wordlist:
    is_palendrome = True
    for count in range(len(word)):
        if word[count] != word[-(count+1)]:
            is_palendrome = False
    if is_palendrome == True and len(word) > len(longestword):
        longestword = word
print(longestword)