word = input("Скажи слово    ")
word2 = word[::-1].lower()
if word.lower() == word2:
    print ("Это палендром")
else:
    print("Это не палендром")
