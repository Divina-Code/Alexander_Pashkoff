word = input("Скажи слова   ")
word = word.split(" ")
print(word)
for a in word:
    word2 = a[::-1].lower()
    if a.lower() == word2:
        print (a,"Это палендром")
    else:
        print(a,"Это не палендром")
