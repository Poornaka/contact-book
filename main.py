# contact book by Poornaka @ 2021

print("Contact book")

while True:
    d = str(input("To see your contacts press, {}, to add contact {}, to delete press {}, to exit press {}: ".format("s", "a", "d", "e")))
    if d == 's':
        file = open("contacts.txt", "r")
        print(file.read())
    elif d == 'a':
        file = open("contacts.txt", "a")
        name = str(input("enter name of contact: "))
        number = str(input("enter number of contact: "))
        confirm = str(input("confirm by pressing c: "))
        if confirm == 'c':
            file.write("\n {} - {}".format(name, number))
            file = open("contacts.txt", "r")
            print("Successfully added your contact...")
            print(file.read())
    elif d == 'd':
        print('Still adding feature')
    elif d == 'e':
        exit()
        
