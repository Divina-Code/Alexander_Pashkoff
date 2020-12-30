d = {}
while True:
    s = input("Нажмите l чтобы добавить слово, Нажмите R чтобы открыть список, Нажмите Q чтобы начть играть, Нажмите U чтобы удалить элемент, Нажмите G чтобы удалить всё    ")
    if s == "l":
        a = input("Скажите слово и перевод   ").split()
        if len(a) == 2:
            name = a[0]
            translate = a[1]
            if d.get(name) == None:
                 d[name] = translate
                 print("Слово успешно добавленно")
            else:
                print("Такое слово уже есть ")
        else:
            print("Попробуй ещё раз ")
    if s == "r":
        print(" ".join(d))
    if s == "u":
        name = input("Кого удалить? ")
        if d.get(name) == None:
            print("Такого нет")
        else:
            d.pop(name)
            print("Пользователь", name ,"удалён")
    if s == "g":
        dict.clear(d)
    if s == "q":
        print("Давай сыграем")

