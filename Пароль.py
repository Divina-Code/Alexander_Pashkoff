import random
w = int(input("Сколько будет цифр в вашем пароле?    "))
letter = list("abcdefghigklmnopqrstuvwxz!@#$%^&*_+-*/`")
massiv = []

for q in range(w):
    a = letter[random.randint(0,38)]
    massiv.append(a)
print(" ".join(massiv))

