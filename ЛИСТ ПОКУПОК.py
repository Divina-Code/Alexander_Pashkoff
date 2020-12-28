MyList = [] #
while True:
    answer = input("Добавьте объект, для этого напечатайте добавить,удалите объект нажмите удалить и выбирете объект и нажмите прочитать, чтобы раскрыть список, напишие сортировать,чтобы отсортировать список        ")
    if answer == "добавить":
        product_add = input("Что именно вы хотели бы добавить?      ")
        MyList.append(product_add)
    if answer == "удалить":
        product_delete = input("Что именно вы хотели бы удалить?      ")
        MyList.pop(product_delete)
    if answer == "прочитать":
        print(MyList)
    if answer == "сортировать":
       MyList.sort()
       print(MyList)











