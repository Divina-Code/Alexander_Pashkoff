import random
random_count = random.randint(0,100)
decide = False
a = 0
bad = -1
while decide != True:
    my_count = int(input("Please,enter the estimated number\n          "))
    a = a + 1
    if my_count == random_count:
        print("Wow, this is the correct answer\n")
        decide = True
    elif my_count == bad:
        print("It happened before\n")
    elif my_count >= random_count:
        print("Take less\n")
        bad = my_count
    elif my_count <= random_count:
        print("Take more\n")
        bad = my_count
print("You guessed this number,\n You guessed right by", a,"trying")
