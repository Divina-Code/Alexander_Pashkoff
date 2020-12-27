decide = False
a = 6
while decide != True:
    a = a - 1
    answer = int(input("7 * 8    "))
    if answer == 56:
        print("Да ты большой молодец")
        decide = True
    elif answer == 0:
        print("Не ленись!")
    elif a == 1:
        print("У тебя единица, садись")
        exit()
    else:
        print("Подумай заново")
print("Ты решил эту задачу, твоя оценка", a)
