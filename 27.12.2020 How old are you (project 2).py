print("Hello user")
name = input("what is your name?      ")
print("Hello", name,"in your name",len(name),"letters")
year = int(input("When did you born?   "))
print(year,"Your age")
if len(str(year)) == 4:
    print(len(str(year)))
    print(2020 - year)
else:
    print("You make mistake")
